import sys
import argparse
import os
import pandas as pd
import pprint as pp

def main(file_path):
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", 
        nargs=1, 
        type=str, 
        metavar="path/to/html/source",
        help="The absolute path to the html file containing the courses searched")
    args = parser.parse_args()

    print(args.filepath[0])

