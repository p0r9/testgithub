import matplotlib.pyplot as plt

Days = ['Thu','Fri','Sat','Sun']
Tables = [62,19,87,76]

plt.figure()
plt.pie(Tables,labels=Days,autopct='%1.2f%%')
plt.show()