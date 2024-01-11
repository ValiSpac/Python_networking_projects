import matplotlib.pyplot as pyp
import matplotlib.animation as animation

# creating the function that reads the data from cpu.txt and feeds it to out subplot
def animation_function(frame, ip_list, subplot):
    cpu_data = {}
    x = {}
    for ip in ip_list:
        cpu_data[ip] = open(f"{ip}_cpu").readlines()
        x[ip] = []

    for subplo in subplot:
        subplo.clear()

    for ip in ip_list:
        for each_value in cpu_data[ip]:
            if (len(each_value)) > 1:
                x[ip].append(float(each_value))
    # plotting the values in the list
    for i, ip in enumerate(ip_list):
        subplot[i].grid(True)
        subplot[i].set_xlabel("Cycle of 5 seconds")
        subplot[i].plot(x[ip], label=ip, marker='o')
        subplot[i].legend()

def show_graph(ip_list):
    num_subplots = len(ip_list)
    # creating a new figure and asigning multiple subplots
    figure , subplots = pyp.subplots(num_subplots, 1, sharex = True)

    graph_animation = animation.FuncAnimation(figure, animation_function, fargs=(ip_list, subplots,), interval = 5000)
    # adjust the layout so that labels and legends do not overlap
    pyp.show()
