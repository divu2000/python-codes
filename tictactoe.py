# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 13:25:18 2021

@author: Divneet
"""
import numpy
board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
p1s='X'
p2s='0'
def place(symbol):
    print(numpy.matrix(board))
    while(1):
        row=int(input('enter row 1 or 2 or 3'))
        col=int(input('enter col 1 or 2 or 3'))
        if(row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=='-'):
            break
        else:
            print('invalid try again')
    board[row-1][col-1]=symbol

def checkcol(symbol):
    for c in range(3):
        
        count=0
        for r in range(3):
            if board[r][c]==symbol:
                count+=1
        if count==3:
            print(symbol,'won')
            return True
    return False
def checkrow(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if board[r][c]==symbol:
                count+=1
        if count==3:
            print(symbol,'won')
            return True
    return False
def checkdiagnol(symbol):
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[2][2]==symbol:
        return True
    if board[2][0]==board[1][1] and board[1][1]==board[0][2] and board[1][1]==symbol:
        return True
    return False
def won(symbol):
    return checkrow(symbol) or checkcol(symbol) or checkdiagnol(symbol)            

def play():
    for turn in range(9):
        if turn%2==0:
            print(p1s,'turn')
            place(p1s)
            if won(p1s):
                break
        else:
             print(p2s,'turn')
             place(p2s)
             if won(p2s):
                 break
play()

                   