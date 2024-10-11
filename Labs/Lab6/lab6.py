import json
import math
import statistics

# Open and read the JSON file
with open('datasets/counties.json', 'r') as file:
    data = json.load(file)

# Read and print according to string
# for i in data['name']:
# print(i)


county_list = []
weather_list = []
month_temps = []
most_stable = None
most_stable_name = ''

for i in data:
    # county_list.append(i['name'])

    try:
        temp_jan = i['noaa']['temp-jan']
        month_temps.append(temp_jan)
    except KeyError:
        temp_jan = None

    try:
        temp_apr = i['noaa']['temp-apr']
        month_temps.append(temp_apr)
    except KeyError:
        temp_apr = None

    try:
        temp_jul = i['noaa']['temp-jul']
        month_temps.append(temp_jul)
    except KeyError:
        temp_jul = None

    try:
        temp_oct = i['noaa']['temp-oct']
        month_temps.append(temp_oct)
    except KeyError:
        temp_oct = None

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

#
#     for temp in month_temps:
#         if temp is not None:
#             weather_list.append(temp)
#         elif temp is None:
#             pass
#
#     print(month_temps)
#     print(weather_list)
#     temp_count = len(weather_list)
#
#     if temp_count < 4:
#         weather_list.clear()
#         month_temps.clear()
#         continue
#     # if temp_count == 1:
#     #     temp_var = 0
#     #     continue
#
#     temp_var = statistics.variance(weather_list)
#     print(temp_var)
#
#     if temp_var < most_stable:
#         most_stable = temp_var
#         most_stable_name = i['name']
#
#     print(most_stable)
#     print(most_stable_name)
#
#     month_temps = []
#     weather_list = []
#
# top_stability = most_stable_name, ' has the most stable weather with a variance of ', most_stable


data.close()

# Print the data
# print(data)
