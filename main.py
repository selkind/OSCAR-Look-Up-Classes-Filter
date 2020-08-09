import sys
import argparse
import os
import pandas as pd
import pprint as pp
import logging

def main(file_path):
    pass

if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s\n%(levelname)s: %(message)s", 
        datefmt="%Y/%m/%d %I:%M%S %p", level=logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "filepath", 
        nargs=1, 
        type=str, 
        metavar="path/to/html/source",
        help="The absolute path to the html file containing the courses searched")
    args = parser.parse_args()

    logging.info(f"Attempting to parse file: {args.filepath[0]}")
    main(args)

