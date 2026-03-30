# from matplotlib import pyplot as plt
# import numpy as np
# marks = [-33,30,40,45,50,60,70,80,85,90,250]
# plt.boxplot(marks)
# plt.show()

# Q1=np.percentile(marks,25)
# Q3=np.percentile (marks,75)
# IQR = Q3-Q1
# print(f'IQR: {IQR}')
# U=Q3+1.5*IQR
# L=Q1-1.5*IQR
# print(f"UPPER: {U}\nLOWER: {L}")

# o=[]
# for m in marks:
#     if m>U or m<1:
#         o.append(m)
# print(o)


# import seaborn as sns
# from matplotlib import pyplot as plt
# salary = [20000,30000,35000,38000,60000,68000,45000]
# sns.histplot(salary,kde=True)
# plt.show()


import pandas as pd
salary = [20000,30000,35000,40000,45000,150000]
marks = [20,78,79,80,81,82,83,87]
adults_ht = [165,167,166,168,169,170]
sal=pd.Series(salary)
print(sal.skew())   #2.2719408103984624

mk=pd.Series(marks)
print(mk.skew())  #-2.7361608308899634

h=pd.Series(adults_ht)
print(h.skew())   #00