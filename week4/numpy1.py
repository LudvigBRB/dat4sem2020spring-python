import numpy as np
import matplotlib.pyplot as plt

with open ('befkbhalderstatkode.csv') as kbh: 
    dd = np.genfromtxt(kbh, delimiter=',', dtype=np.uint, skip_header=1)

neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave', 
       5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst', 
       10: 'Amager Vest', 99: 'Udenfor'}

#disse to funktioner udfører opgaven
def number_of_people_in_area(n, data):
    all_people_in_given_n = data[data[:,1] == n]
    sum_of_people = all_people_in_given_n[:,4 ].sum()
    return sum_of_people

allPeopleAreas = np.array([number_of_people_in_area(n, dd) for n in neighb.keys()])
#print(allPeopleAreas)

def area_and_number_people(dd, areas, funct):
    allPeopleAreas = np.array([funct(n, dd) for n in areas.keys()])
    allAreas = np.array([a for a in areas.values()])

    for x in range(len(allAreas)):
        print("Antal folk i", allAreas[x], "er", allPeopleAreas[x])
        print("\n")

#area_and_number_people(dd, neighb, number_of_people_in_area)

allAreas = np.array([neighb.values()])

import numpy as np
import matplotlib.pyplot as plt

neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave', 
       5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst', 
       10: 'Amager Vest', 99: 'Udenfor'}

def number_of_people_in_area(n, data):
    all_people_in_given_n = data[data[:,1] == n]
    sum_of_people = all_people_in_given_n[:,4 ].sum()
    return sum_of_people

allPeopleAreas = np.array([number_of_people_in_area(n, dd) for n in neighb.keys()])

allAreas = neighb.values()

plt.figure(figsize=(19,10))
plt.bar(allAreas, allPeopleAreas)

plt.bar(allAreas, allPeopleAreas)