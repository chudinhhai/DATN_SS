from node import Node
import random
import math
import sys
import queue
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

def build_mlst(node_list):
    list = []
    tree = []
    untree = []
    for component_node in node_list:
        untree.append(component_node.ID)
    # append sink node
    tree.append(0)
    untree.remove(0)
    # other node
    while untree:
        cost_list = []
        min = 999999999999999999999
        min_id = None
        
        for v_node_ID in tree:
            for u_node_ID in untree:
                if u_node_ID in node_list[v_node_ID].neighbors:
                    node_cost = Cost()
                    node_cost.ID = u_node_ID
                    node_cost.parentID = v_node_ID
                    node_cost.cost = 10000*(len(node_list[v_node_ID].childrenIDs) + node_list[v_node_ID].depth) + 100*len(node_list[v_node_ID].neighbors) + len(node_list[u_node_ID].neighbors)
                    cost_list.append(node_cost)
                else:
                    continue
        
        for value_cost in cost_list:
            if value_cost.cost <= min:
                min = value_cost.cost
                min_id = value_cost.ID
                min_parentID = value_cost.parentID
                
                
        # append node into tree
        tree.append(min_id)
        untree.remove(min_id)
        node_list[min_id].depth = node_list[min_parentID].depth + 1
        node_list[min_id].parentID = min_parentID
        node_list[min_parentID].childrenIDs.add(min_id)

if __name__ == "__main__":
    node_list = create_fixed_topology()
    result = build_mlst(node_list)
    
    for component_node in result:
        print("ID: " + str(component_node.ID))
        print(component_node.childrenIDs)
    