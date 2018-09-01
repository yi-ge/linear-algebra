import sys
import numpy
import scipy

from playLA.Vector import Vector


if __name__ == "__main__":

    print(sys.version)
    print(numpy.__version__)
    print(scipy.__version__)

    vec = Vector([1, 3])
    print("vec = {}".format(vec))
    print("len(vec) = {}".format(len(vec)))
    print("vec[0] = {}, vec(1) = {}".format(vec[0], vec[1]))

    vec1 = Vector([2, 3])
    print("vec1 = {}".format(vec1))
    print("vec + vec1 = {}".format(vec + vec1))
    print("vec - vec1 = {}".format(vec - vec1))

    print("{} * {} = {}".format(vec, 2, vec * 2))
    print("{} * {} = {}".format(2, vec, 2 * vec))

    print("+{} = {}".format(vec, +vec))
    print("-{} = {}".format(vec, -vec))
