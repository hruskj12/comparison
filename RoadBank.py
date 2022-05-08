
from RoadSection import RoadSection

class RoadBank:
    roadSections = []
    index = 0

    def __init__(self, roadSections):
        self.roadSections = roadSections

    def findSameAndPrintBasedOnXYArea(self, template, percentage):
        toBeChecked = []
        result = []

        for roadSection in self.roadSections:
            if (roadSection.length * 10) >= template.length:
                toBeChecked.append(roadSection)
        same = True
        for roadSection in toBeChecked:
            #plt.plot(self.getXFromSection(roadSection, 0, roadSection.length), self.getYFromSection(roadSection, 0, roadSection.length))
            for i in range(roadSection.length - template.length + 1):
                for j in range(0, template.length):
                    comparisonPercentageXY = template.roadElements[j].xyArea * (percentage / 100)
                    comparisonPercentageZ = template.roadElements[j].zArea * (percentage)
                    if (abs(roadSection.roadElements[i+j].xyArea - template.roadElements[j].xyArea) > comparisonPercentageXY) \
                            or (abs(roadSection.roadElements[i+j].zArea - template.roadElements[j].zArea) > comparisonPercentageZ):
                        same = False
                if same:
                    #plt.plot(self.getXFromSection(roadSection, i, i + template.length), self.getYFromSection(roadSection, i, i + template.length))
                    self.index = self.index + 1
                    result.append(self.getSection(roadSection, i, i + template.length))
                same = True
        #plt.show()
        self.index = 0
        return result

    def calculateXYArea(self, roadSection, startIndex, endIndex):
        result = 0
        for i in range(startIndex, endIndex):
            result = result + roadSection.roadElements[i].xyArea
        return result

    def getXFromSection(self, roadSection, startIndex, endIndex):
        result = []
        for i in range(startIndex, endIndex):
            result.append(roadSection.roadElements[i].x1)
        return result

    def getYFromSection(self, roadSection, startIndex, endIndex):
        result = []
        for i in range(startIndex, endIndex):
            result.append(roadSection.roadElements[i].y1)
        return result

    def getSection(self, roadSection, startIndex, endIndex):
        pom = []
        for i in range(startIndex, endIndex):
            pom.append(roadSection.roadElements[i])
        result = RoadSection()
        result.load("shoda" + str(self.index), pom)
        return result
