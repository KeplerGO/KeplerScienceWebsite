"""Prepares an overview of the K2 programs and summaries for the website."""
import os
import re
import pandas as pd


class TargetList(object):
    """Class for interacting with a target list in Tom's CSV format."""

    def __init__(self, csv_filename):
        self._df = pd.read_csv(csv_filename)

    def get_unique_programs(self):
        """Returns a sorted list of unique program ids in the target list."""
        all_ids = []
        for program_id in self._df[" Investigation IDs"]:
            all_ids.extend(program_id.split("|"))
        unique_ids = sorted(
                             set(
                                  [program_id.split("_")[0].strip()
                                   for program_id in all_ids
                                   if program_id.strip().startswith("GO")]
                             )
                     )
        return unique_ids

    def get_targets(self, program_id):
        """Returns the list of EPIC IDs for a single program."""
        mask = self._df[" Investigation IDs"].str.contains(program_id)
        return self._df.loc[mask]


class ProgramList(object):
    """Class for interacting with a program list in NSPIRES's Excel format."""

    def __init__(self, excel_filename):
        self._df = pd.read_excel(excel_filename)

    def get_program(self, progam_id):
        seqnum = int(progam_id[3:])
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
                "      <i>Click on a title to view the abstract and a list of targets observed.</i>\n"
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
            url = "data/k2-programs/{}.txt".format(program_id)
            html += (
                        "        <tr>\n"
                        "          <td>{}</td>\n"
                        "          <td>{}</td>\n"
                        "          <td><a href='{}'>{}</a></td>\n"
                        "          <td class='text-right'>{}</td>\n"
                        "        </tr>\n\n".format(program_id,
                                                   program["PI Last name"],
                                                   url,
                                                   program["Title"].translate(dict.fromkeys(range(1, 32))),
                                                   len(targets))
                     )
        html += "      </table>\n    </div>\n  </div>\n"
        return html

    def write_html(self, output_fn):
        with open(output_fn, "w") as output:
            print("Writing {}".format(output_fn))
            output.write(self.to_html())

    def write_summaries(self, output_dir=""):
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

CFG = {
       "summaries_dir": "/home/gb/dev/KeplerScienceWebsite/content/data/k2-programs/",
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
       }

def create_website_pages():
    for campaign in ["4", "5", "6", "7", "8"]:
        tl = TargetList(CFG[campaign]["targetlist"])
        pl = ProgramList(CFG[campaign]["programlist"])
        wrf = WebSummaryCreator(tl, pl, campaign=campaign)
        wrf.write_html("c{}.html".format(campaign))
        wrf.write_summaries(CFG["summaries_dir"])


if __name__ == "__main__":
    create_website_pages()