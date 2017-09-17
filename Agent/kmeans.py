from numpy import *
import numpy as np
import random

def euclidean_dist(vec_a, vec_b):
    dis_sum = sum((vec_a - vec_b) ** 2)
    distance = dis_sum ** 0.5
    return distance

class kmeans():
    def __init__(self, dataset, k):
        self.dataset = dataset
        self.k = k
        self.center = None
        self.group_id = []
        self.search_flag = True
        self.search_counter = 0

    def train(self):
        self.cluster_center()
        while self.search_flag == True:
            self.do_cluster()
            self.cluster_center()
        
        print "Search Done!"
        for i in range(k):
            print i, self.center[i]
        print self.group_id
        
    def cluster_center(self):
        if self.center == None:
            self.center = []
            last_index = 0
            length = len(self.dataset) / k

            for i in range(k):
                last_index = random.randint(last_index, last_index + length)
                self.center.append(self.dataset[last_index])
        else:
            self.center = []
            avg_dict = {}       # id, id_len
            for i in range(k):
                avg_dict[str(i)] = 0
                avg_dict[str(i) + "_len"] = 0
            for i in range(len(self.dataset)):
                _id = self.group_id[i]
                avg_dict[str(_id)] += self.dataset[_id]
                avg_dict[str(_id) + "_len"] += 1
            
            for i in range(k):
                if float(avg_dict[str(i) + "_len"]) != 0:
                    self.center.append(np.float32(avg_dict[str(i)]) / np.float32(avg_dict[str(i) + "_len"]))
                else:
                    self.center.append(0)
            #print self.center
    def do_cluster(self):
        group = []
        for data in self.dataset:
            min_index = -1
            min_dis = -1
            for i in range(k):
                dis = euclidean_dist(data, array(self.center[i]))
                if min_dis == -1:
                    min_dis = dis
                    min_index = i
                elif dis < min_dis:
                    min_dis = dis
                    min_index = i
            group.append(min_index)
        
        if self.group_id == group:
            self.search_flag = False
        else:
            self.search_counter += 1
            self.search_flag = True
            self.group_id = group[:]
#Testing
sample = array( [[1,2],
                  [5,7],
                  [1,21],
                  [41,32],
                  [21,2],
                  [0,8]])
k = 3

k_machine = kmeans(sample, k)
k_machine.train()
    
