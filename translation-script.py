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
        
    # read each line in the file
    with open(pathToInputFile) as iFile:
        # split data in file into an array
        enWords = iFile.read().split()
        cleanedEnWords = list(dict.fromkeys(enWords))

        # translate elements
        translator = Translator(to_lang="de")
        
        for word in cleanedEnWords:
            # translate elements
            translation = translator.translate(word)
            newWordTranslations.append([word, translation])
            
        # output csv file with translations
        with open(ankiFile, 'w', newline= '') as aFile:
            ankiFileCsv = csv.writer(aFile)
            ankiFileCsv.writerows(newWordTranslations)


if __name__ == "__main__":
    main()
