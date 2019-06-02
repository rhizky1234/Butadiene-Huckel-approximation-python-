import numpy as np
from numpy import linalg as LA
from numpy.linalg import inv
#H=[[α,β,0,0],[β,α,β,0],[0,β,α,β],[0,0,β,α]]
i=np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
M=np.array([[0,1,0,0],[1,0,1,0],[0,1,0,1],[0,0,1,0]]) #define H as αi+βM
d=LA.eig(M)[0] #the diagonalized form of the matrix M
E=np.diag(d) #the diaonalized Hamiitonian matrix
N=i+M
c=LA.eig(N)[1] #the matrix that achieves the diaginalization

print("E1=α+ %.2f"% E[2,2],"β", "Ψ1= %.3f"% -c[0,2],"χA+","%.3f"% -c[1,2],"χB+","%.3f"% -c[2,2],"χC+","%.3f"% -c[3,2],"χD")
print("E2=α+ %.2f"% E[3,3],"β", "Ψ2= %.3f"% -c[0,3],"χA+","%.3f"% -c[1,3],"χB+","%.3f"% -c[2,3],"χC+","%.3f"% -c[3,3],"χD")
print("E3=α+ %.2f"% E[1,1],"β", "Ψ3= %.3f"% c[0,1],"χA+","%.3f"% c[1,1],"χB+","%.3f"% c[2,1],"χC+","%.3f"% c[3,1],"χD")
print("E4=α+ %.2f"% E[0,0],"β", "Ψ4= %.3f"% -c[0,0],"χA+","%.3f"% -c[1,0],"χB+","%.3f"% -c[2,0],"χC+","%.3f"% -c[3,0],"χD")
