import matplotlib.pyplot as plt
#Add pyplot in order for plt.scatter to work

from random_walk import RandomWalk

#Keep making random walks while the program is active

while True:
    #make a random walk, and plot the points
    rw = RandomWalk(5000)
    #To add points just put the number of points you want in the parentheis
    rw.fill_walk()

    #Set the size of the plotting window.
    plt.figure(figsize=(10,6))
    

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values,c=point_numbers,cmap=plt.cm.Reds
    ,edgecolors='none',
     s=1)
    
    
    #Rmphasize the first and last point
    plt.scatter(0,0, c='green', edgecolors='none', s=100)
    #0,0 is the first point and we are going to color it to find it
    plt.scatter(rw.x_values[-1],rw.y_values[-1], c='red', edgecolors='none' ,
    s=100)
    #Rw.x_values is used to find the last point of the walk

    
    

    plt.show()

    
    
    

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
