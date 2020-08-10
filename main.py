import sys
import argparse
import pandas as pd
import pprint as pp
import logging

CONTENTS_KEY = 5
TABLE_TOP_LEVEL_INDEX = "Computational Science & Engr"
DESIRED_SUBJECTS = ["CSE", "CS", "ISYE", "PUBP"]
UN_DESIRED_SECTIONS = ["OAN", "OCY", "OCL", "OAH"]
NUMERIC_COL_NAMES = ["CRN", "Crse", "Cred", "Cap", "Act", "Rem", "WL Cap", "WL Act", "WL Rem"]
USEFUL_COLS = ["CRN", "Subj", "Crse", "Sec", "Cred", "Title", "Cap", "Act", "Rem", "WL Cap", "WL Act", "WL Rem", "Instructor"]
SORT_COLUMNS = ["Subj", "WL Act"]
DEFAULT_OUT_PATH = "./filtered_courses.html"

def main(input_file_path, output_file_path=DEFAULT_OUT_PATH):
    with open(input_file_path, 'r') as f:
        data = pd.read_html(f)

    logging.info("Raw data loaded")

    table_data = data[CONTENTS_KEY][TABLE_TOP_LEVEL_INDEX]
    logging.debug(table_data["Subj"].unique())

    subj_filtered_data = table_data[table_data["Subj"].isin(DESIRED_SUBJECTS)]
    logging.debug(subj_filtered_data["Subj"].unique())

    logging.debug(subj_filtered_data["Sec"].unique())
    section_filtered_data = subj_filtered_data[~subj_filtered_data["Sec"].isin(UN_DESIRED_SECTIONS)]
    logging.debug(section_filtered_data["Sec"].unique())

    section_filtered_data[NUMERIC_COL_NAMES] = section_filtered_data[NUMERIC_COL_NAMES].apply(pd.to_numeric, errors="ignore")

    useful_data = section_filtered_data.sort_values(SORT_COLUMNS)[USEFUL_COLS]

    with open(output_file_path, 'w+') as f_out:
        f_out.write(useful_data.to_html())

    logging.info(f"Filtered table written to {output_file_path}")

if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s\n%(levelname)s: %(message)s\n", 
        datefmt="%Y/%m/%d %I:%M:%S %p", level=logging.INFO)

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "input_file_path", 
        nargs=1, 
        type=str, 
        metavar="path/to/html/source",
        help="The absolute path to the html file containing the courses searched")

    parser.add_argument(
        "output_file_path", 
        nargs=1, 
        type=str, 
        metavar="path/to/html/output",
        help="The absolute path to the html file containing the filtered courses")
    args = parser.parse_args()
    logging.debug(args)

    logging.info(f"Attempting to parse file: {args.input_file_path[0]}")
    main(args.input_file_path[0], args.output_file_path[0])

