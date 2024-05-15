from rdflib import Graph
from datetime import datetime


current_datetime = datetime.now()
print("Time before parsing: ", current_datetime)

g = Graph()
g.parse("C:/data/MeSH/mesh2024.nt")

current_datetime = datetime.now()
print("Time after parsing: ", current_datetime)


current_datetime = datetime.now()
print("Time before calculating graph length: ", current_datetime)

print("The MeSH terminology in turtle format has a length of ", len(g))

current_datetime = datetime.now()
print("Time after calculating graph length: ", current_datetime)