from sklearn import tree
from numpy import *
import numpy as np
import copy

target = ['n', 'n', 'y', 'y', 'y',
          'n', 'y', 'n', 'y', 'y',
          'y', 'y', 'y', 'n']
attribute = ['outlook', 'temp', 'humidity', 'windy']
attr_dataset = [['rainy', 'rainy', 'overcast', 'sunny', 'sunny', 'sunny', 'overcast', 'rainy', 'rainy', 'sunny', 'rainy', 'overcast', 'overcast', 'sunny'],
           ['hot', 'hot', 'hot', 'mid', 'cold', 'cold', 'cold', 'mid', 'cold', 'mid', 'mid', 'mid', 'hot', 'mid'],
           ['high', 'high', 'high', 'high', 'normal', 'normal', 'normal', 'high', 'normal', 'normal', 'normal', 'high', 'normal', 'high'],
           ['false', 'true', 'false', 'false', 'false', 'true', 'true', 'false', 'false', 'false', 'true', 'true', 'false', 'true']]

Data_set = [['rainy', 'hot', 'high', 'false', 'n'],
            ['rainy', 'hot', 'high', 'true', 'n'],
            ['overcast', 'hot', 'high', 'false', 'y'],
            ['sunny', 'mid', 'high', 'false', 'y'],
            ['sunny', 'cold', 'normal', 'false', 'y'],
            ['sunny', 'cold', 'normal', 'true', 'n'],
            ['overcast', 'cold', 'normal', 'true', 'y'],
            ['rainy', 'mid', 'high', 'false', 'n'],
            ['rainy', 'cold', 'normal', 'false', 'y'],
            ['sunny', 'mid', 'normal', 'false', 'y'],
            ['rainy', 'mid', 'normal', 'true', 'y'],
            ['overcast', 'mid', 'high', 'true', 'y'],
            ['overcast', 'hot', 'normal', 'false', 'y'],
            ['sunny', 'mid', 'high', 'true', 'n']]

def arrange_dataset(target, attribute, attr_dataset):
    dataset = {}
    for i, attr in enumerate(attribute):
        dataset[attr] = {}
        for j, attr_set in enumerate(attr_dataset[i]):
            if (attr_set in dataset[attr]) is False:
                dataset[attr][attr_set] = {}
            if (target[j] in dataset[attr][attr_set]) is False:
                dataset[attr][attr_set][target[j]] = 1
            else:
                dataset[attr][attr_set][target[j]] += 1
    return dataset

def entropy(y_num, n_num):
    #-p*log2(p) - q*log2(q)
    if y_num == 0 or n_num == 0:
        return 0
    p = float(y_num) / float(y_num + n_num)
    q = float(n_num) / float(y_num + n_num)
    v = -p * np.log2(p) - q * np.log2(q)
    return v


def E(attr, dataset):
    e_value = 0
    length = 0
    for key in dataset[attr]:
        for k in dataset[attr][key]:
            length += dataset[attr][key][k]
    for key in dataset[attr]:
        y_num = 0
        n_num = 0
        if ('y' in dataset[attr][key]) is True:
            y_num = dataset[attr][key]['y']
        if ('n' in dataset[attr][key]) is True:
            n_num = dataset[attr][key]['n']
        e_value += entropy(y_num, n_num) * (float(y_num+ n_num) / float(length))
    return e_value

def gain(attribute, dataset):
    #Entropy(T) - Entropy(T, attr)
    y_num = 0
    n_num = 0
    for attr in dataset:
        for attr_set in dataset[attr]:
            if ('y' in dataset[attr][attr_set]) is True:
                y_num += dataset[attr][attr_set]['y']
            if ('n' in dataset[attr][attr_set]) is True:
                n_num += dataset[attr][attr_set]['n']
        break
    value = entropy(y_num, n_num) - E(attribute, dataset)
    return value

def evaluate_attribute(dataset):
    max_v = 0
    max_key =""
    for attr in dataset:
        gain_v = gain(attr, dataset)
        if gain_v > max_v:
            max_v = gain_v
            max_key = attr
    return max_key, max_v

def rearrange_attr(attribute, data_set, attr):
    result_data_set = copy.deepcopy(data_set)
    attr_list = copy.deepcopy(attribute)
    data_set_dict = {}

    #Step1 choose the attr list
    if type(attr) != {}:
        once = False
        for main_attr in attr:
            tmp_data_set = []
            main_index = attr_list.index(main_attr)
            attr_list.pop(main_index)
            for sec_list in result_data_set:
                if sec_list[main_index] == attr[main_attr]:
                    tmp_data_set.append(sec_list)
            for i in tmp_data_set:
                i.pop(main_index)
            if once == False:
                result_data_set = []
                once = True
            result_data_set = tmp_data_set
        #print result_data_set
        
    #Step2 arrange dict
    for main_attr in attr_list:
        if main_attr not in data_set_dict:
            data_set_dict[main_attr] = {}
        index = attr_list.index(main_attr)
        for sec_attr_list in result_data_set:
            if sec_attr_list[index] not in data_set_dict[main_attr]:
                data_set_dict[main_attr][sec_attr_list[index]] = {}
            if sec_attr_list[-1] not in data_set_dict[main_attr][sec_attr_list[index]]:
                data_set_dict[main_attr][sec_attr_list[index]][sec_attr_list[-1]] = 1
            else:
                data_set_dict[main_attr][sec_attr_list[index]][sec_attr_list[-1]] += 1
    #print data_set_dict

    return data_set_dict


#testing
def main():

    dataset = rearrange_attr(attribute, Data_set, "")

    tree = {}
    
    #Evaluate the max gain and find attr
    max_key, max_v = evaluate_attribute(dataset)
    tmp_tree = {}

    print dataset[max_key]
    #step1: using the max_key to separate the attribute
     
    #step2: check the depth to substract the attribute
    print "---------------"
    print rearrange_attr(attribute, Data_set, {"outlook":"rainy"})
    print "---------------"
    print rearrange_attr(attribute, Data_set, {"outlook":"overcast"})
    print "---------------"
    print rearrange_attr(attribute, Data_set, {"outlook":"sunny"})
    
                
if __name__ == "__main__":
    main()




