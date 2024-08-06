import json
import csv

# Read json to a list of address strings.
data = json.load(open("data.json"))
pubs = data["results"]
locations = []
for pub in pubs:
    locations += [pub["address"]]

# Check if the string can be split into two by a comma.
valid_locs = {}
invalid_locs = []
for loc in locations:
    parts = loc.split(", ")
    if len(parts) == 2:
        city = parts[0]
        country = parts[1]
        # Group by country.
        if country in valid_locs:
            valid_locs[country].append(city)
        else:
            valid_locs[country] = [city]
    else:
        invalid_locs.append(loc)

# Save "city, country" pair to a CSV file
with open("city_country.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["City", "Country"])
    for country in valid_locs:
        for city in valid_locs[country]:
            writer.writerow([city, country])

# Save country to another CSV file.
with open("country.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Country"])
    for country in valid_locs:
        writer.writerow([country])

# Print valid data.
print("Saved the following (city, country) to CSV:")
for country in valid_locs:
    for city in valid_locs[country]:
        print(f"{city}, {country}")

# Print excluded data.
print("Excluded the following data:")
for item in invalid_locs:
    print(item)
