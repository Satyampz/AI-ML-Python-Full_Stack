from scipy.stats import ttest_1samp
# salary = [44000,47000,48000,50000,55000,45000,51000,53000]
# mu=50000
# t_st,p_value=ttest_1samp(salary,mu)
# print(p_value)

# if p_value<=0.05:
#     print("Reject H0")
# else:
#     print("Fail to reject H0")

orders = [360,300]
cust = [5000,5000]

from statsmodels.stats.proportion import proportions_ztest
z_st,p_value=proportions_ztest(orders,cust)
print(p_value)
if p_value<=0.05:
    print("Reject H0")
else:
    print("Fail to reject H0")
    