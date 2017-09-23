from sklearn import tree
from numpy import *
import numpy as np


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

#testing
def main():
    dataset = arrange_dataset(target, attribute, attr_dataset)


    #Evaluate the max gain and find attr
    choose_priority = {}
    max_v = 0
    max_key =""
    for attr in dataset:
        gain_v = gain(attr, dataset)
        if gain_v > max_v:
            max_v = gain_v
            max_key = attr
        choose_priority[attr] = gain_v

    #
    print dataset[max_key]
    
    
    for attr in dataset[max_key]:
        tmp_attr_dataset = {}
        main_attr_index = attribute.index(max_key)
        if len(dataset[max_key][attr]) == 2:
            for list_data in Data_set:
                if list_data[main_attr_index] == attr:
                    #assign data
                    for i in list_data:
                        if i != attr and i != list_data[-1]:
                            
                            if not (attribute[list_data.index(i)] in tmp_attr_dataset):
                                tmp_attr_dataset[attribute[list_data.index(i)]] = {}
                                tmp_attr_dataset[attribute[list_data.index(i)]][i] = {}
                                tmp_attr_dataset[attribute[list_data.index(i)]][i][list_data[-1]] = 1
                            elif not( i in tmp_attr_dataset[attribute[list_data.index(i)]]):
                                tmp_attr_dataset[attribute[list_data.index(i)]][i] = {}
                                tmp_attr_dataset[attribute[list_data.index(i)]][i][list_data[-1]] = 1
                            elif not(list_data[-1] in tmp_attr_dataset[attribute[list_data.index(i)]][i]):
                                tmp_attr_dataset[attribute[list_data.index(i)]][i][list_data[-1]] = 1
                            else:
                                tmp_attr_dataset[attribute[list_data.index(i)]][i][list_data[-1]] += 1
            
        print attr
        print tmp_attr_dataset
        print "==============="
            
if __name__ == "__main__":
    main()




