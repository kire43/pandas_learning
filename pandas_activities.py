# Activity 1 - Create a dataframe to store information on the planets of the solar system.
# For each planet, record: Name, Avg. Temperature, Planet radius in KM, Planet colour, An interesting feature of the Planet.
import pandas as pd

planet_name = pd.Series(["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"])
avg_temperature = pd.Series(["167", "464", "15", "-65", "-110", "-140", "-195", "-200"])
planet_radius = pd.Series(["2439.5", "6052", "6378", "3396", "71492", "60268", "25559", "24764"])
planet_colour = pd.Series(["Grey", "Golden Brown", "Blue", "Red", "Yellow, Brown, Red", "Yellow, Brown, Grey", "Cyan", "Blue"])
planet_feature = pd.Series(["Shortest year at 88 days", "Rotates in the opposite direction to most planets", "Has Four layers: Inner Core, Outer Core, Mantle, Crust", "Ice caps grow and shrink with the seasons", "So large that 1300 Earths could fit inside the planet", "Only planet less dense than water", "Windiest planet in the solar system", "5 main rings and 14 known moons"])

df = pd.DataFrame({
    "Planet Name" : planet_name,
    "Average Temperature" : avg_temperature,
    "Radius" : planet_radius,
    "Colour" : planet_colour,
    "Feature" : planet_feature
})

print(df)
#---------------------------------
# Activity 2 - Research into turning an excel file and turn your planets frame into a spreadsheet.