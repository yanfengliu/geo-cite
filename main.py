import json
import csv


data = json.load(open("data.json"))
pubs = data["results"]
locations = []
for pub in pubs:
    locations += [pub["address"]]

valid_locs = {}
invalid_locs = []
for loc in locations:
    parts = loc.split(", ")
    if len(parts) == 2:
        city = parts[0]
        country = parts[1]
        if country in valid_locs:
            valid_locs[country].append(city)
        else:
            valid_locs[country] = [city]
    else:
        invalid_locs.append(loc)

with open("city_country.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["City", "Country"])
    for country in valid_locs:
        for city in valid_locs[country]:
            writer.writerow([city, country])

with open("country.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Country"])
    for country in valid_locs:
        writer.writerow([country])

print("Saved the following (city, country) to CSV:")
for item in valid_locs:
    print(item)

print("Excluded the following data:")
for item in invalid_locs:
    print(item)
