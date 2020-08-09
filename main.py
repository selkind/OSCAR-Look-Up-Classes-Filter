import sys
import argparse
import pandas as pd
import pprint as pp
import logging

contents_key = 5
table_top_level_index = "Computational Science & Engr"

def main(file_path):
    with open(file_path, 'r') as f:
        data = pd.read_html(f)
    logging.info("Raw data loaded")

    table_data = data[contents_key][table_top_level_index]
    logging.debug(table_data["Subj"].unique())



if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s\n%(levelname)s: %(message)s\n", 
        datefmt="%Y/%m/%d %I:%M%S %p", level=logging.DEBUG)

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

