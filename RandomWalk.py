import matplotlib.pyplot as plt
import math
import random

#Nicer format for plot
plt.style.use('seaborn-v0_8') 

#Possible spots for the King to take
move_options = ((-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0))
TRIALS = 10000

#Initialize location
move_setx = [0]
move_sety = [0]

num_steps = (10, 50, 100) #Steps accounted for are 10, 50, and 100

# ---- Initialize variables ---- #

#Average values for each step length
ave_x_pos = []
ave_y_pos = []
ave_distance = []
ave_euc_distance = []

#For middle calculations
final_positions_x = []
final_positions_y = []
final_euclidean_distances = []
total_distances = []
for steps in num_steps:
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
        
        final_positions_x.append(new_spotx)
        final_positions_y.append(new_spoty)
        final_euclidean_distances.append(((move_setx[-1] ** 2) + (move_sety[-1] ** 2)) ** 0.5) # ( x^2 + y^2 ) ^ 1/2
        total_distances.append(total_distance)

    #Get the averages of postion, euclidean distance, and total distance for the step length
    ave_x_pos.append(sum(final_positions_x) / TRIALS)
    ave_y_pos.append(sum(final_positions_y) / TRIALS)
    ave_euc_distance.append(sum(final_euclidean_distances) / TRIALS)
    ave_distance.append(sum(total_distances) / TRIALS)

print(f"Steps In Random Walk:    \t\t{round(num_steps[0], 3)} \t\t{round(num_steps[1], 3)} \t\t{round(num_steps[2], 3)}")
print(f"Average x-value:         \t\t{round(ave_x_pos[0], 3)} \t\t{round(ave_x_pos[1], 3)} \t\t{round(ave_x_pos[2], 3)}")
print(f"Average y-value:         \t\t{round(ave_y_pos[0], 3)} \t\t{round(ave_y_pos[1], 3)} \t\t{round(ave_y_pos[2], 3)}")
print(f"Average Euc. Distance:   \t\t{round(ave_euc_distance[0], 3)} \t\t{round(ave_euc_distance[1], 3)} \t\t{round(ave_euc_distance[2], 3)}")
print(f"Average Total Distance:  \t\t{round(ave_distance[0], 3)} \t\t{round(ave_distance[1], 3)}\t\t{round(ave_distance[2], 3)}")

#Make scatter plot

#Make plot
plt.plot(move_setx, move_sety)
plt.plot(0, 0, 'ko', label="Start Point")
plt.plot(move_setx[-1], move_sety[-1], 'go', label="End Point")
plt.title("Random Walk")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
