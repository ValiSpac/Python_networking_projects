import matplotlib.pyplot as pyp
import matplotlib.animation as animation

# creating the function that reads the data from cpu.txt and feeds it to out subplot
def animation_function(frame, ip_list, subplot):
    cpu_data = {}
    x = {}
    for ip in ip_list:
        cpu_data[ip] = open(f"{ip}_cpu").readlines()
        x[ip] = []

    for ip in ip_list:
        for each_value in cpu_data[ip]:
            if (len(each_value)) > 1:
                x[ip].append(float(each_value))
    # clearing/refreshing the figure to avoid unnecessary overwriting for each new poll (every 5 seconds)
    subplot.clear()
    # plotting the values in the list
    for ip in ip_list:
        subplot.plot(x[ip], label=ip)

    subplot.legend()

def show_graph(ip_list):
    # creating a new figure and asigning multiple subplots
    figure , subplot = pyp.subplots()

    graph_animation = animation.FuncAnimation(figure, animation_function, fargs=(ip_list, subplot,), interval = 5000)

    pyp.show()
