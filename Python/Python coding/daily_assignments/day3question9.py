# Use the Datetime Module:
# Write a program that imports the datetime module and uses it to:
# Get and print the current date and time .

import datetime
from calendar import different_locale

current_datetime = datetime.datetime.now()
print(current_datetime)
# Calculate and print the number of days between two dates.
date1=datetime.date(2026,4,25)
date2=datetime.date(2026,6,29)
difference = date1-date2
print(f'difference between date1 and date2 is{difference}')

# 3. Format and print the current date in "DD-MM-YYYY"
formatted_date = current_datetime.strftime("%d-%m-%Y")
print("Formatted Current Date:", formatted_date)