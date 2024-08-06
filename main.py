import json
import csv

# Read json to a list of address strings.
data = json.load(open("data.json"))
results = data["results"]
locations = []
for result in results:
    locations.append(
        {
            "address": result["address"].lower(),
            "lat": result["lat"],
            "long": result["lon"],
        }
    )

# Check if the string can be split into two by a comma.
valid_addresses = {}
invalid_addresses = []
for loc in locations:
    address = loc["address"]
    lat = loc["lat"]
    long = loc["long"]
    parts = address.split(", ")
    if len(parts) == 2:
        city = parts[0]
        country = parts[1]
        city_info = {
            "city": city,
            "lat": lat,
            "long": long,
        }
        # Group by country.
        if country in valid_addresses:
            valid_addresses[country].append(city_info)
        else:
            valid_addresses[country] = [city_info]
    else:
        invalid_addresses.append(loc)

# Save "city, country" pair to a CSV file
with open("city_country.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["City", "Country", "Lat", "Long"])
    for country in valid_addresses:
        for city_info in valid_addresses[country]:
            writer.writerow(
                [city_info["city"], country, city_info["lat"], city_info["long"]]
            )

# Save country to another CSV file.
with open("country.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Country"])
    for country in valid_addresses:
        writer.writerow([country])

# Print valid data.
print("Saved the following to CSV:")
for country in valid_addresses:
    for city_info in valid_addresses[country]:
        print(
            f"{city_info['city']}, {country}, {city_info['lat']}, {city_info['long']}"
        )

# Print excluded data.
print("Excluded the following data:")
for item in invalid_addresses:
    print(item)
