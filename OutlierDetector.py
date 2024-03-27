import numpy as np
from scipy.stats import entropy

def SFE(S,q): 
    pool = np.zeros(0)
    differences = np.abs(S - q)
    dmax = np.max(differences)
    dmin = np.min(differences)
    sum = 0
    for i in range(np.shape(S)[0]):
        p = S[i]
        if (dmax-dmin) !=0 and ((np.abs(q - p)-dmin)) !=0:
            sum = ((np.abs(q - p)-dmin)/(dmax-dmin))*np.log2((np.abs(q - p)-dmin)/(dmax-dmin))    
    return –sum

S = np.zeros((T,mu,n))
FWV = np.zeros((T,n))
AFS = np.empty((0, 2), dtype=int)

for i in range(T):
    subset_indices = np.random.choice(m, mu, replace=False)
    S[i] = Y[subset_indices]

a = np.zeros((n,m))
for i in range(n):a[i] = Y.T[i]

for i in range(T):
    for j in range(n):
        q = np.mean(a[j])   
        SFEq = SFE(S[i].T[j],q)
        SFEp = 0
        for k in range(np.shape(S[0].T[0])[0]):
            p = S[i].T[j][k]
            SFEp += SFE(S[i].T[j],p)
        SFEp = SFEp/np.shape(S[i].T[j])[0]
        if SFEq > SFEp:
            pair = np.array([[i, j]])
            AFS = np.vstack([AFS, pair])
   
        FWV[i][j] = SFEq

for i in range(T):
    for j in range(n):    
        FWV[i][j] = betta
        
for k in range(np.shape(AFS)[0]):
    i = AFS[k][0]
    j = AFS[k][1]
    FWV[i][j] = alfa
    


SW = np.zeros((T,mu)) 
for i in range(T):
    for j in range(mu):
        
        for i_ in range(n):
            SW[i][j] += FWV[i][i_]*(abs(S[i][j][i_] -np.mean(a[i_])))
        SW[i][j] = SW[i][j]**0.5    
