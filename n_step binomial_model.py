import numpy as np
T=float(input("The call option expiration in years is:"))
n=int(input("The number of steps of this binomial tree is:"))
t=T/n
E=float(input("The strike price of the call option  is:"))
S_0=float(input("The stock initial value is:"))
u=float(input("The up-factor is:"))
d=float(input("The down-factor is:"))
S=np.zeros((n+1,n+1))
for i in range(n+1):
    for j in range(n+1):
            S[i,j]=S_0*(u**i)*(d**j)

f=np.zeros((n+1,n+1))
for i in range(n+1):
    for j in range(n+1):
        if i+j==n:
            f[i,j]=max(S[i,j]-E,0)

r=float(input("The risk-free interest is:"))
p=(np.exp(r*t)-d)/(u-d)
q=1-p
for k in range(n+1):
     for i in range(n):
          for j in range(n):
               if i+j==n-k:
                    Delta=(f[i+1,j]-f[i,j+1])/(S[i+1,j]-S[i,j+1])
                    f[i,j]=np.exp(-r*Delta*t)*(p*f[i+1,j]+q*f[1,j+1])

print("The call option price is "+ str(f[0,0])+".")
                    