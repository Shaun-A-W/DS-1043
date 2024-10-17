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

# ON/OFF SWITCH FOR FULL REPORT FUNCTION.
# ALL 15 TABLES. LOCATED AT BOTTOM OF FILE.
# True = ON. False = OFF.
full = True


# Data List formation & Associated Tables Below
# Denoted with comments at top and bottom of topics


##\\ WEATHER DATA //##

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
        temp_var = round(statistics.pvariance(temp_months), 3)

        county_weather_list = [temp_name, temp_state, temp_var, temp_jan, temp_apr, temp_jul, temp_oct]
        all_counties_weather.append(county_weather_list)

    return all_counties_weather

def most_stable_table():

    weather_most = sorted(make_weather_list(), key=lambda x: x[2])
    truncated_most = weather_most[0:5]

    row_string = ''
    with open('report.md' , 'a') as w:

        w.write("\n")
        w.write("#### Most Stable Weather  ")
        w.write("\n")
        w.write("| County Name | State | Weather Variance | Temp Jan | Temp Apr | Temp July | Temp Oct |   ")
        w.write("\n")
        w.write("| --- | --- | --- | --- | --- | --- | --- |  ")
        w.write("\n")

        for item in truncated_most:
            for i in item:
                row_string = row_string + ' | ' + str(i)
            row_string += '  '
            w.write(row_string)
            w.write('\n')
            row_string = ''

        w.write("\n")

def least_stable_table():

    weather_least = sorted(make_weather_list(), key=lambda x: x[2], reverse=True)
    truncated_least = weather_least[0:5]


    row_string = ''
    with open('report.md', 'a') as w:

        w.write("\n")
        w.write("#### Least Stable Weather  ")
        w.write("\n")
        w.write("| County Name | State | Weather Variance | Temp Jan | Temp Apr | Temp July | Temp Oct |   ")
        w.write("\n")
        w.write("| --- | --- | --- | --- | --- | --- | --- |  ")
        w.write("\n")

        for item in truncated_least:
            for i in item:
                row_string = row_string + ' | ' + str(i)
            row_string += '  '
            w.write(row_string)
            w.write('\n')
            row_string = ''

        w.write("\n")

##// END WEATHER DATA \\##



##\\ GROWTH DATA //##

def make_growth_list():

    all_counties_growth = []
    county_growth_list = []

    for d in data:
        try:
            growth_name = d['name']
            growth_state = d['state']
            year1 = d['population']['2010']
            year2 = d['population']['2019']
        except KeyError:
            continue

        growth_rate = round((year2 - year1) / year1, 5)
        county_growth_list = [growth_name, growth_state, growth_rate, year1, year2]
        all_counties_growth.append(county_growth_list)

    return all_counties_growth

def most_growth_table():

    growth_most = sorted(make_growth_list(), key=lambda x: x[2], reverse=True)
    truncated_most = growth_most[0:5]

    row_string = ''
    with open('report.md', 'a') as w:

        w.write("\n")
        w.write("#### Highest Growth Counties ")
        w.write("\n")
        w.write("| County Name | State | Growth Rate | 2010 Pop | 2019 Pop |  ")
        w.write("\n")
        w.write("| --- | --- | --- | --- | --- |  ")
        w.write("\n")

        for item in truncated_most:
            for i in item:
                row_string = row_string + ' | ' + str(i)
            row_string += '  '
            w.write(row_string)
            w.write('\n')
            row_string = ''

        w.write("\n")

def least_growth_table():

    growth_least = sorted(make_growth_list(), key=lambda x: x[2])
    truncated_least = growth_least[0:5]

    row_string = ''
    with open('report.md', 'a') as w:

        w.write("\n")
        w.write("#### Lowest Growth Counties ")
        w.write("\n")
        w.write("| County Name | State | Growth Rate | 2010 Pop | 2019 Pop |  ")
        w.write("\n")
        w.write("| --- | --- | --- | --- | --- |  ")
        w.write("\n")

        for item in truncated_least:
            for i in item:
                row_string = row_string + ' | ' + str(i)
            row_string += '  '
            w.write(row_string)
            w.write('\n')
            row_string = ''

        w.write("\n")

##// END GROWTH DATA \\##



##\\ DEATH DATA //##

def make_death_list():

    all_counties_death = []
    county_death_list = []

    for d in data:
        try:
            death_name = d['name']
            death_state = d['state']
            suicide = d['deaths']['suicides']
            firearm_suicide = d['deaths']['firearm suicides']
            homicide = d['deaths']['homicides']
            vehicle = d['deaths']['vehicle']
        except KeyError:
            continue

        if suicide is None:
            continue
        else: suicide = round(suicide, 3)
        if firearm_suicide is None:
            continue
        else: firearm_suicide = round(firearm_suicide, 3)
        if homicide is None:
            continue
        else: homicide = round(homicide, 3)
        if vehicle is None:
            continue
        else: vehicle = round(vehicle, 3)

        death_capita = round(suicide + firearm_suicide + homicide + vehicle, 3)
        county_death_list = [death_name, death_state, death_capita, suicide, firearm_suicide, homicide, vehicle]
        all_counties_death.append(county_death_list)

    return all_counties_death

def most_death_table():

    death_most = sorted(make_death_list(), key=lambda x: x[2], reverse=True)
    truncated_most = death_most[0:5]

    row_string = ''
    with open('report.md', 'a') as w:

        w.write("\n")
        w.write("#### Deadliest Counties ")
        w.write("\n")
        w.write("| County Name | State | Total Deaths/Cap | Suicides/Cap | Gun Suicide/Cap | Homicide/Cap | Vehicle/Cap |  ")
        w.write("\n")
        w.write("| --- | --- | --- | --- | --- | --- | --- |  ")
        w.write("\n")

        for item in truncated_most:
            for i in item:
                row_string = row_string + ' | ' + str(i)
            row_string += '  '
            w.write(row_string)
            w.write('\n')
            row_string = ''

        w.write("\n")

def least_death_table():

    death_least = sorted(make_death_list(), key=lambda x: x[2])
    truncated_least = death_least[0:5]

    row_string = ''
    with open('report.md', 'a') as w:

        w.write("\n")
        w.write("#### Safest Counties ")
        w.write("\n")
        w.write("| County Name | State | Total Deaths/Cap | Suicides/Cap | Gun Suicide/Cap | Homicide/Cap | Vehicle/Cap |  ")
        w.write("\n")
        w.write("| --- | --- | --- | --- | --- | --- | --- |  ")
        w.write("\n")

        for item in truncated_least:
            for i in item:
                row_string = row_string + ' | ' + str(i)
            row_string += '  '
            w.write(row_string)
            w.write('\n')
            row_string = ''

        w.write("\n")

##// END DEATHS DATA \\##



##\\ EDUCATION DATA //##

def make_educated_list():

    all_counties_educated = []
    county_educated_list = []

    for d in data:
        try:
            educated_name = d['name']
            educated_state = d['state']
            less_hs = d['edu']['less-than-high-school']
            high_school = d['edu']['high-school']
            some_college = d['edu']['some-college']
            degrees = d['edu']['bachelors+']
        except KeyError:
            continue

        county_educated_list = [educated_name, educated_state, degrees, less_hs, high_school, some_college]
        all_counties_educated.append(county_educated_list)

    return all_counties_educated

def most_educated_table():

    educated_most = sorted(make_educated_list(), key=lambda x: x[2], reverse=True)
    truncated_most = educated_most[0:5]

    row_string = ''
    with open('report.md', 'a') as w:

        w.write("\n")
        w.write("#### Most Educated Counties ")
        w.write("\n")
        w.write("| County Name | State | College Graduate Rate | Less than HS | HS Diploma | Some College Time |  ")
        w.write("\n")
        w.write("| --- | --- | --- | --- | --- | --- |  ")
        w.write("\n")

        for item in truncated_most:
            for i in item:
                row_string = row_string + ' | ' + str(i)
            row_string += '  '
            w.write(row_string)
            w.write('\n')
            row_string = ''

        w.write("\n")

def least_educated_table():

    educated_least = sorted(make_educated_list(), key=lambda x: x[2])
    truncated_least = educated_least[0:5]

    row_string = ''
    with open('report.md', 'a') as w:

        w.write("\n")
        w.write("#### Least Educated Counties ")
        w.write("\n")
        w.write("| County Name | State | College Graduate Rate | Less than HS | HS Diploma | Some College Time |  ")
        w.write("\n")
        w.write("| --- | --- | --- | --- | --- | --- |  ")
        w.write("\n")

        for item in truncated_least:
            for i in item:
                row_string = row_string + ' | ' + str(i)
            row_string += '  '
            w.write(row_string)
            w.write('\n')
            row_string = ''

        w.write("\n")

##// END EDUCATION DATA \\##



##\\ GENDER DATA //##

def make_gender_list():
    all_counties_gender = []
    county_gender_list = []

    for d in data:
        try:
            gender_name = d['name']
            gender_state = d['state']
            male = d['male']
            female = d['female']
        except KeyError:
            continue

        total_gender = male + female
        male_prop = round(male / total_gender, 3)
        female_prop = round(female / total_gender, 3)
        county_gender_list = [gender_name, gender_state, male_prop, female_prop, male, female, total_gender]
        all_counties_gender.append(county_gender_list)

    return all_counties_gender

def most_male_table():

    most_male = sorted(make_gender_list(), key=lambda x: x[2], reverse=True)
    truncated_most = most_male[0:5]

    row_string = ''
    with open('report.md', 'a') as w:

        w.write("\n")
        w.write("#### Most Male Skewed Counties ")
        w.write("\n")
        w.write("| County Name | State | Male % | Female % | Male Total | Female Total | Overall Total |  ")
        w.write("\n")
        w.write("| --- | --- | --- | --- | --- | --- | --- |  ")
        w.write("\n")

        for item in truncated_most:
            for i in item:
                row_string = row_string + ' | ' + str(i)
            row_string += '  '
            w.write(row_string)
            w.write('\n')
            row_string = ''

        w.write("\n")

def most_female_table():

    most_female = sorted(make_gender_list(), key=lambda x: x[2])
    truncated_most = most_female[0:5]

    row_string = ''
    with open('report.md', 'a') as w:

        w.write("\n")
        w.write("#### Most Female Skewed Counties ")
        w.write("\n")
        w.write("| County Name | State | Male % | Female % | Male Total | Female Total | Overall Total |  ")
        w.write("\n")
        w.write("| --- | --- | --- | --- | --- | --- | --- |  ")
        w.write("\n")

        for item in truncated_most:
            for i in item:
                row_string = row_string + ' | ' + str(i)
            row_string += '  '
            w.write(row_string)
            w.write('\n')
            row_string = ''

        w.write("\n")

##// END GENDERS DATA \\##


##\\ AGE DATA //##

def make_age_list():

    all_counties_age = []
    county_age_list = []

    for d in data:
        try:
            age_name = d['name']
            age_state = d['state']
            young = round(d['age']['0-4'] + d['age']['5-9'] + d['age']['10-14'] + d['age']['15-19'], 5)
            old = round(d['age']['65-69'] + d['age']['70-74'] + d['age']['80-84'] + d['age']['85+'], 5)
        except KeyError:
            continue


        county_age_list = [age_name, age_state, young, old]
        all_counties_age.append(county_age_list)

    return all_counties_age

def make_old_table():

    oldest = sorted(make_age_list(), key=lambda x: x[3], reverse=True)
    truncated_most = oldest[0:5]

    row_string = ''
    with open('report.md', 'a') as w:

        w.write("\n")
        w.write("#### Old Population Counties ")
        w.write("\n")
        w.write("| County Name | State | Under 20yo % | Over 65yo % |  ")
        w.write("\n")
        w.write("| --- | --- | --- | --- |  ")
        w.write("\n")

        for item in truncated_most:
            for i in item:
                row_string = row_string + ' | ' + str(i)
            row_string += '  '
            w.write(row_string)
            w.write('\n')
            row_string = ''

        w.write("\n")

def make_young_table():

    youngest = sorted(make_age_list(), key=lambda x: x[2], reverse=True)
    truncated_most = youngest[0:5]

    row_string = ''
    with open('report.md', 'a') as w:

        w.write("\n")
        w.write("#### Young Population Counties ")
        w.write("\n")
        w.write("| County Name | State | Under 20yo % | Over 65yo % |  ")
        w.write("\n")
        w.write("| --- | --- | --- | --- |  ")
        w.write("\n")

        for item in truncated_most:
            for i in item:
                row_string = row_string + ' | ' + str(i)
            row_string += '  '
            w.write(row_string)
            w.write('\n')
            row_string = ''

        w.write("\n")

def age_variance_table():

    all_counties_age = []
    county_age_list = []

    for d in data:
        try:
            age_name = d['name']
            age_state = d['state']
            ages = d['age']
        except KeyError:
            continue

        age_groups = ages.values()
        age_var = round(statistics.pvariance(age_groups), 8)

        county_age_list = [age_name, age_state, age_var]
        all_counties_age.append(county_age_list)

    aged = sorted(all_counties_age, key=lambda x: x[2])
    truncated_most = aged[0:5]

    row_string = ''
    with open('report.md', 'a') as w:

        w.write("\n")
        w.write("#### Highest Age Diversity Counties ")
        w.write("\n")
        w.write("| County Name | State | Age Group Variance |  ")
        w.write("\n")
        w.write("| --- | --- | --- |  ")
        w.write("\n")

        for item in truncated_most:
            for i in item:
                row_string = row_string + ' | ' + str(i)
            row_string += '  '
            w.write(row_string)
            w.write('\n')
            row_string = ''

        w.write("\n")

##// END AGES DATA \\##


##\\ EMPLOYMENT DATA //##

def make_employ_list():
    all_counties_employ = []
    county_employ_list = []

    for d in data:
        try:
            employ_name = d['name']
            employ_state = d['state']
            labor = d['bls']['2020']['labor_force']
            employed = d['bls']['2020']['employed']
            unemployed = d['bls']['2020']['unemployed']
        except KeyError:
            continue

        employment = round(employed/labor, 5)
        unemployment = round(unemployed/labor, 5)

        county_employ_list = [employ_name, employ_state, employment, unemployment, labor]
        all_counties_employ.append(county_employ_list)

    return all_counties_employ

def most_employ_table():

    most_employ = sorted(make_employ_list(), key=lambda x: x[2], reverse=True)
    truncated_most = most_employ[0:5]

    row_string = ''
    with open('report.md', 'a') as w:

        w.write("\n")
        w.write("#### Highest Employment Counties ")
        w.write("\n")
        w.write("| County Name | State | Employment Rate | Unemployment Rate | Labor Force |  ")
        w.write("\n")
        w.write("| --- | --- | --- | --- | --- |  ")
        w.write("\n")

        for item in truncated_most:
            for i in item:
                row_string = row_string + ' | ' + str(i)
            row_string += '  '
            w.write(row_string)
            w.write('\n')
            row_string = ''

        w.write("\n")

def least_employ_table():
    most_employ = sorted(make_employ_list(), key=lambda x: x[3], reverse=True)
    truncated_most = most_employ[0:5]

    row_string = ''
    with open('report.md', 'a') as w:

        w.write("\n")
        w.write("#### Lowest Employment Counties ")
        w.write("\n")
        w.write("| County Name | State | Employment Rate | Unemployment Rate | Labor Force |  ")
        w.write("\n")
        w.write("| --- | --- | --- | --- | --- |  ")
        w.write("\n")

        for item in truncated_most:
            for i in item:
                row_string = row_string + ' | ' + str(i)
            row_string += '  '
            w.write(row_string)
            w.write('\n')
            row_string = ''

        w.write("\n")

##// END EMPLOYMENT DATA \\##


# calling all 15 table functions below
def full_report():
    most_stable_table()
    least_stable_table()
    most_growth_table()
    least_growth_table()
    most_death_table()
    least_death_table()
    most_educated_table()
    least_educated_table()
    most_male_table()
    most_female_table()
    make_old_table()
    make_young_table()
    age_variance_table()
    most_employ_table()
    least_employ_table()
# end
if full is True:
    full_report()