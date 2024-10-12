import json
import math
import statistics
import markdown

# Open and read the JSON file
with open('datasets/counties.json', 'r') as file:
    data = json.load(file)

# Read and print according to string
# for i in data['name']:
# print(i)

def make_weather_list():
    """Goes through counties.json and makes a list of lists.
    Each list inside contains the county name, state, weather variance
    and individual month data."""

    all_counties_weather = []
    county_weather_list = []

    for d in data:
        try:
            temp_name = d['name']
            temp_state = d['state']
            temp_jan = d['noaa']['temp-jan']
            temp_apr = d['noaa']['temp-apr']
            temp_jul = d['noaa']['temp-jul']
            temp_oct = d['noaa']['temp-oct']
        except:
            continue

        temp_months = [temp_jan, temp_apr, temp_jul, temp_oct]
        temp_var = statistics.pvariance(temp_months)

        county_weather_list = [temp_name, temp_state, temp_var, temp_jan, temp_apr, temp_jul, temp_oct]
        all_counties_weather.append(county_weather_list)

    all_counties_weather = sorted(all_counties_weather, key=lambda x: x[2])

    print(all_counties_weather)

make_weather_list()

data.close()

# Print the data
# print(data)
