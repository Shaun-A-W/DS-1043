import json
import math
import statistics

# Open and read the JSON file
with open('datasets/counties.json', 'r') as file:
    data = json.load(file)

# Read and print according to string
# for i in data['name']:
# print(i)



def weather_most_stable():
    """Goes through the counties.json data file. Finds set of jan,apr,jul,oct
    temperature data from each data and finds the set of least variance.
    If counties do not have all four month temperature readings, they are
    skipped over and not considered."""

    most_stable = None
    month_temps = []
    most_stable_name = ''
    weather_dict = {}

    for i in data:

        try:
            temp_jan = i['noaa']['temp-jan']
            month_temps.append(temp_jan)
        except KeyError:
            pass

        try:
            temp_apr = i['noaa']['temp-apr']
            month_temps.append(temp_apr)
        except KeyError:
            pass

        try:
            temp_jul = i['noaa']['temp-jul']
            month_temps.append(temp_jul)
        except KeyError:
            pass

        try:
            temp_oct = i['noaa']['temp-oct']
            month_temps.append(temp_oct)
        except KeyError:
            pass

        if len(month_temps) < 4:
            month_temps.clear()
            continue

        temp_var = statistics.variance(month_temps)

        if most_stable is None or temp_var < most_stable:
            most_stable = temp_var
            most_stable_name = i['name'] + ', ' + i['state']

        month_temps.clear()


    top_stability = most_stable_name, ' has the most stable weather with a variance of ', most_stable
    print(top_stability)

data.close()

# Print the data
# print(data)
