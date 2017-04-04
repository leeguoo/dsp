# Matrix Algebra
import numpy as np

A = np.matrix([[1,2,3],[2,7,4]])
B = np.matrix([[1,-1],[0,1]])
C = np.matrix([[5,-1],[9,1],[6,0]])
D = np.matrix([[3,-2,-1],[1,2,3]])

u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])
w = np.array([[1],[8],[0],[5]])

print "A=\n",A
print "B=\n",B
print "C=\n",C
print "D=\n",D
print "u=\n",u
print "v=\n",v
print "w=\n",w
print ""

####
print "1.Matrix Dimensions"
print "1.1) A\n", "{0}x{1}".format(A.shape[0],A.shape[1])
print "1.2) B\n", "{0}x{1}".format(B.shape[0],B.shape[1])
print "1.3) C\n", "{0}x{1}".format(C.shape[0],C.shape[1])
print "1.4) D\n", "{0}x{1}".format(D.shape[0],D.shape[1])
print "1.5) u\n", len(u)
print "1.6) w\n", len(w)
print ""

####
print "2.Vector Operations"
print "2.1) u+v=\n", u+v
print "2.2) u-v=\n", u-v
print "2.3) alpha*u=\n",6*u
print "2.4) u.v=\n",np.dot(u,v)
print "2.5)||u||=\n",np.linalg.norm(u)
print ""

####
print "3.Matrix Operations"
print "3.1) A+C=\nnot defined"
print "3.2) A-C^T=\n",A-C.transpose()
print "3.3) C^T+3D=\n",C.transpose()+3*D
print "3.4) BA=\n",np.dot(B,A)
print "3.5) BA^T=\nnot defined"

####
print "3.6) BC=\nnot defined"
print "3.7) CB=\n",np.dot(C,B)
print "3.8) B^4=\n",np.power(B,4)
print "3.9) AA^T=\n",np.dot(A,A.transpose())
print "3.10) D^TD=\n",np.dot(D.transpose(),D)
