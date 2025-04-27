#!/usr/bin/env python3

import sys
import os
import csv
import uuid
import string
from translate import Translator


def main():
    # get input file
    pathToInputFile = sys.argv[1]
    language = sys.argv[2]
    fileExtension = os.path.splitext(pathToInputFile)[1]
    ankiFile = f"./anki_{uuid.uuid4()}.csv"
    saveFile = "./save.txt"
    newWordTranslations = []
    newWords = []

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
        text = iFile.read()
        text = text.translate(str.maketrans('', '', string.punctuation)) 
        enWords = text.split()
        cleanedEnWords = list(dict.fromkeys(enWords))
        
        # save new words to txt file for future comparison
        with open(saveFile, 'a+') as sFile:
            sFile.seek(0)
            savedWords = sFile.read().lower().split()
            
            for word in cleanedEnWords:
                word = word.lower()
                
                if word not in savedWords:
                    sFile.write(f"{word}\n")
                    newWords.append(word)

        # translate elements
        translator = Translator(to_lang=language)
                
        if newWords:    
            for word in newWords:
                    translation = translator.translate(word)
                    newWordTranslations.append([word, translation])
                
            # output csv file with translations
            with open(ankiFile, 'w', newline= '') as aFile:
                ankiFileCsv = csv.writer(aFile)
                ankiFileCsv.writerows(newWordTranslations)
                
            print(f"Translated {len(newWords)} words")
            return 0
        else:
            print("No new words to translate")
            return -1


if __name__ == "__main__":
    main()
