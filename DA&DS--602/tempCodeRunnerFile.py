
Q3=np.percentile (marks,75)
IQR = Q3-01
print(f'IQR: {IQR}')
U=Q3+1.5*IQR
L=Q1-1.5*IQR
print(f"UPPER: {U}\nLOWER: (L}")

o=[]
for min marks:
    if m>U or m<1:
        o.append(m)
print(o)