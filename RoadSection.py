from RoadElement import RoadElement


class RoadSection:
    name = ""
    length = 0
    similarity = 0

    def __init__(self):
        self.roadElements = []

    def load(self, name, roadElements):
        self.roadElements = []
        self.name = name
        self.roadElements = roadElements
        self.length = len(self.roadElements) * 10

    def loadFromFile(self, name, fileName):
        self.name = name
        self.roadElements = []
        file = open(fileName, 'r')
        lines = file.readlines()
        x1 = 0
        x1_wgs = 0
        x2 = 0
        x2_wgs = 0
        y1 = 0
        y1_wgs = 0
        y2 = 0
        y2_wgs = 0
        z1 = 0
        z2 = 0
        for line in lines:
            s = line.split(';')
            if x1 == 0:
                x1 = s[0]
                y1 = s[1]
                z1 = s[2]
                x1_wgs = s[3]
                y1_wgs = s[4]
                z1_wgs = s[5]
            else:
                x2 = s[0]
                y2 = s[1]
                z2 = s[2]
                x2_wgs = s[3]
                y2_wgs = s[4]
                z2_wgs = s[5]
                self.roadElements.append(RoadElement(x1, x1_wgs, x2, x2_wgs, y1, y1_wgs, y2, y2_wgs, z1, z1_wgs, z2, z2_wgs))
                self.length = self.length + 1
                x1 = x2
                x1_wgs = x2_wgs
                y1 = y2
                y1_wgs = y2_wgs
                z1 = z2
                z1_wgs = z2_wgs

    def printRoadSectionToConsole(self):
        for roadElement in self.roadElements:
            print(str(roadElement.x1) + ";" + str(roadElement.x2) + ";" + str(roadElement.y1) + ";" + str(roadElement.y2) + ";" + str(roadElement.z1) + ";" + str(roadElement.z2) + ";" + str(roadElement.xArea) + ";" + str(roadElement.yArea) + ";" + str(roadElement.zArea) + ";" + str(roadElement.xyArea))

    def printRoadSectionToGraph2D(self):
        x = []
        y = []

        for roadElement in self.roadElements:
            x.append(roadElement.x1)
            y.append(roadElement.y1)

        plt.plot(x,y)
        plt.show()

    def createGPXFile(self):
        file = open(self.name + ".gpx", 'w')
        file.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\r\n")
        file.write("<gpx creator=\"JH\" version=\"1.1\" xmlns=\"http://www.topografix.com/GPX/1/1\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd\">\r\n")
        file.write("<trk>\r\n")
        file.write("<name>" + self.name + "</name>\r\n")
        file.write("<trkseg>\r\n")
        for item in self.roadElements:
            file.write("<trkpt lat=\"" + str(item.x2_wgs) + "\" lon=\"" + str(item.y2_wgs) +"\">\r\n")
            file.write("<ele>" + str(item.z2_wgs) + "</ele>\r\n")
            file.write("</trkpt>\r\n")
        file.write("</trkseg>\r\n")
        file.write("</trk>\r\n")
        file.write("</gpx>\r\n")
