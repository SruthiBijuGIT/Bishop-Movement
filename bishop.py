# Given an empty chess board and one Bishop placed in any square, say (r,c) generate the list of all squares the Bishop could not move to 
r = int(input())
c = int(input())

MAX = 64

if c != 1:
  print(r,c-1)
if c != MAX:
  print(r,c+1)
if r != MAX:
  print(r+1,c)
if r != 1:
  print(r-1,c)
