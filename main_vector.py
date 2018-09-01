import sys
import numpy
import scipy

from playLA.Vector import Vector

if __name__ == "__main__":

    print(sys.version)
    print(numpy.__version__)
    print(scipy.__version__)

    vec = Vector([1, 3])
    print(vec)
    print("len(vec) = {}".format(len(vec)))
    print("vec[0] = {}, vec(1) = {}".format(vec[0], vec[1]))

    vec1 = Vector([2, 3])
    print("vec + vec1 = {}".format(vec + vec1))
    print("vec - vec1 = {}".format(vec + vec1))
