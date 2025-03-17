# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

conversion = {"M": 1000000, "B": 1000000000}

from collections import Counter, defaultdict

def update_damages(damages):
    return [float(i[:-1])*conversion['M'] if i[-1] == 'M'
            else float(i[:-1])*conversion['B'] if i[-1] == 'B'
            else i for i in damages]

updated_damages = update_damages(damages)

def hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    return {names[i]:
        {"Name": names[i],
        "Month": months[i],
        "Year": years[i],
        "Max Sustained Wind": max_sustained_winds[i],
        "Areas Affected": areas_affected[i],
        "Damage": damages[i],
        "Deaths": deaths[i]} for i in range(len(names))}

old = hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
new = {v['Year'] : v for v in old.values()}

def affected_areas(old_dict):
    affected_areas = []
    for v in old_dict.values():
        affected_areas.extend(v['Areas Affected'])
    return Counter(affected_areas)

affected = affected_areas(old)

def hurricane_with_highest_mortality(old):
    maxval = max(deaths)
    for key in old:
        if old[key]['Deaths'] == maxval:
            return key, maxval

target_key, target_value = hurricane_with_highest_mortality(old)

def hurricanes_by_mortality(old):
    hurricanes_by_mortality_dictionary = defaultdict(list)
    death_ranges = {
                    0: range(0),
                    1: range(1, 101),
                    2: range(101, 501),
                    3: range(501, 1001),
                    4: range(1001, 10001),
                    5: range(10001, max(deaths)+1)
                    }
    for key, value in old.items():
        check_value = value["Deaths"]
        for k in death_ranges:
            if check_value in death_ranges[k]:
                hurricanes_by_mortality_dictionary[k] += [{key: value}]
    return hurricanes_by_mortality_dictionary

def greatest_damage_and_cost(old):
    updated_damages_recorded = [i for i in updated_damages if type(i) == float]
    max_value = max(updated_damages_recorded)
    for key in old:
        if old[key]["Damage"] == max_value:
            return key, max_value

hurricane, greatest_damage = greatest_damage_and_cost(old)

def hurricanes_by_damage_rating(old):
    hurricanes_by_damage_rating_dictionary = defaultdict(list)
    damage_ranges = {
                    0: range(0, 10**8),
                    1: range(10**8, 10**9),
                    2: range(10**9, 10**10),
                    3: range(10**10, 5*10**10)
                    }
    for key, value in old.items():
        value_to_check = value["Damage"]
        try:
            value_to_check = int(value_to_check)
            for k in damage_ranges:
                if value_to_check in damage_ranges[k]:
                    hurricanes_by_damage_rating_dictionary[k] += [{key: value}]
        except ValueError:
            continue
    return hurricanes_by_damage_rating_dictionary

print(updated_damages)
print(old)
print(new)
print(affected)
print(f"The most affected area due to hurricanes is {affected.most_common(1)[0][0]}.")
print(f"The greatest number of deaths is caused by Hurricane {target_key}, and it caused {target_value} deaths.")
print(hurricanes_by_mortality(old))
print(f"Hurricane {hurricane} caused the greatest damage with a cost of {greatest_damage}$")
print(hurricanes_by_damage_rating(old))