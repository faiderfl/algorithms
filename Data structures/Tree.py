import threading, queue
from collections import deque

class TreeNode():

    def  __init__(self, value, children):
        self.value= value
        self.children=children

childsofThree= [TreeNode(7, [])]
childsofSix= [TreeNode(8,[]), TreeNode(9,[])]
childofFive=[TreeNode(10,[])]
childofTwo= [TreeNode(5,childofFive),TreeNode(6,childsofSix)]

childs= [TreeNode(2,childofTwo), TreeNode(3,childsofThree), TreeNode(4,[])]

root = TreeNode(1,childs)

def backTrace(parents, end, start):6
    path =[end]
    while path[len(path)-1] != start:
        path.append(parents[path[len(path)-1]])
    #pathReverse  path.reverse
    return  path [::-1]

def computeRoute(objetive, root): #BFS
    parents =dict()
    queueRoute= []
    queueRoute.append(root)

    while (len(queueRoute)>0):
        currentNode= queueRoute[0]
        queueRoute= queueRoute[1:]
        if currentNode.value==objetive:
           return backTrace(parents,currentNode.value,root.value)        
        for c in currentNode.children:
            parents[c.value]=currentNode.value
            queueRoute.append(c)

    return []

def getCommonAncestor(value1, value2, root):
    route1= computeRoute(value1, root) # [1,2,6,8]  
    route2= computeRoute(value2, root) # [1,2,5,10] 

    #[1,2,6,8] - [1,2,5,10]

    commonAncestor=root
    for i in range (0, min(len(route1), len(route2))):
        if route1[i]== route2[i]:
            commonAncestor=route1[i]
        else:
            break
    return commonAncestor



print(getCommonAncestor(2,3,root))
#          1 
#     2         3   4
#  5     6    7
# 10   8   9








