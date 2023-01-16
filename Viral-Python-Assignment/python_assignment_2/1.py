"""Create a function to read csv file and convert to python data structure (dict, list, set)
first_name, last_name,roll
John,Ken,11
Ronny,Baggs,12
Sam,Shone,13
"""

with open("text.csv","w") as file:
  file.writelines(['First_name,Last_name,roll\n','John,Ken,11\n','Ronny,Baggs,12\n','Sam,Shone,13\n'])

import csv
def csv_to_list_of_dicts(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    return data

data = csv_to_list_of_dicts('text.csv')
print(data)
