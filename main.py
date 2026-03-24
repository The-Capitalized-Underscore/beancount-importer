#import libraries & comparison dictionaries
import os
import csv
from datetime import datetime
import functions

#################################################
#Variables for working directory, filenames, etc.
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) #gets the active directory for this file, no matter where it's run from
import_directory = "data/imports/" #sub directory with all of the import files, should be inside the active directory
directory_path = os.path.join(BASE_DIR, import_directory) #joins BASE_DIR & import_directory, allowing for the import folder to have a custom name




def main():
    find_files = os.listdir(directory_path)
    for file in find_files:
        file_path = os.path.join(directory_path, file)

    print("main")

#open file & determine the account
    #csv reader, determiner
#clean the file based on account
    #column renamer/deleter, date reformater
#printout/inputs based on account


if __name__ == "__main__":
    main()
