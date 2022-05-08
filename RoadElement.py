class RoadElement:
    x1 = 0
    x1_wgs = 0
    x2 = 0
    x2_wgs = 0
    y1 = 0
    y1_wgs = 0
    y2 = 0
    y2_wgs = 0
    z1 = 0
    z1_wgs = 0
    z2 = 0
    z2_wgs = 0
    xArea = 0
    yArea = 0
    zArea = 0
    xyArea = 0
    length = 10

    def __init__(self, x1, x1_wgs,x2, x2_wgs, y1, y1_wgs, y2, y2_wgs, z1, z1_wgs, z2, z2_wgs):
        self.x1 = float(x1)
        self.x1_wgs = float(x1_wgs)
        self.x2 = float(x2)
        self.x2_wgs = float(x2_wgs)
        self.y1 = float(y1)
        self.y1_wgs = float(y1_wgs)
        self.y2 = float(y2)
        self.y2_wgs = float(y2_wgs)
        self.z1 = float(z1)
        self.z1_wgs = float(z1_wgs)
        self.z2 = float(z2)
        self.z2_wgs = float(z2_wgs)
        self.xArea = abs(abs(float(x2)) - abs(float(x1)))
        self.yArea = abs(abs(float(y2)) - abs(float(y1)))
        self.zArea = abs(abs(float(z2)) - abs(float(z1)))
        self.xyArea = self.xArea + self.yArea

