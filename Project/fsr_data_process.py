import matplotlib as plt

# Convert voltage reading to mass of food (g)
# Arduino: read voltage and send to pi
# Calibrate
food_portion = 25               # Input from food portion from website setting

# At next feeding interval time, compare leftover food mass to regular portion size
food_leftover = 15             # 15 will be replaced from g read from arduino



# Adjust next feed based on leftover food
food_eaten = food_portion - food_leftover

# Save food eaten in memory somewhere
next_feed = food_eaten

# Send next_feed to motor control




# Track how much food has been eaten at each meal, this will be conducted on the website or somewhere with memory
food_eaten_log = []
food_portion_log = []
food_eaten_log.append(food_eaten)
i = 0
for i in range(len(food_eaten_log)):
    food_portion_log.append(food_portion)

print(food_eaten)
    






# Create a graph using track, display expected and actual


# Write statements about food

