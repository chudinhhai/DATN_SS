from node import Node
import random
import math
import sys
import queue
import os
from cost_value import Cost

def create_fixed_topology():
    sink_node = Node()
    sink_node.ID = 0
    sink_node.neighbors = [1,3,5]
    # sink_node.childrenIDs = {1,3,5}
    
    node1 = Node()
    node1.ID = 1
    node1.neighbors = [0,2,5,6]
    # node1.childrenIDs = {2,6}
    
    node2 = Node()
    node2.ID = 2
    node2.neighbors = [1]
    
    node3 = Node()
    node3.ID = 3
    node3.neighbors = [0]
    # node3.childrenIDs = {2,6}
    
    node4 = Node()
    node4.ID = 4
    node4.neighbors = [5]
    
    node5 = Node()
    node5.ID = 5
    node5.neighbors = [0,4,1]
    # node5.childrenIDs = {4}
    
    node6 = Node()
    node6.ID = 6
    node6.neighbors = [1]
    
    list = []
    list.append(sink_node)
    list.append(node1)
    list.append(node2)
    list.append(node3)
    list.append(node4)
    list.append(node5)
    list.append(node6)
    
    return list

def cal_depth_of_node(node_ID, node_list):
    min = 0
    if not node_list[node_ID].neighbors:
        return 0
    for neighbor_ID in node_list[node_ID].neighbors:
        if neighbor_ID == 0:
            return 1
        else:
            1 + cal_depth_of_node(neighbor_ID, node_list)

def build_mlst(node_list, n, l, t):
    list = []
    tree = []
    untree = []
    for component_node in node_list:
        untree.append(component_node.ID)
    # append sink node
    tree.append(0)
    untree.remove(0)
    # other node
    while len(untree)>0:
        cost_list = []
        min_cost = 9999999999999999999999
        min_id = None
        min_parentID = None

        for v_node_ID in tree:
            
            for u_node_ID in untree:
                if u_node_ID in node_list[v_node_ID].neighbors:
                    
                    cost = 1000000*(len(node_list[v_node_ID].childrenIDs) + node_list[v_node_ID].depth) + 1000*len(node_list[v_node_ID].neighbors) + len(node_list[u_node_ID].neighbors)
                    
                    if cost <= min_cost:
                        min_cost = cost
                        min_id = u_node_ID
                        min_parentID = v_node_ID
                    
                else:
                    continue

                
                
        # append node into tree
        tree.append(min_id)
        untree.remove(min_id)
        node_list[min_id].depth = node_list[min_parentID].depth + 1
        node_list[min_id].parentID = min_parentID
        node_list[min_parentID].childrenIDs.add(min_id)
        node_list[min_parentID].ready += 1
        
    save_path = "C:/Users/ADMIN/Desktop/DATN/" +  str(l) + "-" + str(l) + "/" 
    name_of_file =  str(l) + "-" + str(n) + "-" + str(t) + '.txt'
    full_directory = os.path.join(save_path, name_of_file)
    if os.path.exists(full_directory):
        os.remove(full_directory)
    os.makedirs(os.path.dirname(full_directory), exist_ok=True)
    with open(full_directory, 'w') as file:
        for node in node_list:
            string_list = []
            for childrenID in node.childrenIDs:
                string_list.append(str(childrenID))
            string_list.append(str(0))
            string_list.append("\n")
            
            file.write(",".join(string_list))

def distance (node1, node2):
    # print("distance: " + str(math.sqrt(pow((node1.x-node2.x), 2) + pow((node1.y-node2.y), 2))))
    return math.sqrt(pow((node1.x-node2.x), 2) + pow((node1.y-node2.y), 2))


if __name__ == "__main__":
    count = 0
    node_list = []
    # n = (95*2*2)/(math.pi)
    # r,im = divmod(n,1)
    save_path = "C:/Users/ADMIN/Desktop/DATN/" + str(4) + "/"
    name_of_file = str(4) + "-" + str(25) + "-" + str(0) + '.txt'
    full_directory = os.path.join(save_path, name_of_file)
    # print(full_directory)
    file = open(full_directory)
    for node_coordinate in file.readlines():
        node = Node()
        node.ID = count
        node.x = float(node_coordinate.split(',')[0])
        node.y = float(node_coordinate.split(',')[1])
        
        node_list.append(node)
        count += 1
        pass
    
    # Update neighbors
    # loop through node_list
    for i in range(0,len(node_list)):
        for k in range(1,len(node_list)):
            if(distance(node_list[i], node_list[k]) < 1):
                node_list[i].neighbors.append(k)
    
    build_mlst(node_list, 4, 25, 0)
    for component_node in node_list:
        print("ID: " + str(component_node.ID))
        print(component_node.neighbors)
        print(component_node.childrenIDs)
    