import matplotlib.pyplot as plt
import numpy as np

# Convert voltage reading to mass of food (g)

# Arduino: read voltage and send to pi                  #COMM   Ard to Pi


# Calibrate



food_eaten_log = []
food_portion_log = []

while True:
    food_portion = 25               # Input from food portion from website setting          #COMM   Web to File

    # At next feeding interval time, compare leftover food mass to regular portion size
    food_leftover = int(input("Enter food leftover: "))             # 15 will be replaced from g read from arduino
    if(food_leftover == 66):
        break



    # Adjust next feed based on leftover food
    food_eaten = food_portion - food_leftover

    # Save food eaten in memory somewhere
    next_feed = food_eaten

    # Send next_feed to motor control           #COMM Pi to Ard
    # Inverse of voltage to grams equation


    # Track how much food has been eaten at each meal, this will be conducted on the website or somewhere with memory

    food_eaten_log.append(food_eaten)
    food_portion_log.append(food_portion)

    print("food eaten:")
    print(food_portion)
    print("log:")
    print(food_eaten_log)
    print(food_portion_log)

# Plotting food                                 #COMM File to Web
num_feeds = [z for z in range(len(food_eaten_log))]

        
plt.plot(num_feeds,food_eaten_log)
plt.plot(num_feeds, food_portion_log)
plt.xlabel("Number of feeds")
plt.ylabel("Food (g)")
plt.ylim(0, 50)
plt.legend(["Food eaten", "Food portion"])
plt.show()

avg_food_eaten = np.average(food_eaten_log)
print(avg_food_eaten)
if(food_portion - avg_food_eaten >= 5):
    print("Your cat is not eating enough")
elif(food_portion - avg_food_eaten < 5):
    print("Your cat is eating well")

