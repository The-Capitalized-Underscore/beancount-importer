import os
import csv
from datetime import datetime
import account_mapping

#creates a csvreader object, opens the .csv file, and appends each row to a list
def csv_reader(file_path):
    if os.path.exists(file_path): #if the file exists, continue
        print (f"----- Opening {file_path} -----")
        with open(file_path, newline='', encoding='utf-8-sig') as working_csvfile:
            csvreader = csv.DictReader(working_csvfile) #create csv reader
            file_tempdata = [] #store csv data in temp dictionary
            for row in csvreader:
                file_tempdata.append(row) #add the current row to the temp list

    else:
        print (f"Trying to open {file_path}... Does not exist")
###############################################################################

#format dates to one standardized format
def format_date(data, csv_field):
    change_date = data[csv_field]
    date_formats = ["%Y-%m-%d","%m/%d/%Y","%d-%m-%Y","%Y-%m-%d %H:%M:%S","%m/%d/%Y %I:%M:%S %p"]   
    for fmt in date_formats:
        try:
            date_obj = datetime.strptime(change_date, fmt)
            return date_obj.strftime("%Y/%m/%d")  # consistent output format
        except ValueError:
            continue  # try the next format
    # last-resort: strip time if present
    if " " in change_date:
        try:
            date_obj = datetime.strptime(change_date.split(" ")[0], "%Y-%m-%d")
            return date_obj.strftime("%Y/%m/%d")
        except ValueError:
            pass 
    # if none of the formats work, raise an error
    raise ValueError(f"Date '{change_date}' does not match any expected formats.")
###############################################################################

#rename column
def rename_column(entry, columns, new_column):
    reformat_data = []
    for col in columns:
        if col in entry:
            entry[new_column] = entry[col]
            del entry[col]
    return entry
###############################################################################





