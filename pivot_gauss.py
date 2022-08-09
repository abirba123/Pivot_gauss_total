import math
import matplotlib.pyplot as plt
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity="all";
import numpy as np
from scipy.special import logsumexp
import time
import random


start = time.time()

def entrer_matrice(A,B,n):
    for r in range(0,n):
        for c in range(0,n):
            A[(r),(c)]=(input("Element a["+str(r+1)+","+str(c+1)+"] "))
        B[(r)]=(input('b['+str(r+1)+']: '))


def nb_lig(A): return len(A)
def nb_col(A): return len(A[0])
def prnt(A):
    p = nb_lig(A)
    q = nb_col(A)
    for i in range(p):
       s = ''
       for j in range(q):
          s += '%+10.5f ' % A[i][j]
       print(s)





def randmat(p,q):
    A = np.random.randint(10, size=(p, q))
    return A
def echanger_lignes(A, i, j):
    A[i], A[j] = A[j], A[i]

#echanger_lignes(A, 0, 1)
def multiplier_ligne(A, i, t):
   q = nb_col(A)
   for j in range(q): A[i][j] *= t
def combiner_lignes(A, k, i, t):
 q = nb_col(A)
 for j in range(q): A[k][j] += t * A[i][j]
def chercher_pivot(A, k):
    n = nb_lig(A)
    l = k
    while l < n and A[l][k] == 0: l = l + 1
    if l == n: raise Exception('Pivot non trouvé')
    return l
def pivoter(A, B, k, D):
    n = nb_lig(A)
    l = chercher_pivot(A, k)
    if l != k:
       D = -D
       echanger_lignes(A, k, l)
       echanger_lignes(B, k, l)
    P = A[k][k]
    D = D * P
    multiplier_ligne(B, k, 1 / P)
    multiplier_ligne(A, k, 1 / P)
    for i in range(n):
       if i != k:
          Aik = A[i][k]
          combiner_lignes(A, i, k, -Aik)
          combiner_lignes(B, i, k, -Aik)
    return D
def pivot_gauss(A, B):
 n = nb_lig(A)
 A = [A[i].copy() for i in range(n)]
 B = [B[i].copy() for i in range(n)]
 D = 1
 for i in range(n):
   D = pivoter(A, B, i, D)
 return (A, B, D)
#A = [[1, 3, 3], [2, 2, 5], [3, 2, 6]]
#B = [[-2], [7], [12]]
test=1
while(test):
    print('------------------------------------')
    print('Veuillez choisir la methode de saisi de matrice')
    print('1: une matrice aleatoire')
    print('2: votre propore matrice')
    print('0: pour quitter')
    print()


    x=int(input('Votre choix: '))

    if x==1:
        n=random.randint(5, 400)
        print('La dimension choisie aleatoirement est:',n)
        A=randmat(n,n)
        B=randmat(n,1)
    elif x==2:
        n = int(input("Entrer le dimension de la matrice"))
        A = np.zeros((n, n))
        B = np.zeros((n, 1))
        entrer_matrice(A,B,n)
    elif x==0:
        test=0;
    else:
        print('entrer un choix valide')

    A1, B1, D = pivot_gauss(A, B)
    print("Determinant de la matrice A est Det(A)=", D)
    print()
    prnt(B1)
