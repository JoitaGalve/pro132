import csv
import plotly.express as px

rows = []

with open("stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        rows.append(row)

headers = rows[0]
stars_data_rows = rows[1:]

print(headers)
print(stars_data_rows[0])

headers[0] = "row_num"
solar_system_stars_count = {}
for stars_data in stars_data_rows:
    if solar_system_stars_count.get(stars_data[2]):
        solar_system_stars_count[stars_data[2]] += 1

    else:
        solar_system_stars_count[stars_data[2]] = 1

max_solar_system = max(solar_system_stars_count, key = solar_system_stars_count.get)

print("Solar system {} has maximum stars {} out of the solar system we have discovered so far".format(max_solar_system, solar_system_stars_count[max_solar_system]))

sun_star = []

for stars_data in stars_data_rows:
    if max_solar_system == stars_data[2]:
        sun_star.append(stars_data)

#print(len(KOI_351_planet))
#print(KOI_351_planet)
sun_star_masses = []
sun_star_names = []

for planet_data in sun_star:
    sun_star_masses.append(stars_data[4])
    sun_star_names.append(stars_data[1])

sun_star_masses.append(1)
sun_star_names.append("Sun")

fig = px.bar(x = sun_star_names, y = sun_star_masses)
fig.show()

temp_data_rows = list(stars_data_rows)
print(temp_data_rows[0])

for planet_data in temp_data_rows:
    planet_mass = planet_data[3]
    
    if planet_mass.lower() == "unknown":
        stars_data_rows.remove(planet_data)
        
        continue
    else:
        planet_mass_value = planet_mass.split(' ')[0]
        planet_mass_ref = planet_mass.split(' ')[1]

        if planet_mass_ref == "Jupiters":
            planet_mass_value = float(planet_mass_value) * 317.8
            planet_data[3] = planet_mass_value
            planet_radius = planet_data[7]

            if planet_radius.lower() == "unknown":
                stars_data_rows.remove(planet_data)

                continue
            else:
                planet_radius_value = planet_radius.split()[0]
                planet_radius_ref = planet_radius.split()[2]

                if planet_radius_ref == "Jupiter":
                  planet_radius_value = float(planet_radius_value) * 11.2
                  planet_data[7] = planet_radius_value

