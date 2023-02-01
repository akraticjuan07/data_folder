import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
#this is used to plot a line of dots
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolors='none', s=40)
#To change the color you will need to put edgecolor and c is shorten for color
#You can also use RGB color 
#cmp means colormap which  is a series of colors


#Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)


#Set size of tick labels.
plt.tick_params(axis='both',which='major',labelsize=14)

#Set the range for each axis
plt.axis([0,1100, 0 ,1100000])
plt.savefig('squares_plot.png',bbox_inches='tight')
#To save the plot you have to put plt.savefig and name the file/