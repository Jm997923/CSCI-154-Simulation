import matplotlib.pyplot as plt
import math
import random

#Nicer format for plot
plt.style.use('seaborn-v0_8') 

#Possible spots for the King to take
move_options = ((-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0))

#Initialize location
move_setx = [0]
move_sety = [0]

steps = int(input("How many steps do you want to take?: "))

total_distance = 0
for i in range(steps):
    new_spot = move_options[random.randint(0,7)]
    new_spotx, new_spoty = move_setx[-1] + new_spot[0], move_sety[-1] + new_spot[1]
    total_distance += ((new_spotx ** 2) + (new_spoty ** 2)) ** (1 / 2)
    move_setx.append(new_spotx)
    move_sety.append(new_spoty)

#Summary Statistics of Random Walk
print(f"Final Location: {move_setx[-1]}, {move_sety[-1]}")
print(f"Euclidian Distance: { ((move_setx[-1] ** 2) + (move_sety[-1] ** 2)) ** (1 / 2)}")
print(f"Total Distance traveled: {total_distance}")

#Make plot
plt.plot(move_setx, move_sety)
plt.plot(0, 0, 'ko', label="Start Point")
plt.plot(move_setx[-1], move_sety[-1], 'go', label="End Point")
plt.title("Random Walk")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()