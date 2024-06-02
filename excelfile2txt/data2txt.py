
# simply importing panda repo
import pandas as pd

# this is how you get to read the CSV file
df = pd.read_csv('jrizo013.csv') # random csv file I had to use for one class were I had to do a similar yet way more complex assignment

# here we are separating users based on their gender so we can call them as groups later
male_users = []
female_users = []
other_users = []

for index, row in df.iterrows(): # This collect ALL data meaning, username - directions as it's an info dump. 
    user = {                     # you can opt out and just do important stuff.
        'username': row['username'],
        'first_name': row['first_name'],
        'last_name': row['last_name'],
        'gender': row['gender'],
        'dob': row['dob'],
        'olympics': row['olympics'],
        'computers': row['computers'],
        'f1': row['f1'],
        'hex_color': str(row['hex_color']),  # converting this into a string just in case
        'cities': row['cities'],
        'channels': row['channels'],
        'directions': row['directions']
    }
    user_str = f"{user['username']},{user['first_name']},{user['last_name']},{user['gender']},{user['dob']},{user['olympics']},{user['computers']},{user['f1']},{user['hex_color']},{user['cities']},{user['channels']},{user['directions']}"
    if user['gender'] == 'm': # putting the users in groups if gender has M then it goes into male group | if F goes into female group
        male_users.append(user_str)
    elif user['gender'] == 'f':
        female_users.append(user_str)
    else:
        other_users.append(user_str)

# writing users to the txt file starting with males
with open('usergenders.txt', 'w') as f:
    f.write("Male users:\n")
    for user_str in male_users:
        f.write(user_str + '\n') # \n for proper spacing though it collects ALL of the data

    f.write("\nFemale users:\n")
    for user_str in female_users:
        f.write(user_str + '\n')

    f.write("\nOther users:\n")
    for user_str in other_users:
        f.write(user_str + '\n')

# End
