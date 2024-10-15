import json
import math
import statistics

# Open and read the JSON file
with open('datasets/counties.json', 'r') as file:
    data = json.load(file)

# Markdown heading/start

with open('report.md' , 'a') as h:
    h.write("# DS-1043 Lab 6 Report  ")
    h.write("\n")
    h.write("## Shaun Worthen  ")
    h.write("\n")


def make_weather_list():
    """Goes through counties.json and makes a list of lists.
    Each list inside contains the county name, state, weather variance
    and individual month data. Ignores counties without all
    four months of data."""

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
        except KeyError:
            continue

        temp_months = [temp_jan, temp_apr, temp_jul, temp_oct]
        temp_var = statistics.pvariance(temp_months)

        county_weather_list = [temp_name, temp_state, temp_var, temp_jan, temp_apr, temp_jul, temp_oct]
        all_counties_weather.append(county_weather_list)

    all_counties_weather = sorted(all_counties_weather, key=lambda x: x[2])
    return all_counties_weather


def make_weather_table():

    weather_info = make_weather_list()
    row_string = ''
    with open('report.md' , 'a') as w:

        w.write("\n")
        w.write("#### Most Stable Weather  ")
        w.write("\n")
        w.write("| County Name | State | Weather Variance | Temp Jan | Temp Apr | Temp July | Temp Oct |   ")
        w.write("\n")
        w.write("| --- | --- | --- | -------- | --- | --- | --- |  ")
        w.write("\n")

        for item in weather_info:
            for i in item:
                row_string = row_string + ' | ' + str(i)
            row_string += '  '
            w.write(row_string)
            w.write('\n')
            row_string = ''

        w.write("\n")

            # row_string.append(' || ' .join(map(str, item[info])) + ' |\n')


make_weather_table()

# data.close()

# Print the data
# print(data)
