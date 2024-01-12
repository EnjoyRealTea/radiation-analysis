# ============================================== Case Study 03 =========================================================
# =============================== Physics Experiment - Radiation Exposure Analysis =====================================
# *********************************************** E. Thompson **********************************************************
from statistics import stdev


def collect_data(location_name, current_data):
    # Function to take user's input and add it to the existing data dictionary.
    if current_data.get(location_name) is None:
        user_list = []
    else:
        user_list = current_data.get(location_name)

    while True:
        try:
            reading = int(input("Please enter a reading (enter 0 to stop) : "))
        except ValueError:
            print("Error: Invalid entry.")
            continue
        if reading == 0:
            break
        else:
            user_list.append(reading)

    current_data[location_name] = user_list
    return current_data


def show_results(data_dictionary):
    # Function to return average and standard deviation for each location.
    for key, data_list in data_dictionary.items():
        average = sum(data_list) / len(data_list)
        if len(data_list) > 1:
            st_dev = round(stdev(data_list), 2)
        else:
            st_dev = "Requires more than 1 reading"
        print(f"{key} Average Radiation Level: {round(average,2)}")
        print(f"{key} Standard Deviation: {st_dev}")


locations = ["Forest", "Urban", "Rural"]
data_collected = {}

# Gives the user a choice of locations to enter data for, or the option to finish:
while True:
    number_options = len(locations) + 1
    print("Which location are you entering radiation levels for?")
    for i, location in enumerate(locations, start=1):
        print(f"{i}  {location}")
    print(f"{number_options}  Finish collection and see results.")
    try:
        user_choice = int(input(f"Please enter your selection (1 to {number_options}): "))
    except ValueError:
        print("Error: Input must be a digit.")
        continue

    if user_choice == number_options:
        # The user has chosen to finish the data collection and see the results
        show_results(data_collected)
        break
    elif 0 < user_choice < number_options:
        # Allows the user to enter data for the selected location:
        data_collected = collect_data(locations[user_choice-1], data_collected)
        # print(data_collected)
    else:
        print(f"Error: Please enter a number between 1 and {number_options}")
