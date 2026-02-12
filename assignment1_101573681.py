"""
Author: Sofia Janik
Assignment: #1
"""

# Step b: Create 4 variables

gym_member = "Alex Alliton" #String with the member name
preferred_weight_kg = 20.5 #Float showing preferred weight of the member
highest_reps = 25 #Int showing the highest rep the member can do
membership_active = True #boolean showing the membership status 

# Step c: Create a dictionary named workout_stats

#Key represents the name of a friend, first value represents yoga, second value represents running and third value represents weightlifting
workout_stats = {"Alex": (50, 45, 40), "Jamie": (20, 35, 45), "Taylor": (45, 20, 35)} 

# Step d: Calculate total workout minutes using a loop and add to dictionary

total_minutes = {} #Dictionary that stores workout minutes for friends
#Stores the sum of minutes into total_minutes
for name in workout_stats:
    activity_minutes = workout_stats[name]
    total_minutes[name + "_Total"] = sum(activity_minutes)

#Stores the total minutes into the original dictionary
for key in total_minutes:
    workout_stats[key] = total_minutes[key]

# Step e: Create a 2D nested list called workout_list

workout_list = []
#Looping through dictionary keys with an intention of adding the activity minutes to workout_list
for name in workout_stats:
    if not name.endswith("_Total"):
        yoga, running, weightlifting = workout_stats[name]
        workout_list.append([yoga, running, weightlifting])

# Step f: Slice the workout_list

#Printing yoga and running for all friends
print("Yoga and running for all friends:")
for row in workout_list:
    print(row[0:2])
#Print the minutes for weigthlifting for the last two friends
print("Weightlifting for the last two friends:")
for row in workout_list[-2:]:
    print(row[2])

# Step g: Check if any friend's total >= 120

for name in workout_stats:
    if name.endswith("_Total"):
        #Checks if any of the friends has workout minutes that are 120 or above
        if workout_stats[name] >= 120:
            original_name = name.replace("_Total", "")
            #Congartulating the friend on working out a lot
            print("Great job staying active, ", original_name + " !")

# Step h: User input to look up a friend

input = input("Enter a friend's name: ")
#Checks if the friend exists
if input in workout_stats:
    yoga, running, wieghtlifting = workout_stats[input] #Workout stats with the friend name get assigned into variables 
    total = workout_stats[input + "_Total"]
    #Print stats
    print("Yoga:", yoga)
    print("Running:", running)
    print("Weightlifting:", wieghtlifting)
    print("Minutes:", total)

else:
    print("Friend", input, "not found in the records.") #If the friend doesn't exist print this messages

# Step i: Friend with highest and lowest total workout minutes

highest_friends = [] #Has to be an array because if two friends have the same highest score the program doesn't do its job well
lowest_friends = [] #Has to be an array because if two friends have the same lowest score the program doesn't do its job well
highest_total = -1 #Added so a it is guaranteed for the if statement to change it
lowest_total = 9999999 #Added so a it is guaranteed for the if statement to change it

for name in workout_stats:
    if name.endswith("_Total"):
        total_value = workout_stats[name]
        original_name = name.replace("_Total", "")

        #Checks for the highest value
        if total_value > highest_total:
            highest_total = total_value
            highest_friends = [original_name]

        elif total_value == highest_total:
            highest_friends.append(original_name)

        #Checks for the lowest value
        if total_value < lowest_total:
            lowest_total = total_value
            lowest_friends = [original_name]

        elif total_value == lowest_total:
            lowest_friends.append(original_name)


print("Highest workout minutes:", highest_friends, highest_total)
print("Lowest workout minutes:", lowest_friends, lowest_total)