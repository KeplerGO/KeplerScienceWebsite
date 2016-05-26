"""Prepares an overview of the K2 programs and summaries for the website.
"""
import os
import re
import pandas as pd


class TargetList(object):
    """Class for interacting with a target list in Tom's CSV format."""

    def __init__(self, csv_filename):
        self.csv_filename = csv_filename
        self._df = pd.read_csv(csv_filename)
        # The column names in the target lists aren't consistent
        if " Investigation IDs" in self._df:
            self._programs_key = " Investigation IDs"
        else:
            self._programs_key = "Investigation IDs"

    def get_unique_programs(self):
        """Returns a sorted list of unique program ids in the target list."""
        all_ids = []
        for program_id in self._df[self._programs_key]:
            all_ids.extend(program_id.split("|"))
        unique_ids = sorted(
                             set(
                                  [program_id.split("_")[0].strip()
                                   for program_id in all_ids
                                   if program_id.strip().startswith("GO")]
                             )
                     )
        #if "c9" in self.csv_filename:
        #    unique_ids.append("GO9901")  # Only C9 program with all targets in C9 superstamp
        #    unique_ids.append("GO9005")  # C9b late targets had not been selected at time of page creation
        #    unique_ids.sort()
        return unique_ids

    def get_targets(self, program_id):
        """Returns the list of EPIC IDs for a single program."""
        mask = self._df[self._programs_key].str.contains(program_id)
        return self._df.loc[mask]


class ProgramList(object):
    """Class for interacting with a program list in NSPIRES's Excel format."""

    def __init__(self, table_filename):
        if table_filename.endswith("xls"):
            self._df = pd.read_excel(table_filename)
        else:
            self._df = pd.read_csv(table_filename)

    def get_program(self, program_id):
      try:
        return self._df.loc[self._df['program_id'] == program_id].iloc[0]
      except KeyError:
        # The excel sheets contain the response sequence number rather than the GO id
        seqnum = int(program_id[3:])
        try:
            return self._df.loc[self._df['Response seq number'] == seqnum].iloc[0]
        except IndexError:  # Program not in list
            return None


class WebSummaryCreator(object):

    def __init__(self, targetlist, programlist, campaign=None):
        self.targetlist = targetlist
        self.programlist = programlist
        self.programs = self.targetlist.get_unique_programs()
        self.campaign = campaign

    def to_html(self):
        html = (".. raw:: html\n\n"
                "  <div class='panel panel-primary'>\n\n"
                "    <div class='panel-heading'>\n"
                "      <h3 class='panel-title'>Programs that contributed to the Campaign " + str(self.campaign) + " target list</h3>\n"
                "    </div>\n\n"
                "    <div class='panel-body'>\n"
                "      <i>Click on a title to view the abstract. Click on the number of targets to download the target list.</i>\n"
                "      <table class='table table-striped table-hover'>\n"
                "        <thead>\n"
                "        <tr>\n"
                "          <th>Program</th>\n"
                "          <th style='min-width:7em;'>PI</th>\n"
                "          <th>Title</th>\n"
                "          <th>Targets</th>\n"
                "        </tr>\n"
                "        </thead>\n\n")
        for program_id in self.programs:
            program = self.programlist.get_program(program_id)
            if program is None:
                continue
            targets = self.targetlist.get_targets(program_id)
            if self.campaign not in ['0', '1', '2', '3']:
                url_summary = "data/k2-programs/{}.txt".format(program_id)
            else:
                edit_program_id = program_id.replace("GO3", "GO2")
                url_summary = "data/k2-programs/{}_{}.pdf".format(edit_program_id, program["PI Last name"])
            url_targets = "data/k2-programs/{}-targets.csv".format(program_id)
            html += (
                        "        <tr>\n"
                        "          <td>{}</td>\n"
                        "          <td>{}</td>\n"
                        "          <td><a href='{}'>{}</a></td>\n"
                        "          <td class='text-right'><a href='{}'>{}</a></td>\n"
                        "        </tr>\n\n".format(program_id,
                                                   program["PI Last name"],
                                                   url_summary,
                                                   program["Title"].translate(dict.fromkeys(range(1, 32))),
                                                   url_targets,
                                                   len(targets))
                     )
        html += "      </table>\n    </div>\n  </div>\n"
        return html

    def write_html(self, output_fn):
        with open(output_fn, "w") as output:
            print("Writing {}".format(output_fn))
            output.write(self.to_html())

    def write_summaries(self, output_dir=""):
        """Produce txt files for all programs with title/summary/targets."""
        for program_id in self.programs:
            program = self.programlist.get_program(program_id)
            if program is None:
                continue
            program = program.fillna("")
            targets = self.targetlist.get_targets(program_id)
            if program["PI Middle name"] == "":
                pi_name = (program["PI Last name"] +
                           ", " + program["PI First name"])
            else:
                pi_name = (program["PI Last name"] +
                           ", " + program["PI First name"] +
                           " " + program["PI Middle name"])
            if program["Company name"] == "":
                pi_institute = program["Linked Org"]
            else:
                pi_institute = program["Company name"]
            # In early K2 days we had to submit proposals for foreign PIs or something
            if pi_institute.startswith("Bay Area"):
                pi_institute = ""
            co_investigators = []
            for idx in range(1, 99):  # Number of "Member" columns is variable
                try:
                    field = program["Member - {} Member name; Role; Email; Organization; Phone".format(idx)]
                    if field != "":
                        co_investigators.append(field.split(";")[0].strip())
                except KeyError:
                    continue  # Max number of "Member" columns reached

            # Some abstracts contain control characters (wtf?), remove these
            summary = program["Summary"].translate(dict.fromkeys(range(14, 32)))
            # Also remove excessive whitespace
            summary = summary.replace("\n\n\n\n", "\n\n").replace("\n\n\n", "\n\n")
            # Only allow two whitespaces after a period
            summary = re.sub("(?<!\.)(\n\n)", " ", summary)
            # ... unless it's a numeric listing
            summary = re.sub("(\n\n)(\d)", "\n\\2", summary)

            output_fn = os.path.join(output_dir, "{}.txt".format(program_id))
            with open(output_fn, "w") as output:
                print("Writing {}".format(output_fn))
                output.write("# Summary of K2 Program {}\n\nTitle: {}\n\n"
                             "PI: {} ({})\nCoIs: {}\n\n{}\n\n"
                             "# Targets requested by this program "
                             "that have been observed ({})\n{}"
                             "".format(program_id,
                                       program["Title"],
                                       pi_name,
                                       pi_institute,
                                       "; ".join(co_investigators),
                                       summary,
                                       len(targets),
                                       targets.to_csv(index=False)
                                       )
                             )

    def write_targetlists(self, output_dir=""):
        """Write a CSV target list for each program."""
        for program_id in self.programs:
            program = self.programlist.get_program(program_id)
            if program is None:
                continue
            targets = self.targetlist.get_targets(program_id)
            output_fn = os.path.join(output_dir, "{}-targets.csv".format(program_id))
            with open(output_fn, "w") as output:
                print("Writing {}".format(output_fn))
                output.write(targets.to_csv(index=False))


CFG = {
       "summaries_dir": "/home/gb/dev/KeplerScienceWebsite/content/data/k2-programs/",
       "0": {
                "targetlist": "/home/gb/dev/KeplerScienceWebsite/content/data/campaigns/c0/K2Campaign0targets.csv",
                "programlist": "/home/gb/Dropbox/k2/k2-c0123-programs.csv"
            },
       "1": {
                "targetlist": "/home/gb/dev/KeplerScienceWebsite/content/data/campaigns/c1/K2Campaign1targets.csv",
                "programlist": "/home/gb/Dropbox/k2/k2-c0123-programs.csv"
            },
       "2": {
                "targetlist": "/home/gb/dev/KeplerScienceWebsite/content/data/campaigns/c2/K2Campaign2targets.csv",
                "programlist": "/home/gb/Dropbox/k2/k2-c0123-programs.csv"
            },
       "3": {
                "targetlist": "/home/gb/dev/KeplerScienceWebsite/content/data/campaigns/c3/K2Campaign3targets.csv",
                "programlist": "/home/gb/Dropbox/k2/k2-c0123-programs.csv"
            },
       "4": {
                "targetlist": "/home/gb/dev/KeplerScienceWebsite/content/data/campaigns/c4/K2Campaign4targets.csv",
                "programlist": "/home/gb/Dropbox/k2/Campaign4_5/K2GO1_programs_geert_edit.xls"
            },
       "5": {
                "targetlist": "/home/gb/dev/KeplerScienceWebsite/content/data/campaigns/c5/K2Campaign5targets.csv",
                "programlist": "/home/gb/Dropbox/k2/Campaign4_5/K2GO1_programs_geert_edit.xls"
            },
       "6": {
                "targetlist": "/home/gb/dev/KeplerScienceWebsite/content/data/campaigns/c6/K2Campaign6targets.csv",
                "programlist": "/home/gb/Dropbox/k2/Campaign6_7/K2GO2_1 Updated Investigation Report 1_28.xls"
            },
       "7": {
                "targetlist": "/home/gb/dev/KeplerScienceWebsite/content/data/campaigns/c7/K2Campaign7targets.csv",
                "programlist": "/home/gb/Dropbox/k2/Campaign6_7/K2GO2_1 Updated Investigation Report 1_28.xls"
            },
       "8": {
                "targetlist": "/home/gb/dev/KeplerScienceWebsite/content/data/campaigns/c8/K2Campaign8targets.csv",
                "programlist": "/home/gb/Dropbox/k2/Campaign8_9_10/K2GO3_2 Investigation Report.xls"
            },
       "9a": {
                "targetlist": "../../../data/campaigns/c9/K2Campaign9atargets.csv",
                "programlist": "../../../data/campaigns/c9/c9-programs.csv"
            },
       "9b": {
                "targetlist": "../../../data/campaigns/c9/K2Campaign9btargets.csv",
                "programlist": "../../../data/campaigns/c9/c9-programs.csv"
            },
       "10": {
                "targetlist": "/home/gb/dev/KeplerScienceWebsite/content/data/campaigns/c10/K2Campaign10targets.csv",
                "programlist": "/home/gb/Dropbox/k2/Campaign8_9_10/K2GO3_2 Investigation Report.xls"
            },
       }


def create_website_pages():
    for campaign in ['10']: #["0", "1", "2", "3", "4", "5", "6", "7", "8", "9a", "9b", "10"]:
        tl = TargetList(CFG[campaign]["targetlist"])
        pl = ProgramList(CFG[campaign]["programlist"])
        wsc = WebSummaryCreator(tl, pl, campaign=campaign)
        wsc.write_html("c{}.html".format(campaign))
        if campaign not in ['0', '1', '2', '3']:
          wsc.write_summaries(CFG["summaries_dir"])
        wsc.write_targetlists(CFG["summaries_dir"])


if __name__ == "__main__":
    create_website_pages()
