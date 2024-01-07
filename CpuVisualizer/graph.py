import matplotlib.pyplot as pyp
import matplotlib.animation as animation

# Creating a new figure
figure = pyp.figure()

# Creating a single subplot in our figure
subplot = figure.add_subplot(1, 1, 1)

# Creating the function that reads the data from cpu.txt and feeds it to out subplot
def animation_function(i):
    cpu_data = open("cpu.txt").readlines()

    x = []

    for each_value in cpu_data:
        if (len(each_value)) > 1:
            x.append(float(each_value))

# Clearing/refreshing the figure to avoid unnecessary overwriting for each new poll (every 10 seconds)
    subplot.clear()
# Plotting the values in the list
    subplot.plot(x)

graph_animation = animation.FuncAnimation(figure, animation_function, interval = 5000)

pyp.show()
