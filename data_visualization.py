import matplotlib.pyplot as plt
# to import  matplotlib you use import it and change it to plt
input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.plot(input_values,squares, linewidth=5)
#Controls the thickness of the line

#Set chart tiitle and label axes.
plt.title("Square numbers", fontsize=24)
#Sets the name of the chart
plt.xlabel("Value", fontsize=14)
#allows you to set a title for each axes
plt.ylabel("Square of value" , fontsize=14)

#Set size of tick labels
plt.tick_params(axis='both', labelsize=14)
plt.show()
#to plot the number you use plt.show