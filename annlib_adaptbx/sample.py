import math,os,StringIO
from annlib_ext import AnnAdaptor
from scitbx.array_family import flex
from libtbx.utils import hashlib_md5

import libtbx.load_env
dist_dir = libtbx.env.dist_path("annlib_adaptbx")
tests = os.path.join(dist_dir,"tests")

def data_from_files():
  data = flex.double()
  query = flex.double()

  D = open(os.path.join(tests,"data.txt"))
  for line in D.xreadlines():  # x & y coordinates of reference set
    point = line.strip().split(" ")
    data.append(float(point[0]))
    data.append(float(point[1]))

  Q = open(os.path.join(tests,"query.txt"))
  for line in Q.xreadlines():  # x & y coordinates of query set
    point = line.strip().split(" ")
    query.append(float(point[0]))
    query.append(float(point[1]))

  return data,query

def excercise_nearest_neighbor():

  data,query = data_from_files()
  S = StringIO.StringIO()

  A = AnnAdaptor(data,2)       # construct k-d tree for reference set
  A.query(query)               # find nearest neighbors of query points

  for i in xrange(len(A.nn)):
    print >>S,"Neighbor of (%7.1f,%7.1f), index %6d distance %4.1f"%(
    query[2*i],query[2*i+1],A.nn[i],math.sqrt(A.distances[i]))

  return S.getvalue()

def gethash(longstring):
  m = hashlib_md5()
  m.update(longstring)
  return "".join(["%02X"%ord(i) for i in m.digest()])

def check_memory():
  data,query = data_from_files()
  for x in xrange(1000):
    AnnAdaptor(data,2).query(query)

if __name__=="__main__":
  assert gethash(
    excercise_nearest_neighbor() ) == 'E486456DC3A225C40FE8A3A9D9A760E9'
  #check_memory()
  print "OK"
