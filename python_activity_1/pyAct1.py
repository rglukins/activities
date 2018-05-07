import os
import csv

cereal_csv_path = os.path.join(".", "Resources", "cereal.csv")

with open(cereal_csv_path, newline = "") as csvfile:
    csv_reader = csv.reader (csvfile, delimiter =",")
    for row in csv_reader:
        if(float(row[7]) >= 5):
            print(row)
    
    

