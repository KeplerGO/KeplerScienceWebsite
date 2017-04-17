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
        return unique_ids

    def get_targets(self, program_id):
        """Returns the list of EPIC IDs for a single program."""
        mask = self._df[self._programs_key].str.contains(program_id)
        return self._df.loc[mask]


class ProgramList(object):
    """Class for interacting with a table listing all K2 programs."""
    def __init__(self, filename):
        self._df = pd.read_csv(filename)

    def get_program(self, program_id):
        try:
            return self._df.loc[self._df['program_id'] == program_id].iloc[0]
        except IndexError as e:
            raise Exception("ERROR: Could not find program {}".format(program_id))


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
                "      <i>Click on the title to view the abstract. Click on the number of targets to view the target list. Click on the icon to go to the data.</i>\n"
                "      <table class='table table-striped table-hover'>\n"
                "        <thead>\n"
                "        <tr>\n"
                "          <th>Program</th>\n"
                "          <th style='min-width:7em;'>PI</th>\n"
                "          <th>Title</th>\n"
                "          <th>Targets</th>\n"
                "          <th>Data</th>\n"
                "        </tr>\n"
                "        </thead>\n\n")
        for program_id in self.programs:
            program = self.programlist.get_program(program_id)
            if program is None:
                continue
            targets = self.targetlist.get_targets(program_id)
            # We do not have abstracts in text form for Cmapaigns 0-3,
            # because they were not submitted through NSPIRES.
            # For these, and for DDT programs, we can post the PDF instead.
            ddt_programs_with_pdf_abstract = ['GO4901', 'GO9901', 'GO9902', 'GO9903',
            'GO9904', 'GO9905', 'GO9906', 'GO9907', 'GO9908', 'GO9909', 'GO9910',
            'GO9911', 'GO9912', 'GO9913', 'GO9914', 'GO9915', 'GO9916', 'GO9917',
            'GO9918', 'GO9919', 'GO9920', 'GO9921', 'GO9922', 'GO9923', 'GO9924',
            'GO10901', 'GO10902', 'GO10903', 'GO10904', 'GO10905']
            if self.campaign not in ['0', '1', '2', '3'] and program_id not in ddt_programs_with_pdf_abstract:
                url_summary = "data/k2-programs/{}.txt".format(program_id)
            else:
                edit_program_id = program_id.replace("GO3", "GO2")
                url_summary = "data/k2-programs/{}_{}.pdf".format(edit_program_id, program["pi_last_name"])
            url_targets = "data/k2-programs/{}-targets.csv".format(program_id)
            url_archive = 'https://archive.stsci.edu/k2/data_search/search.php?action=Search&ktc_investigation_id={}'.format(program_id)
            html += (
                        "        <tr>\n"
                        "          <td>{}</td>\n"
                        "          <td>{}</td>\n"
                        "          <td><a href='{}'>{}</a></td>\n"
                        "          <td class='text-right'><a href='{}'>{}</a></td>\n"
                        "          <td class='text-center'><a href='{}'><i class='fa fa-external-link'></i></a></td>\n"
                        "        </tr>\n\n".format(program_id,
                                                   program["pi_last_name"],
                                                   url_summary,
                                                   program["title"].translate(dict.fromkeys(range(1, 32))),
                                                   url_targets,
                                                   len(targets),
                                                   url_archive)
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
            program = program.fillna("")
            targets = self.targetlist.get_targets(program_id)
            if program["pi_middle_name"] == "":
                pi_name = (program["pi_last_name"] +
                           ", " + program["pi_first_name"])
            else:
                pi_name = (program["pi_last_name"] +
                           ", " + program["pi_first_name"] +
                           " " + program["pi_middle_name"])

            output_fn = os.path.join(output_dir, "{}.txt".format(program_id))
            with open(output_fn, "w") as output:
                print("Writing {}".format(output_fn))
                output.write("# Summary of K2 Program {}\n\nTitle: {}\n\n"
                             "PI: {} ({})\nCoIs: {}\n\n{}\n\n"
                             "# Targets requested by this program "
                             "that have been observed ({})\n{}"
                             "".format(program_id,
                                       program["title"],
                                       pi_name,
                                       program["pi_institution"],
                                       program["coi_names"],
                                       program["summary"],
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


def create_website_pages():
    PATH = '/home/gb/dev/KeplerScienceWebsite'
    summaries_dir = PATH + "/content/data/k2-programs/"
    programlist = ProgramList('/home/gb/dev/YouHadOneJob/k2-programs-table/k2-programs.csv')
    for campaign in ["13"]:  #["0", "1", "2", "3", "4", "5", "6", "7", "8", "9a", "9b", "10", "11"]:
        if campaign in ['9a', '9b']:
            targetlist = PATH + '/content/data/campaigns/c9/K2Campaign{}targets.csv'.format(campaign)
        else:
            targetlist = PATH + '/content/data/campaigns/c{}/K2Campaign{}targets.csv'.format(campaign, campaign)
        tl = TargetList(targetlist)
        wsc = WebSummaryCreator(tl, programlist, campaign=campaign)
        wsc.write_html("c{}.html".format(campaign))
        if campaign not in ['0', '1', '2', '3']:  # We only have PDFs for these
            wsc.write_summaries(summaries_dir)
        wsc.write_targetlists(summaries_dir)

        # Write program_ids and target numbers to a text file we can use
        # to inform the PIs of the target management outcome
        with open('programlist-c{}.txt'.format(campaign), 'w') as out:
            out.write('program_id,targets\n')
            for programid in tl.get_unique_programs():
                out.write('{},{}\n'.format(programid, len(tl.get_targets(programid))))


if __name__ == "__main__":
    create_website_pages()
