from node import Node
import random
import os
import math
from mlst import build_mlst

def distance (node1, node2):
    # print("distance: " + str(math.sqrt(pow((node1.x-node2.x), 2) + pow((node1.y-node2.y), 2))))
    return math.sqrt(pow((node1.x-node2.x), 2) + pow((node1.y-node2.y), 2))

def create_and_save_topology(n,l,t):
    node_list = []
    N = n
    R = 1
    X = l
    Y = l    
    # gap = round(L/100, 2)
    # val_list = []
    # m = 0
    # while m<l:
    #     val_list.append(m)
    #     m += 1
        
        
    # Init sink node
    sink_node = Node()
    sink_node.ID = 0
    sink_node.x = l/2
    sink_node.y = l/2
    node_list.append(sink_node)
    i=1
    collision = True
    while len(node_list)<N:
        node = Node()
        node.ID = i
        node.x = random.uniform(0,l)
        node.y = random.uniform(0,l)
        k = 0
        is_node_same = False
        is_tranmission_link_exist = False
        for component_node in node_list:
            if component_node.x == node.x and component_node.y == node.y:
                is_node_same = True
                break
            if distance(component_node, node) <= 1:
                is_tranmission_link_exist = True
                break
                
        
        if is_node_same == False and is_tranmission_link_exist == True:
            node_list.append(node)
            i += 1
        
    for node_1 in node_list:
        for node_2 in node_list:
            if node_1.ID != node_2.ID and distance(node_1, node_2) <= 1:
                node_1.neighbors.append(node_2.ID)
    try:
        build_mlst(node_list, n, l, t) 
        save_path = "C:/Users/ADMIN/Desktop/DATN/" + str(l) + "/"
        name_of_file = str(l) + "-" + str(int(n)) + "-" + str(t) + '.txt'
        full_directory = os.path.join(save_path, name_of_file)
        with open (full_directory, 'w') as f:
            for component_node in node_list:
                f.write(str(component_node.x) + "," + str(component_node.y) + '\n')  
        print("success")
        return True
    except:
        print("t = " + str(t) + " again")
        return False
        
if __name__ == "__main__":
    i = 0
    k = 0
    D = 55
    L = 7
    n = (D*L*L)/(math.pi)
    print(n)
    r,im = divmod(n,1)
    while i<20:
        print(D)
        if create_and_save_topology(r//1, L, i) == True:
            i += 1
        else:
            continue
        
        