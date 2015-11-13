#to I
from_A = 8
from_B = 6
from_C = 6
from_D = 3
from_E = 10
from_F = 2
from_G = 5
from_H = 5
from_J = 2
from_K = 15

froml =  [from_A, from_B, from_C, from_D, from_E, from_F, from_G, from_H, from_J, from_K]

#from I
to_A=20
to_B=22
to_C=23
to_D=28
to_E=29
to_F=26
to_G=28
to_H=16
to_J=2
to_K=6
to_L=7
to_M=9

tol = [to_A,to_B,to_C,to_D,to_E,to_F,to_G,to_H,to_J,to_K,to_L,to_M]
to = list("ABCDEFGHJKLM")

#print len(tol) == len(to)

print "_,A,B,C,D,E,F,G,H,J,K"

for i in range(len(tol)):
  print to[i], ",",
  for fromv in froml[:-1]: print tol[i] + fromv, ",",
  print tol[i] + froml[-1]
  



