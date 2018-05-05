# PyBoss Challenge

import os
import csv
import datetime

# Import the employee_data1.csv and employee_data2.csv files


new_employee_data = []
def pyBoss(filepath):
    # Read data within file
    with open(filepath) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            emp_id = row["Emp ID"]
            name = row["Name"]
            dob = row["DOB"]
            ssn = row["SSN"]
            state = row["State"]
        
        # split name into first and last name
            first_name = name.split()[0]
            last_name = name.split()[1]
        
        # DOB reformat to MM/DD/YYYY
            dob_mdy = datetime.datetime.strptime(dob, '%Y-%m-%d').strftime('%m/%d/%y')

            # ssn masking
            ssn_mask = ssn[-4:].rjust(len(ssn), "*")

            # create dictionary to take into consideration states and abbreviation
            us_state_abbrev = {
                'Alabama': 'AL',
                'Alaska': 'AK',
                'Arizona': 'AZ',
                'Arkansas': 'AR',
                'California': 'CA',
                'Colorado': 'CO',
                'Connecticut': 'CT',
                'Delaware': 'DE',
                'Florida': 'FL',
                'Georgia': 'GA',
                'Hawaii': 'HI',
                'Idaho': 'ID',
                'Illinois': 'IL',
                'Indiana': 'IN',
                'Iowa': 'IA',
                'Kansas': 'KS',
                'Kentucky': 'KY',
                'Louisiana': 'LA',
                'Maine': 'ME',
                'Maryland': 'MD',
                'Massachusetts': 'MA',
                'Michigan': 'MI',
                'Minnesota': 'MN',
                'Mississippi': 'MS',
                'Missouri': 'MO',
                'Montana': 'MT',
                'Nebraska': 'NE',
                'Nevada': 'NV',
                'New Hampshire': 'NH',
                'New Jersey': 'NJ',
                'New Mexico': 'NM',
                'New York': 'NY',
                'North Carolina': 'NC',
                'North Dakota': 'ND',
                'Ohio': 'OH',
                'Oklahoma': 'OK',
                'Oregon': 'OR',
                'Pennsylvania': 'PA',
                'Rhode Island': 'RI',
                'South Carolina': 'SC',
                'South Dakota': 'SD',
                'Tennessee': 'TN',
                'Texas': 'TX',
                'Utah': 'UT',
                'Vermont': 'VT',
                'Virginia': 'VA',
                'Washington': 'WA',
                'West Virginia': 'WV',
                'Wisconsin': 'WI',
                'Wyoming': 'WY',
            }    

            # two-letter state abbreviation.
            state_abbrev = [us_state_abbrev[state]]

            # Append data to the converted_employee_data fields
            new_employee_data.append(
                    {
                        "emp_id": emp_id,
                        "first_name": first_name,
                        "last_name" : last_name,
                        "dob_mdy": dob_mdy,
                        "ssn_mask": ssn_mask,
                        "us_state_abbrev": state_abbrev   
                    }
            )


            # Grab filename from the original path
            _, filename = os.path.split(filepath)  

            # Write updated data to csv file
            csvpath = os.path.join("output", filename)
            with open(csvpath, "w") as csvfile:
                fieldnames = ["emp_id", "first_name", "last_name", "dob_mdy", "ssn_mask", "us_state_abbrev"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(new_employee_data)

filepath = os.path.join("employee_data1.csv")
filepath2 = os.path.join("employee_data2.csv")

pyBoss(filepath)
pyBoss(filepath2)