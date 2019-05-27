import matplotlib.pyplot as plt 

Umtiti=[92.9,68.3]
x=[1,4]
Lenglet=[88.8,48.7]
x1=[1.5,4.5]

tick_label=['Passing\nAccuracy','Passes']
plt.barh(x,Umtiti,align='center',label='Umtiti',color='red')
plt.barh(x1,Lenglet,align='center',label='Lenglet',color='blue')

plt.yticks(x,tick_label,rotation='horizontal')
plt.title('La Liga\nUmtiti 2016-17 vs Lenglet 2018-19')
plt.legend()
plt.show()