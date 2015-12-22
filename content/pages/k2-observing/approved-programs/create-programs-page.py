"""Prepares an overview of the K2 programs and summaries for the website."""
import os
import logging
import pandas as pd

log = logging.getLogger("k2programs")
log.setLevel("INFO")


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
                                  [program_id.split("_")[0]
                                   for program_id in all_ids
                                   if program_id.startswith("GO")]
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
        return self._df.loc[self._df['Response seq number'] == seqnum].iloc[0]


class WebResourceFactory(object):

    def __init__(self, targetlist, programlist):
        self.targetlist = targetlist
        self.programlist = programlist
        self.programs = self.targetlist.get_unique_programs()

    def to_html(self):
        html = (".. raw:: html\n\n"
                "  <div class='panel panel-primary'>\n\n"
                "    <div class='panel-heading'>\n"
                "      <h3 class='panel-title'>Programs that contributed to the Campaign 8 target list</h3>\n"
                "    </div>\n\n"
                "    <div class='panel-body'>\n"
                "      <i>Click on the titles to view abstracts and target lists.</i>\n"
                "      <table class='table table-striped table-hover'>\n"
                "        <thead>\n"
                "        <tr>\n"
                "          <th>ID</th>\n"
                "          <th style='min-width:7em;'>PI</th>\n"
                "          <th>Title</th>\n"
                "          <th>Targets</th>\n"
                "        </tr>\n"
                "        </thead>\n\n")
        for program_id in self.programs:
            program = self.programlist.get_program(program_id)
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
                                                   program["Title"],
                                                   len(targets))
                     )
        html += "      </table>\n    </div>\n  </div>\n"
        return html

    def write_html(self, output_fn):
        with open(output_fn, "w") as output:
            log.info("Writing {}".format(output_fn))
            output.write(self.to_html())

    def write_summaries(self, output_dir=""):
        for program_id in self.programs:
            program = self.programlist.get_program(program_id).fillna("")
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
            for idx in range(1, 16):
                field = program["Member - {} Member name; Role; Email; Organization; Phone".format(idx)]
                if field != "":
                    co_investigators.append(field.split(";")[0].strip())

            # Some proposals manage to contain ascii control characters,
            # let's remove those
            summary = program["Summary"].translate(dict.fromkeys(range(14, 32)))

            output_fn = os.path.join(output_dir, "{}.txt".format(program_id))
            with open(output_fn, "w") as output:
                log.info("Writing {}".format(output_fn))
                output.write("# Summary of K2 Program {}\n\nTitle: {}\n\n"
                             "PI: {} ({})\nCoIs: {}\n\n{}\n\n\n"
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

if __name__ == "__main__":
    tl = TargetList("../../../data/campaigns/c8/K2Campaign8targets.csv")
    pl = ProgramList("/home/gb/Dropbox/k2/Campaign8_9_10/K2GO3_2 Investigation Report.xls")
    wrf = WebResourceFactory(tl, pl)
    wrf.write_html("c8.html")
    wrf.write_summaries("/home/gb/dev/KeplerScienceWebsite/content/data/k2-programs/")
