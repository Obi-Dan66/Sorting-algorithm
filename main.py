import csv
import sys
import os

users_database = 'user_database.csv' # Define the name of the users database file
two_fa ='twofactor_authentication_enabled' # Define the column name for the two-factor authentication column

# Define a function to filter users based on utilization
def utilization_rule(user):
    utilization = float(user['worked_hours_on_project_per_month']) / float(user['worked_hours_per_moth'])
    return utilization < 0.5

# Define a function to check if two-factor authentication is disabled
def two_factor_disabled(user):
    return user[two_fa] == 'False'

# Define the main function
def main():
    # Get the command-line arguments
    try:
        action = sys.argv[1]
        rule = sys.argv[2]
    except IndexError:
        print('Missing argument(s). Usage: python main.py <True/False> <utilization/2fa>')
        return

    # Check if the command-line arguments are valid
    if action not in ('True', 'False') or rule not in ('utilization', '2fa'):
        print('Invalid argument(s). Usage: python main.py <True/False> <utilization/2fa>')
        return

    # Check if the users database file exists
    if not os.path.isfile(users_database):
        print(f"File {users_database} does not exist.")
        sys.exit()

      # Read the users database into a list of dictionaries
    with open(users_database) as user_db:
        reader = csv.DictReader(user_db)
        users = [user for user in reader]

        # Remove users based on the selected rule
        if action == 'True':
            # Filter out users based on rule
            if rule == 'utilization':
                filtered_users = []
                for user in users:
                    if utilization_rule(user):
                        filtered_users.append(user)
                output = f'Users with utilization more than 50% removed from {os.path.abspath(users_database)}'

            elif rule == '2fa':
                filtered_users = []
                for user in users:
                    if two_factor_disabled(user):
                        filtered_users.append(user)
                output = f'Users with two factor authentication enabled removed from {os.path.abspath(users_database)}'

            # Write the filtered users to the users database file
            with open(users_database, 'w', newline='') as user_db:
                writer = csv.DictWriter(user_db, fieldnames=reader.fieldnames)
                writer.writeheader()
                writer.writerows(filtered_users)

            print(output)
        else:
            # Print the names of users based on rule
            if rule == 'utilization':
                print('Users with utilization less than 50%: ')
                for user in users:
                    if utilization_rule(user):
                        print(user['emp_name'])

            elif rule == '2fa':
                filtered_users = []
                for user in users:
                    if two_factor_disabled(user):
                        filtered_users.append(user)
                print('Users with two factor authentication disabled: ')
                for user in filtered_users:
                    print(user['emp_name'])
if __name__ == '__main__':
    main()