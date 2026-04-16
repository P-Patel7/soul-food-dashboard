import csv
from pathlib import Path

RAW_DATA = Path("./data")
FORMATTED_DATA = "./formatted_data.csv"

with open(FORMATTED_DATA, mode='w', newline='') as dataOutput:
    outputWriter = csv.writer(dataOutput, delimiter=',')
    
    outputWriter.writerow(['sales', 'date', 'region'])

    for file_path in RAW_DATA.glob("*.csv"):

        with open(file_path, "r") as dataInput:
            inputReader = csv.reader(dataInput, delimiter=',')
            
            next(inputReader) 

            for row in inputReader:
                if row[0] == "pink morsel":
                    price = float(row[1].replace("$", ""))
                    sale = price * int(row[2])

                    outputWriter.writerow([sale, row[3], row[4]])