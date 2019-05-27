import matplotlib.pyplot as plt 

Umtiti=[1.1,1.8,1.9,2.7,0.3,0.6,0.2,1,0.8,5]
x=[]
for i in range(1,40,+4):
	x.append(i)
Lenglet=[2.1,1.8,0.7,2.8,1,0.8,0.5,0,0.7,2.8]
x1=[]
for i in range(2,40,+4):
	x1.append(i)
tick_label=['Tackles','Aerials\nWon','Interceptions','Clearances','Blocks','Offsides\nWon','Dribbled\nPast','Goals','Fouled','Long\nBalls']
plt.bar(x,Umtiti,align='center',label='Umtiti',color='red')
plt.bar(x1,Lenglet,align='center',label='Lenglet',color='blue')

plt.xticks(x,tick_label,rotation='horizontal')
plt.title('La Liga\nUmtiti 2016-17 vs Lenglet 2018-19')
plt.legend()
plt.show()
# left=[1,2,3,4,5]
# width=[10,24,36,20,5]
# #Label for each bar
# tick_label=['One','Two','Three','Four','Five']
# #Plotting the Bar Chart
# plt.barh(left,width,height=0.2,color=['red','blue'])
# plt.xlabel('X-Axis')
# plt.ylabel('Y-Axis')
# plt.title('Bar Graph')
# #Assigning the label for each bar 
# plt.xticks(left,tick_label,rotation='vertical')
# plt.legend()
# #Display the plotted graph
# plt.show()
