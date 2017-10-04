import os, sys

os.sys.path.append("./Agent/")
from kmeans import *
from knn import *
from sklearn import tree
from sklearn import svm

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

Dataset = array([[2, 5, 'y'],
                 [24, 5, 'y'],
                 [2, 15, 'n'],
                 [25, 51, 'n'],
                 [6, 5, 'y']])
Trainset = array([[9, 5],
                 [4, 58],
                 [2, 15],
                 [25, 0],
                 [6, 5]])

def svm_run(dataset, trainset):
    data_input = dataset[:,:-1]
    target = dataset[:,-1]
    
    clf = svm.SVC()
    clf.fit(data_input, target)
    print clf.predict(trainset)
    
def main():

    #Kmeans
    kmeans_machine = kmeans(sample, k)
    kmeans_machine.train()

    #KNN
    knn_machine = knn(test, sample, target, k)
    print knn_machine.train()

    #Decision tree

    #SVM
    svm_run(Dataset, Trainset)
    
if __name__ == "__main__":
    main()
    
