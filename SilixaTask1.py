import math

print('Enter R and N values.')

R = float(input())
T = 1 - R
N = int(input())
node = 2*N - 1
i0 = 1*R*T**(node - 1)
j = 3
In = 0
while j < node:
    k = 1*R**j*T**(node - j)
    nj = math.factorial(node)/(math.factorial(j)*math.factorial(node - j))
    In += k*nj
    j += 2
print('Your basic I is ')
print(i0)
print('Your indirect I is')
print(In)
efficiency = i0/In*100
print('Current quality is ')
print(str(efficiency)+'%')
