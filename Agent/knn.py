'''========================================
                KNN
To classify the unit sample to the
specfic group
========================================'''
from numpy import *

def cos_dist (vec_a, vec_b):
    dist = dot(vec_a, vec_b) / (linalg.norm(vec_a) * linalg.norm(vec_b))
    return dist

class knn():
    def __init__(self, testdata, sample_group, target, k):
        self.testdata = testdata
        self.sample_group = sample_group
        self.target = target
        self.k = k
        
    def train(self):
        target_group = None
        distance = []
        sortdistance_index = []
        target_vote = {}
        
        for i in range(len(self.sample_group)):
            distance.append(cos_dist(self.testdata, self.sample_group[i,:]))
        
        sortdistance_index = argsort(distance) #sorting distance and then return minimum dis's index

        for i in sortdistance_index:
            target_vote[str(self.target[i])] = 0
        for i in sortdistance_index:
            target_vote[str(self.target[i])] += 1
            if target_vote[str(self.target[i])] == self.k and target_group== None:
                target_group = str(self.target[i])

        return target_group

def knn_train (testdata, sample_group, target, k):
    target_group = None
    distance = []
    sortdistance_index = []
    target_vote = {}
    
    for i in range(len(sample_group)):
        distance.append(cos_dist(testdata, sample_group[i,:]))
    
    sortdistance_index = argsort(distance) #sorting distance and then return minimum dis's index

    for i in sortdistance_index:
        target_vote[str(target[i])] = 0
    for i in sortdistance_index:
        target_vote[str(target[i])] += 1
        if target_vote[str(target[i])] == k and target_group== None:
            target_group = str(target[i])

    return target_group

