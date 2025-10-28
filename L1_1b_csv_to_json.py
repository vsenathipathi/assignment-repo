# Create a script to convert data from CSV file into a JSON file.
# Date : 24-10-2025
# Author : Venkat

import csv

with open('emp.csv', 'r', encoding='latin-1') as csv_obj:
    csvreader=csv.DictReader(csv_obj)
    records=[]
    for row in csvreader:
        records.append(row)
    print(type(records)) # list of dict

import json
with open('emp.json', 'w') as json_wf:
    file=json.dumps(records, indent=4)
    json_wf.write(file)
print("JSON file created successfully.")
print(type(file)) # str

with open('emp.json', 'r') as json_rf:
    data=json.loads(json_rf.read())
    print(data)
    print(type(data))


# WORKS BUT ISSUE when a field contains comma within quotes
# import json
# with open('emp.csv', 'r', encoding='latin-1') as file:
#     lines_as_list=file.readlines()
#     column_value=lines_as_list[0]
#     column_values_as_list=column_value.strip().split(',')
#     # print(column_values_as_list)

#     records=[]
#     for lines in lines_as_list[1::]:

#         values_as_list=lines.strip().split(',')
#         # for i in range(len(values_as_list)):
#         #     values_as_list[i]=values_as_list[i].strip()
#         zipped=zip(column_values_as_list, values_as_list)
#         # records.update(dict(zipped))
#         new_dict=dict(zipped)
#         records.append(new_dict)
        

#     # print(records)
#     print(type(records))
#     json_file=json.dumps(records, indent=4)
#     print(json_file)
#     print(type(json_file))
#     with open('emp.json', 'w') as jsonf:
#         jsonf.write(json_file)
#     print("JSON file created successfully.")
#     with open('emp.json', 'r') as jsonf:
#         data=json.load(jsonf)
#         print(data)


