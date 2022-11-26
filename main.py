from RoadSection import RoadSection
from RoadBank import RoadBank
b = 1

rs = RoadSection()
rs.loadFromFile("kuba", "kuba.txt")
#rovinka = RoadSection()
#rovinka.loadFromFile("test_rovinka", "test_rovinka.txt")
zatacka = RoadSection()
zatacka.loadFromFile("test_zatacka", "test_zatacka.txt")

roadSections = []
roadSections.append(rs)
rb = RoadBank(roadSections)
pom = rb.findSameAndPrintBasedOnXYArea(zatacka, 95)
rs.printRoadSectionToConsole()
zatacka.createGPXFile()
for item in pom:
    item.createGPXFile()



