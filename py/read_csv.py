import csv
import requests

file_path = '/media/rubel/SOFTWARE/Datasets/chemical/'
file_name = 'chemical_elements.csv'

base_url="http://localhost:8000/api/"
final_url="{0}{1}".format(base_url,'elements/')

with open(file_path+file_name, 'r') as file:
    reader = csv.DictReader(file,delimiter='\t')
    limit = 118
    current_row = 0
    payload = {}
    user = 'admin'
    password = 'admin'
    for row in reader:
        print(row)
        current_row +=1
        if limit >= current_row:
            #print(row['\ufeffAtomic Number'])
            payload = {
                'atomic_number': row['Atomic Number'],
                'name': row['Name'],
                'atomic_weight' :  row['Atomic weight'],
                'symbol' : row['Symbol'],
                'melting_point' : row['Melting Point (°C)'],
                'boiling_point' : row['Boiling Point (°C)'],
                'discovery_year' : row['Discovery(Year)'],
                'group' : row['Group*'],
                'period' : row['Period'],
                'electron_configuration': row['Electron configuration']
                }
            response = requests.post(final_url, data=payload, auth=(user, password))
            print(response.text) #TEXT/HTML
            print(response.status_code, response.reason) #HTTP

        else:
            break

