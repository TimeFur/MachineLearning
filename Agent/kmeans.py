from numpy import *
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

    def train():
        self.cluster_center()
        while self.search_flag == True:
            self.do_cluster()
            self.cluster_center()
            
    def cluster_center(self):
        if self.center == None:
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
                self.center.append(float(avg_dict[str(i)]) / float(avg_dict[str(i) + "_len"]))
            
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
            print "Search Done!"
            self.search_flag = False
        else:
            self.search_counter += 1
            self.search_flag = True
            self.group_id = group[:]
            
    
