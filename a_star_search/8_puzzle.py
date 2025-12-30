# %%
import numpy as np
import pickle 
import pandas as pd
import heapq
import copy

# %%
# we first need to make a node class to amke sure we confer to the 
# rules of the game 
class Node:
    def __init__(self,board,level,fval,parent=None):
        self.board = board
        self.level = level
        self.fval= fval 
        self.parent = parent
    def find(self,board,x):
        """find the x in the board to find blank space"""
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if board[i][j]== x:
                    return i,j
    def valid(self, x,y):
        if(x>=0 and x< len(self.board) and y>=0 and y< len(self.board) ):
            return True
        else:
            return False
    def its_children(self):
        x,y = self.find(self.board,0)
        moves = [
            [x,y-1],
            [x,y+1],
            [x-1,y],
            [x+1,y]
        ]
        valid_moves=[]
        for i in moves:
            if(self.valid(i[0],i[1])):
                valid_moves.append(i)
        children = []
        for i in valid_moves :
            child = self.move(self.board, x,y,i[0],i[1])
            child_node = Node(child,self.level+1,0,parent=self)
            children.append(child_node)
        return children
    def move(self, board, i1,j1,i2,j2):
        """i1, j1 is the blank space 
        i2, j2 is the place to be moved"""
        child = copy.deepcopy(board)
        child[i1][j1]= child[i2][j2]
        child[i2][j2]= 0
        return child
        
    
        

# %%
# let h be the no of the wrong placemtns
# let g be the no fo levels to get to here 
class Solve:
    def __init__(self,size,game,final_state):
        self.n = size
        self.open = []
        self.closed = []
        self.game = game
        self.final_state= final_state
        self.visited=[]
        
        
    def h (self,board,goal):
        ct =0 
        for i in range(self.n):
            for j in range(self.n):
                if board[i][j] != 0 and board[i][j] != self.final_state[i][j]:
                    ct+=1
        return ct
    def g(self, board):
        return board.level
    
    def f (self, node):
        return self.h(node.board,self.final_state)+ node.level
    def print_path(self, node):
        path = []
        while node:
            path.append(node.board)
            node = node.parent
        path.reverse()

        for state in path:
            print(state)
            print("↓")
    def running(self):
        start = self.game
        goal = self.final_state

        start = Node(start,0,0)
        start.fval = self.f(start)

        self.open.append(start)
        while self.open:
            current = self.open.pop(0)

            board_key = tuple(current.board.flatten())
            if board_key in self.visited:
                continue
            self.visited.append(board_key)
            
            if(self.h(current.board,goal)==0):
                print("solved")
                self.print_path(current)
                break


            for i in current.its_children():
                # print(i.board)
                i.fval = self.f(i)
                self.open.append(i)
            
            self.closed.append(current)
            

            self.open.sort(key=lambda x: x.fval,reverse=False)

    

    

# %%
np.random.seed(21)
game = np.arange(1,9)
game = np.append(game,0)

final_state = game.reshape((3,3)).copy()
np.random.shuffle(game)
game = game.reshape((3,3))
print(game)


# %%
puz = Solve(3,game,final_state)
puz.running()


