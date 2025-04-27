#!/usr/bin/env python3

import sys
import os
import csv
import uuid
import string
from translate import Translator


def performChecks(pathToInputFile, fileExtension):
    # check it is a txt file
    if fileExtension != ".txt":
        raise Exception("Input file is not a .txt file")
    
    # check the file exists
    if not os.path.isfile(pathToInputFile):
        raise Exception("Input file does not exist")

def extractWords(pathToInputFile, saveFile):
    # read each line in the file
    with open(pathToInputFile) as iFile:
        # split data in file into an array
        text = iFile.read()
        text = text.translate(str.maketrans('', '', string.punctuation)) 
        newWords = []
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
            
            return newWords

def generateCsv(translator, newWords, ankiFile):
    newWordTranslations = []
    
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
        raise Exception("No new words to translate")


def main():
    try:
        # get input file
        pathToInputFile = sys.argv[1]
        language = sys.argv[2]
        fileExtension = os.path.splitext(pathToInputFile)[1]
        ankiFile = f"./anki_{uuid.uuid4()}.csv"
        saveFile = "./save.txt"

        performChecks(pathToInputFile, fileExtension)
            
        newWords = extractWords(pathToInputFile, saveFile)

        # translate elements
        translator = Translator(to_lang=language)
                    
        generateCsv(translator, newWords, ankiFile)
    except IndexError:
        print("Provide all arguments e.g. <input-file> <target-language-code>")
        return -1
    except Exception as err:
        print(f"{err}")
        return -1


if __name__ == "__main__":
    main()
