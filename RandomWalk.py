import matplotlib.pyplot as plt
import math
import random

#Nicer format for plot
plt.style.use('seaborn-v0_8') 

#Possible spots for the King to take
move_options = ((-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0))
TRIALS = 10000

num_steps = (10, 50, 100) #Steps accounted for are 10, 50, and 100

# ---- Initialize variables ---- #

#Average values for each step length
ave_x_pos = []
ave_y_pos = []
ave_distance = []
ave_euc_distance = []

#Store finals values for statistics
final_x_data = []
final_y_data = []
final_euc_distance_data = []
final_distance_data = []

for steps in num_steps:

    #For middle calculations
    x_positions = []
    y_positions = []
    euclidean_distances = []
    distances = []

    for _ in range(TRIALS):
        total_distance = 0
        move_setx = [0]
        move_sety = [0]

        #Perform complete walk
        for _ in range(steps): 
            new_spot = move_options[random.randint(0,7)]
            new_spotx, new_spoty = move_setx[-1] + new_spot[0], move_sety[-1] + new_spot[1]
            total_distance += ((new_spotx ** 2) + (new_spoty ** 2)) ** 0.5
            move_setx.append(new_spotx)
            move_sety.append(new_spoty)
        
        x_positions.append(new_spotx)
        y_positions.append(new_spoty)
        euclidean_distances.append(((move_setx[-1] ** 2) + (move_sety[-1] ** 2)) ** 0.5) # ( x^2 + y^2 ) ^ 1/2
        distances.append(total_distance)

    #Store final lists
    final_x_data.append(x_positions)
    final_y_data.append(y_positions)
    final_euc_distance_data.append(euclidean_distances)
    final_distance_data.append(distances)

    #Get the averages of postion, euclidean distance, and total distance for the step length
    ave_x_pos.append(sum(x_positions) / TRIALS)
    ave_y_pos.append(sum(y_positions) / TRIALS)
    ave_euc_distance.append(sum(euclidean_distances) / TRIALS)
    ave_distance.append(sum(distances) / TRIALS)

print(f"Steps In Random Walk:    \t\t{round(num_steps[0], 3)} \t\t{round(num_steps[1], 3)} \t\t{round(num_steps[2], 3)}")
print(f"Average x-value:         \t\t{round(ave_x_pos[0], 3)} \t\t{round(ave_x_pos[1], 3)} \t\t{round(ave_x_pos[2], 3)}")
print(f"Average y-value:         \t\t{round(ave_y_pos[0], 3)} \t\t{round(ave_y_pos[1], 3)} \t\t{round(ave_y_pos[2], 3)}")
print(f"Average Euc. Distance:   \t\t{round(ave_euc_distance[0], 3)} \t\t{round(ave_euc_distance[1], 3)} \t\t{round(ave_euc_distance[2], 3)}")
print(f"Average Total Distance:  \t\t{round(ave_distance[0], 3)} \t\t{round(ave_distance[1], 3)}\t\t{round(ave_distance[2], 3)}")

#Make plot
plt.plot(move_setx, move_sety)
plt.plot(0, 0, 'ko', label="Start Point")
plt.plot(move_setx[-1], move_sety[-1], 'go', label="End Point")
plt.title("Random Walk")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

#Scatter Plot
fig, axs = plt.subplots(1, 3, figsize = (10,4))
axs[0].scatter(final_x_data[0], final_y_data[0])
axs[0].set_title(f"{num_steps[0]} Steps")
axs[1].scatter(final_x_data[1], final_y_data[1])
axs[1].set_title(f"{num_steps[1]} Steps")
axs[2].scatter(final_x_data[2], final_y_data[2])
axs[2].set_title(f"{num_steps[2]} Steps")
plt.tight_layout()
plt.show()

#Histogram
fig1, axs1 = plt.subplots(1, 3, figsize = (10,4))
axs1[0].hist(final_euc_distance_data[0])
axs1[0].set_title(f"{num_steps[0]} Steps")
axs1[1].hist(final_euc_distance_data[1])
axs1[1].set_title(f"{num_steps[1]} Steps")
axs1[2].hist(final_euc_distance_data[2])
axs1[2].set_title(f"{num_steps[2]} Steps")
plt.tight_layout()
plt.show()
