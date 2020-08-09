import sys
import argparse
import pandas as pd
import pprint as pp
import logging

contents_key = 5
table_top_level_index = "Computational Science & Engr"
desired_subjects = ["CSE", "CS", "ISYE", "PUBP"]
un_desired_sections = ["OAN", "OCY", "OCL", "OAH"]
numeric_col_names = ["CRN", "Crse", "Cred", "Cap", "Act", "Rem", "WL Cap", "WL Act", "WL Rem"]
useful_cols = ["CRN", "Subj", "Crse", "Sec", "Cred", "Title", "Cap", "Act", "Rem", "WL Cap", "WL Act", "WL Rem", "Instructor"]
SORT_COLUMNS = ["Subj", "WL Act"]
OUT_PATH = "/mnt/c/Users/samue/Desktop/filtered_table.html"

def main(file_path):
    with open(file_path, 'r') as f:
        data = pd.read_html(f)

    logging.info("Raw data loaded")

    table_data = data[contents_key][table_top_level_index]
    logging.debug(table_data["Subj"].unique())

    subj_filtered_data = table_data[table_data["Subj"].isin(desired_subjects)]
    logging.debug(subj_filtered_data["Subj"].unique())
    logging.debug(subj_filtered_data["Sec"].unique())

    section_filtered_data = subj_filtered_data[~subj_filtered_data["Sec"].isin(un_desired_sections)]

    logging.debug(section_filtered_data["Sec"].unique())

    section_filtered_data[numeric_col_names] = section_filtered_data[numeric_col_names].apply(pd.to_numeric, errors="ignore")

    useful_data = section_filtered_data.sort_values(SORT_COLUMNS)[useful_cols]

    with open(OUT_PATH, 'w+') as f_out:
        f_out.write(useful_data.to_html())

    logging.info(f"Filtered table written to {OUT_PATH}")

if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s\n%(levelname)s: %(message)s\n", 
        datefmt="%Y/%m/%d %I:%M:%S %p", level=logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "file_path", 
        nargs=1, 
        type=str, 
        metavar="path/to/html/source",
        help="The absolute path to the html file containing the courses searched")
    args = parser.parse_args()

    logging.info(f"Attempting to parse file: {args.file_path[0]}")
    main(args.file_path[0])

