
class Walker:
    """Walker is a class that implements a recursive algorithm that uses 
       sumdigits to determine if a coordinate is valid and can be visited.
       The constructor can pass a total sum value but the problem
       called for running with value 19, meaning that the sum of
       each digits abs() couldnt exceed 19.
       A few optimizations were implemented:
       1. if x,y is valid then y,x is valid
       2. if x,y is valid then all other coordinates for that
       value are valid
    """

    bDebug = False;

    def __init__(self, sumval):
        self.visited = []
        self.actual = 0;
        self.sumval = sumval
 
    def sumdigits(self, x, y):
        value = 0
        x = abs(x)
        y = abs(y)
        while True:
            value = value + x % 10
            x = x / 10
            if x < 1:
               if value > self.sumval: 
                   return False
               break 

        while True:
            value = value + y % 10
            y = y / 10
            if y < 1:
               if value > self.sumval: 
                   return False
               break 
        return True

    def traversed(self, x, y):
        result = [point for point in self.visited if point[0] == x and point[1] == y]
        if not result:
            return False
        else:
            return True

    def traverse(self, x, y):
        if self.bDebug:
            print "traversing ("+repr(x)+","+repr(y)+")"
            
        '''actual visited locations'''
        self.actual += 1    

        if self.traversed(x, y):
            return 

        ''' optimization, we know that if x,y is valid so is y,x 
            and also variants of x and y negative and positive '''
        self.visited += [(x,y)]
        self.visited += [(y,x)]

        self.visited += [(-x,y)]
        self.visited += [(y,-x)]

        self.visited += [(x,-y)]
        self.visited += [(-y,x)]

        self.visited += [(-x,-y)]
        self.visited += [(-y,-x)]


        ''' only need to visit quadrant x positive, y positive  '''
        if self.sumdigits(x+1, y):
            self.traverse(x+1, y)
        if self.sumdigits(x, y+1):
            self.traverse(x, y+1)

        return

    def total(self):
        return len(self.visited)

summation = 19

walker = Walker(summation);
walker.traverse(0,0)
print "summation value: "+ repr(summation)+ " total valid locaiton: "+ repr(walker.total())+ " actual visits: "+ repr(walker.actual)
