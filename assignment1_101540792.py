#==================================#
#   Author:  Hunter Lusk
#   Assignment: #1
#   Class: comp2152
#   ID: 101540792
#==================================#

# Step b: Create 4 variables

gym_member = "Alex Alliton"# String

preferred_weight_kg = 20.5# Float

highest_reps = 25# Integer

membership_active = True# Boolean

# Step c: Create a dictionary named workout_stats

workout_stats = {"Alex": (30, 45, 20), "Jamie": (40, 35, 50), "Taylor": (25, 30, 60) }

# Step d: Calculate total workout minutes using a loop and add to dictionary

friends = list(workout_stats.keys())

for friend in friends:
    minutes = workout_stats[friend]
    
    total = 0
    for minute in minutes:
        total = total + minute
    
    workout_stats[friend + "_Total"] = total

# Step e: Create a 2D nested list called workout_list

for friend in workout_stats:
    if "_Total" not in friend:
        minutes_tuple = workout_stats[friend]
        minutes_list = list(minutes_tuple)
        workout_list.append(minutes_list)

# Step f: Slice the workout_list

print("Yoga and Running minutes for all friends:")
for row in workout_list:
    print(row[0:2]) 

print("Weightlifting minutes for two friends:")
two_friends = workout_list[-2:]

for row in two_friends:
    print(row[2]) 

# Step g: Check if any friend's total >= 120

for key in workout_stats:
    if "_Total" in key:
        if workout_stats[key] >= 120:
            name = key.replace("_Total", "")
            print("Great job staying active,", name + "!")

# Step h: User input to look up a friend

friend_name = input("Enter a friend's name: ")

if friend_name in workout_stats and "_Total" not in friend_name:
    
    minutes = workout_stats[friend_name]
    total = workout_stats[friend_name + "_Total"]
    
    print(friend_name + "'s Workout Minutes:")
    print("Yoga:", minutes[0], "minutes")
    print("Running:", minutes[1], "minutes")
    print("Weightlifting:", minutes[2], "minutes")
    print("Total:", total, "minutes")

else:
    print("Friend", friend_name, "not found in the records.")

# Step i: Friend with highest and lowest total workout minutes

highest_total = None
lowest_total = None
highest_person = ""
lowest_person = ""

for key in workout_stats:
    if "_Total" in key:
        total = workout_stats[key]
        name = key.replace("_Total", "")
        
        if highest_total is None or total > highest_total:
            highest_total = total
            highest_person = name
        
        if lowest_total is None or total < lowest_total:
            lowest_total = total
            lowest_person = name


print("Person with highest total workout Time = ", highest_person)
print("Person with lowest total workout Time = ", lowest_person)
