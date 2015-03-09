from math import pi , acos , sin , cos
#
def calcd(y1,x1, y2,x2):
   #
   y1  = float(y1)
   x1  = float(x1)
   y2  = float(y2)
   x2  = float(x2)
   #
   R   = 3958.76 # miles
   #
   y1 *= pi/180.0
   x1 *= pi/180.0
   y2 *= pi/180.0
   x2 *= pi/180.0
   #
   # approximate great circle distance with law of cosines
   #
   return acos( sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R

def findD(p):
   dTrav = 0;
   while parent[p] != None:
      dad = parent[p]
      (y1, x1) = pos[dad];
      (y2, x2) = pos[p];
      dBet = calcd(y1, x1, y2, x2);
      dTrav += dBet;
      p = dad;
   return dTrav;

start = input('Starting station: ')
finish = input('Destination: ')

names = {};
fNames = open('romFullNames.txt', 'r');
for line in fNames:
   z = line.strip('\n');
   names[z] = z[0];
fNames.close();
print(' ');
start = names[start];
finish = names[finish];


edges = {};

fEdges = open('romEdges.txt', 'r');
for line in fEdges:
   (x, y, z) = line.partition(' ');
   z = z.strip('\n')
   edges[x] = [];
   edges[z] = [];
fEdges.close();

fEdges = open('romEdges.txt', 'r');
for line in fEdges:
   (x, y, z) = line.partition(' ');
   z = z.strip('\n')
   edges[x].append(z)
   edges[z].append(x);
fEdges.close()

pos = {};

fDist = open('romNodes.txt', 'r');
for line in fDist:
   (x, y, z) = line.partition(' ');
   (z1, z2, z3) = z.partition(' ');
   z3 = z3.strip('\n');
   pos[x] = (z1, z3);
fDist.close();

pq = [];
pq.append((0, start));
parent = {};
parent[start] = None;
now = (0, 0)
visited = [];
count = 0;
while now[1] != finish:
   pq.sort();
   now = pq.pop(0);
   count += 1;
   for val in edges[now[1]]:
      if val == finish:
         do = False;
         for find in pq:
            if find[1] == finish:
               do = True;
               temp = parent[finish];
               parent[finish] = now[1];
               new = findD(val)
               parent[finish] = temp;
               old = findD(val)
               if new < old:
                  pq.append((new, val));
                  parent[finish] = now[1];
         if do == False:
            parent[val] = now[1];
            pq.append((findD(val), val));
      elif val not in visited:
         parent[val] = now[1];
         (y1, x1) = pos[finish];
         (y2, x2) = pos[val];
         (y3, x3) = pos[start];
         pq.append(((findD(val)+0), val));
         visited.append(val)
   visited.append(now[1])


# path = []
# path.append(finish)
# no = finish
# while parent[no] != None:
#    path.append(parent[no])
#    no = parent[no]
# path.reverse()
print("distance", now[0]);
print("pops: ", count)
