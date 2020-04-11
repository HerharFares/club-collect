from config import REPLACE_ITEMS
import csv

def replacing(string):
    """To convert the name of the universities from 
    French to English.
    """
    for temp in REPLACE_ITEMS:
        string = string.replace(temp[0], temp[1])
    return string


def csv_writer(file_name, row, data):
    """This functoin writes data into csv file,
    by speciying the rows head titles, and the data to put.
    """
    csvfile = open(file_name,"w")  # the csv file
    csvwriter = csv.writer(csvfile, delimiter=',', quotechar='|',
                           quoting=csv.QUOTE_MINIMAL)

    # writing desciption row
    csvwriter.writerow(row)

    # writing the data
    for item in data:
        csvwriter.writerow(item)
    
    # close the file
    csvfile.close()