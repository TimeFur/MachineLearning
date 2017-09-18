import os, sys

os.sys.path.append("./Agent/")
from kmeans import *
from knn import *
from sklearn import tree

'''----------------------
    Global variable
----------------------'''
sample = array( [[1,2],
                  [5,7],
                  [1,21],
                  [41,32],
                  [21,2],
                  [0,8]])
target = array(["A",
                "B",
                "A",
                "B",
                "B",
                "A"])
test = array([6,9])
k = 3

def main():

    #Kmeans
    kmeans_machine = kmeans(sample, k)
    kmeans_machine.train()

    #KNN
    knn_machine = knn(test, sample, target, k)
    print knn_machine.train()
    
if __name__ == "__main__":
    main()
    
