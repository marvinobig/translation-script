#!/usr/bin/env python3

import sys
import os
import csv
import uuid
from translate import Translator


def main():
    # get input file
    pathToInputFile = sys.argv[1]
    fileExtension = os.path.splitext(pathToInputFile)[1]
    ankiFile = f"./anki_{uuid.uuid4()}.csv"
    newWordTranslations = []

    # check it is a txt file
    if fileExtension != ".txt":
        print("Input file is not a .txt file")
        return -1
    
    # check the file exists
    if not os.path.isfile(pathToInputFile):
        print("Input file does not exist")
        return -1
        



if __name__ == "__main__":
    main()
