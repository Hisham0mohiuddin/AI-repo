import numpy as np 
import pandas as pd 
import queue

def dfs(jug1, jug2):
    if (jug1,jug2) in visited :
        return False
    
    visited.add((jug1,jug2))
    path.append((jug1,jug2))
    if jug1==t or jug2 == t:
        return True
    
    if dfs(n,jug2):
        return True
    if(dfs(jug1,m)):
        return True
    if(dfs(0,jug2)):
        return True
    if(dfs(jug1,0)):
        return True
    # pour from jug1 to jug2
    if(dfs(max(0,jug1-(m-jug2)),min(5,jug1+jug2))):
        return True
    if dfs(min(3,jug1+jug2),max(0,jug2-(n-jug1))):
        return True
    
    path.pop()
    return False


    

if __name__ =="__main__":
    n = int(input("enter the capacity of jug 1: "))
    m = int(input("of the second jug: "))
    t = int(input("enter the target to reach: "))

    visited = set()
    path = []
    if dfs(0,0):
        print(path)
