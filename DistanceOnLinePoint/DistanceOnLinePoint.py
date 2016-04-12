`

import math

class Point:
     """A simple class that represents a point
     """

     def __init__(self, x, y):
         self.x = x
         self.y = y

     def __repr__(self):
         return "("+repr(self.x)+","+repr(self.y)+")"


class Line:
    """A simple class representing a line
    """

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self): 
         return "p1:"+repr(self.p1)+"->"+"p2:"+repr(self.p2)


    def getPointAtDistance(self, d):
    
        vx = self.p2.x - self.p1.x
        vy = self.p2.y - self.p1.y

        mag = math.sqrt(vx*vx+vy*vy)

        vx = float(vx / mag);
        vy = float(vy / mag);

        x = self.p1.x + vx * d;
        y = self.p1.y + vy * d;

        p = Point(x,y)

        return p;

    def getDistance(self, p1, p2):
        vx = p2.x - p1.x
        vy = p2.y - p1.y

        d = float(math.sqrt(vx*vx+vy*vy))
        
        return d;


start = Point(2,1)
end = Point(5,9)

l  = Line(start,end)

d = 3
p = l.getPointAtDistance(d)
v = l.getDistance(start,p)

print "line: "+ repr(l)+ "distance: "+ repr(d)+ " point: "+ repr(p) + " verify distance: "+repr(v)

start = Point(5,1)
end = Point(2,9)

l  = Line(start,end)

d = 3
p = l.getPointAtDistance(d)
v = l.getDistance(start,p)

print "line: "+ repr(l)+ "distance: "+ repr(d)+ " point: "+ repr(p) + " verify distance: "+repr(v)

start = Point(5,9)
end = Point(2,1)

l  = Line(start,end)

d = 3
p = l.getPointAtDistance(d)
v = l.getDistance(start,p)

print "line: "+ repr(l)+ "distance: "+ repr(d)+ " point: "+ repr(p) + " verify distance: "+repr(v)


