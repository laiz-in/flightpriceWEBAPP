from datetime import datetime

# Get the departure date from the user
date_dep= '2023-04-26'
date_dep = datetime.strptime(date_dep, '%Y-%m-%d')

# Calculate the number of days left until the departure date
date_dep = datetime.strptime(date_dep, '%Y-%m-%d')
days_left = ((date_dep - datetime.now()).days)+1

# Display the result
print("Days left until your flight:", days_left)
