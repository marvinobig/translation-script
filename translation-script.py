#!/usr/bin/env python3

import sys
import os
import csv
from translate import Translator


def main():
    # get input file
    pathToInputFile = sys.argv[1]
    fileExtension = os.path.splitext(pathToInputFile)[1]
    ankiFile = "./anki.csv"
    newWordTranslations = []




if __name__ == "__main__":
    main()
