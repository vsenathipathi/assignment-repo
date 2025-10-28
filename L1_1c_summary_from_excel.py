# Automate weekly reports by extracting specific data from excel files and generate summary report.
# Date : 24-10-2025
# Author : Venkat


# Read CSV
# Extract only Required columns
# Filter & SUmmary
# Automate Weekly SUmmaries

import pandas as pd
import schedule
import time
from datetime import datetime,timedelta

def extract_exit_data(filename):
    time_now= time.strftime('%Y-%m-%d-%H-%M-%S')
    try:
        df=pd.read_csv(filename,encoding='latin1')

    except FileNotFoundError:
        print('File Not found')
        return

    today=datetime.now().date()
    one_week_ago=today-timedelta(7)

    df['Exit Date']=pd.to_datetime(df['Exit Date'],errors='coerce')
    recent_exits=df[df['Exit Date'].dt.date.between(one_week_ago,today)]

    if recent_exits.empty:
        print("No employees have exited in last 7 days.")
    else:
        print(f"Summary Report as of {time_now}:")
        print(recent_exits.to_string(index=False))
        recent_exits.to_csv(f"weekly_exit_summary_{time_now}.csv", index=False)

# extract_exit_data('emp1.csv')
# schedule.every(1).minutes.do(extract_exit_data,'emp1.csv')
schedule.every().friday.at("09:00").do(extract_exit_data, 'emp1.csv')

while True:
    schedule.run_pending()
    time.sleep(1)


# EEID,Full Name,Job Title,Department,Business Unit,Gender,Ethnicity,Age,Hire Date,Annual Salary,Bonus %,Country,City,Exit Date
# E02387,Emily Davis,Sr. Manger,IT,Research & Development,Female,Black,55,4/8/2016,"$141,604 ",15% ,United States,Seattle,10/16/2021