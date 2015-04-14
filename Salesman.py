"""     +==========================+========-========*========-========+==========================+
        ||                           DEVELOPING ALGORITHMS ON YOUR OWN                           ||
        ||                           (THE TRAVELING SALESMAN PROBLEM)                            ||
        ||                                 by Student name  (Date)                               ||
        ||                                                                                       ||
        || Description. Given a set of 2-D points (cities), we seek the SHORTEST PATH (and its   ||
        ||              LENGTH) connecting them. The salesman's path must return home to the     ||
        ||              first city--i.e., we seek a so-called "closed walk" aka a "circuit", aka ||
        ||              a "Hamiltonian cycle". This version of the problem has every city        ||
        ||              connected directly to every other city. The terms "cities and routes"    ||
        ||              are often replaced by "nodes and links", and "vertices and edges". The   ||
        ||              word "traveling" is sometimes spelled "travelling".                      ||
        ||                                                                                       ||
        || Algorithms.  Various algorithms must be invented by the students.                     ||
        || Data.        Download the file tsp.txt of ordered pairs from the school's ai site.    ||
        || Course.      Artificial intelligence                                                  ||
        || Language.    Python Ver. x.x                                                          ||
        || Graphics.    Tkinter package Ver. x.x                                                 ||
        || References.  William J. Cook, In Pursuit of the Traveling Salesman (Princeton, 2012). ||
        ||              Internet site http://www.math.uwaterloo.ca/tsp/index.html.               ||
        +==========================+========-========*========-========+==========================+

                             Problem solving in AI is fundamentally a search.
                             --M. Tim Jones, Artificial Intelligence (Infinity
                             Science Press, 2008), page 21.

PROGRAMMING NOTES.
   1. Short of brute force (finding all paths) there is no known optimal algorithm for the traveling salesman
      problem (aka TSP), for a set of random points of any size. So we seek an algorithm that 1) is quick to
      run, and 2) will give us a short path length, but not necessarily the shortest.

   2. How do we find such an algorithm? Or, again, what do we do when we don't know what to do? We make up
      examples and think about the examples. We try to recall or invent similar kinds of problems--e.g., in-
      stead of the most efficient solution, find the most inefficient solution. Programming a poor idea may
      give us a good idea for another algorithm. BTW, it is extremely important that you display any path you
      create visually on the screen in order to gain new ideas.

   3. If a path crosses itself, the length can be shortened.     A   B                   A---B
      This immediately follows from the Triangle Inequality       \ /|                       |
      Theorem. You can prove this freshman geometry                / |                       |
      problem, can't you? [The truth is that this took me         / \|                       |
      a couple minutes of frustration until I realized           D   C                   D---C
      that the solution was "obvious".]                    poor path = ACBD     shorter path = ABCD
      --------------------------------------------------------------------------------------------------------

HISTORY. The first reference in the mathematical literature is a colloquium talk in 1930, when the Austrian
   mathematician Karl Menger discussed the "messenger problem", which is the same as the TSP, except the
   messenger, who visits every city, does not need to return home. Although the problem was known in the
   mathematics community, no progress was made for nearly 20 years. The first mention of the name "traveling
   salesman problem" comes from a 1949 paper by the mathematician Julia Robinson. In 1954, the optimal
   solution for a particular 49-city problem was solved. It was a route from Washington D.C through major
   cities in each of the 48 states returning to D.C. Skipping ahead, through many minor successes with this
   problem, in 2006, the problem was solved in general for 85,900 random points.
   -----------------------------------------------------------------------------------------------------------

ADVICE.
   1. The data in your program will be a list of xy-coordinates. Make it a list of lists, not tuples. And
      append an id in the zeroth position--e.g.,

              city = [[id, x, y], [id, x, y], ..., [id, x, y]]

      Then x, y = city[n][1], city[n][2]. Why a make list of lists instead of a list of tuples? Because you
      don't know if you will later need to modify the components, and tuples are immutable. Why append an id?
      Because you don't know if you will later need to give your xy-coordinates an attribute.

   2. Recall the 2-D distance function is built-in in Python: hypot(3,4) = 5. Since we are working with city
      points, create a dist function that will accept two cities--NOT xy-coordinates--and return their
      distance. Since my city points look like this: city[n] = [id, x, y], I wrote this function:

                            def dist(cityA, cityB):
                                return hypot(cityA[1]-cityB[1], cityA[2]-cityB[2])

   3. Here is a KEY DESIGN OBSERVATION. We are working with cities, which are at least a pair of xy-coordin-
      ates, and in my case a city is a triple: city[n] = [id, x, y]. Consequently, we want to write functions
      (create tools) that accept city parameters, NOT xy-coordinates. This policy will tend to keep us away
      from nested subscripts (ouch!) and triply subscripted variables (ouch, again!). The dist function above
      is an example of the policy.

   4. The data for this problem consists of all float numbers. It may be an advantage to cast them all as
      integers, until the program is finished. Why? Because 1) ints line up easier for inspection during
      debugging, 2.) it is easier to tell-by-looking if two ints differ than two floats, and 3) you cannot
      directly compare floats for equality.

   5. Finally, watch for two particular errors: OBOEs (off-by-one errors), and aliases (two variables sharing
      the same place in memory). When in doubt, use deepcopy.
   -----------------------------------------------------------------------------------------------------------

THE MOORE PRINCIPLE (R.L. Moore, 1882-1974). You must neither obtain ideas from others, nor check the Internet
   when solving problems. Only after you have programmed up your own ideas do you seek out what others have
   done. (Questions of syntax are excepted.) The advantages of following this principle are multiple:

                   1. We mature as problem solvers.
                   2. We appreciate the clever ideas of others.
                   3. We remember ideas that can be used in future problems.
                   4. We become more confident in ourselves.

   THE FIRST RULE OF PROBLEM SOLVING is--in my opinion--to come to each problem with a history of working out
   challenging problems on your own. You cannot quit on pesky problems or you won't have that history. You
   cannot stop working on problems or you won't have enough of that history. Lucky is the obsessed person, who
   isn't working at all, only playing. Good luck.
   -----------------------------------------------------------------------------------------------------------

ASSIGNMENT.  Code up the following algorithms and print their four lengths in a visually attractive chart.

   Algorithm 1. (Random) Call Python's shuffle instruction to randomize the order of the cities in the list.
                Then create a path by connecting the cities in the order they occur in the file. Don't forget
                to connect the final city back to the initial city.

                [This will be a terrible solution, don't you think? A waste of time, too. Argg! Don't be so
                quick to judge. This "solution" has the obvious advantages of being fast and easy to code. It
                also gets us moving on the problem--both thinking and coding, especially working with
                graphics. It begs the question: could there be a worse solution?  Yes. Can we find it? Yes,
                but why? Because the opposite of a poor solution might be a good solution. So we have learned
                another lesson. Initially coding up a poor algorithm can be a productive way to start
                searching for a good algorithm.]

   Algorithm 2. (Sort on x) Sort the tuples and then connect them in the order they occur in the re-ordered
                city list. Remember to connect the last city with the first city. Look closely at the image.
                Can you think of a way to shorten the total length?

   Algorithm 3. (Sort on y) Isn't this essentially the same as sorting on x? Yes, but we wonder if the path
                lengths are significantly different. The trick, of course, is just to switch the x- and y-
                values and then call the exact same functions to display the graph.

   Algorithm 4. Your algorithm. There are many ways to attack this problem. Don't worry about finding an
                efficient method, because we are interested in why some methods that sound good are not good
                at all.

   The program given below should work and display the shuffled data. The rest is up to you
   ========================================================================================================
"""





##############################################<START OF PROGRAM>##############################################
def setUpCanvas(root): # These are the REQUIRED magic lines to enter graphics mode.
    root.title("THE TRAVELING SALESMAN PROBLEM by (your name here).")
    canvas = Canvas(root, width  = root.winfo_screenwidth(), height = root.winfo_screenheight(), bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    return canvas
#---------------------------------------------------------------------------------Traveling Salesman Problem--

def script(x, y, msg = '', kolor = 'WHITE'):
    canvas.create_text(x, y, text = msg, fill = kolor,  font = ('Helvetica', 10, 'bold'))
#---------------------------------------------------------------------------------Traveling Salesman Problem-

def plot(city): # Plots 5x5 "points" on video screen
    x = city[1]+5; y = city[2]+5 # The +5 is to push away from the side bars.
    if city[0] == -1:
        kolor = 'WHITE'
    else: kolor = 'YELLOW'
    canvas.create_rectangle(x-2, y-2, x+2, y+2, width = 1, fill = kolor)
#---------------------------------------------------------------------------------Traveling Salesman Problem--

def line(city1, city2, kolor = 'RED'):
    canvas.create_line(city1[1]+5, city1[2]+5, city2[1]+5, city2[2]+5, width = 1, fill = kolor)
#---------------------------------------------------------------------------------Traveling Salesman Problem--

def displayDataInConsole(AlgorithmResults, baseCity, city):
    print('===<Traveling Salesman Path Statistics>===')
    print ('   algorithm         path length ')
    for element in AlgorithmResults:
           print ('---%-20s'%element[0], int(element[2]))
    city.sort()
    baseCity.sort()
    if city == baseCity:
        print("---Data verified as unchanged.")
    else:
        print ('ERROR: City data has been corrupted!')
    print('   Run time =', round(clock()-START_TIME, 2), ' seconds.')
#---------------------------------------------------------------------------------Traveling Salesman Problem--

def printCity(city): # Used for debugging.
    count = 0
    for (id,x,y) in city:
        print( '%3d: id =%2d, (%5d, %5d)'%(count,id, int(x), int(y)))
        count += 1
#---------------------------------------------------------------------------------Traveling Salesman Problem--

def displayPathOnScreen(city, statistics):
#=---Normalize data
    (minX, maxX, minY, maxY, meanX, meanY, medianX, medianY, size, m, b) = statistics
    canvas.delete('all')
    cityNorm, (p,q,r,s) = normalizeCityDataToFitScreen(city[:], statistics)

#---Plot points and lines
    cityNorm.append(cityNorm[0])
    plot(cityNorm[0])
    for n in range(1, len(cityNorm)):
        plot(cityNorm[n])
        line(cityNorm[n], cityNorm[n-1])
    script(650,  20, 'path length = ' + str(pathLength(city)))
    canvas.create_rectangle(530,10, 770, 30, width = 1, outline = 'WHITE')
    canvas.update()
    root.mainloop() # Required for graphics.
#---------------------------------------------------------------------------------Traveling Salesman Problem--

def normalizeCityDataToFitScreen(city, statistics):
    """ Coordinates are all assumed to be non-negative."""
    (minX, maxX, minY, maxY, meanX, meanY, medianX, medianY, size, m, b) = statistics
    newCity = []

#---Step 1a. Shift city points to the x- and y-axes.
    for (id, x,y) in city:
        newCity.append ( (id, x-minX, y-minY))

#---Step 1b. Shift line-of-best-fit to the x- and y-axes.
    (x0,y0) = (maxX-minX, m*maxX+b - minY) # = x-intercept of line-of-best-fit.
    (x1,y1) = (minX-minX, m*minX+b - minY) # = y-intercept of line-of-best-fit.


#---Step 1c. Shift max-values to x- and y-axes.
    maxX = maxX-minX
    maxY = maxY-minY

#---Step 2a. # Re-scale city points to fit the screen.
    cityNorm = []
    for (id, x, y) in newCity:
        cityNorm.append ((id, x*SCREEN_WIDTH/maxX, y*SCREEN_HEIGHT/maxY))

#---Step 2b. # Re-scale the x-axis and y-axis intercepts for the line-of-best-fit.
    (x0,y0) = x0/maxX*SCREEN_WIDTH, y0/maxY*SCREEN_HEIGHT # a point on the x-axis
    (x1,y1) = x1/maxX*SCREEN_WIDTH, y1/maxY*SCREEN_HEIGHT # a point on the y-axis

    return cityNorm, (x1,y1,x0,y0) # = the adjusted city xy-values and 2 points on the line-of-best-fit.
#---------------------------------------------------------------------------------Traveling Salesman Problem--

def readDataFromFileAndAppendId(fileName):
    file1 = open(fileName, 'r')
    fileLength = int(file1.readline()) # removes heading
    city = []
    for elt in range(fileLength):
       x, y = file1.readline().split()
       city.append( [0, float(x), float(y)] ) # A place for an id (0, here) is appended.
    file1.close()
    return city
#---------------------------------------------------------------------------------Traveling Salesman Problem--

def pathLength(city):
    totalPath = 0
    for n in range(1, len(city)):
        totalPath += dist( city[n-1], city[n] )
    totalPath += dist( city[n], city[0] )
    return int(totalPath)
#---------------------------------------------------------------------------------Traveling Salesman Problem--

def dataStatistics(city):
    xValues = []
    yValues = []
    size = len(city)
    for (id, x,y) in city:
        xValues.append(x)
        yValues.append(y)
    minX = min(xValues)
    maxX = max(xValues)
    minY = min(yValues)
    maxY = max(yValues)

    assert (minX >= 0 or maxX >= 0 or minY >= 0 or maxY >= 0)

    meanX = sum(xValues)/size
    meanY = sum(yValues)/size
    medianX = city[len(city)//2][0]
    medianY = city[len(city)//2][1]

#---Derive the line of best fit: y = mx+b
    xyDiff   = 0
    xDiffSqr = 0
    for (id, x,y) in city:
        xyDiff  += (meanX - x)*(meanY - y)
        xDiffSqr+= (meanX - x)**2

    m = xyDiff/xDiffSqr
    b = meanY - m*meanX

    return minX, maxX, minY, maxY, meanX, meanY, medianX, medianY, size, m, b
#---------------------------------------------------------------------------------Traveling Salesman Problem--

def dist(cityA, cityB):
    return hypot(cityA[1]-cityB[1], cityA[2] - cityB[2])
#====================================<GLOBAL CONSTANTS and GLOBAL IMPORTS>========Traveling Salesman Problem==

from tkinter   import Tk, Canvas, YES, BOTH
from operator  import itemgetter
from itertools import permutations
from copy import deepcopy
from random    import shuffle
from time      import clock
from math      import hypot
root           = Tk()
canvas         = setUpCanvas(root)
START_TIME     = clock()
SCREEN_WIDTH   = root.winfo_screenwidth() //5*5 - 15 # adjusted to exclude task bars on my PC.
SCREEN_HEIGHT  = root.winfo_screenheight()//5*5 - 90 # adjusted to exclude task bars on my PC.
fileName       = "tsp0734.txt" # My file name will be different from yours
#==================================================< MAIN >=======================Traveling Salesman Problem==

def main():
#---0. Read in data, append an id to every pair, and store results in a variable called "city".
    city  = readDataFromFileAndAppendId(fileName)

#---1. Extract statistics.
    statistics = (minX, maxX, minY, maxY, meanX, meanY, medianX, medianY, size, m, b) = dataStatistics(city)

#---2. Create a random path.
    shuffle(city)

#---3. Sort on y-coordinate and connect sequentially by y.

#---4. Sort on x-coordinate and connect sequentially by x.

#---5. Your algorithm(s). Can you do better than the sorting algorithms above?

#---6. Display results.
    displayPathOnScreen(city, statistics)
#---------------------------------------------------------------------------------Traveling Salesman Problem--
if __name__ == '__main__': main()
###############################################<END OF PROGRAM>###############################################
