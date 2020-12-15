distance_str = input("How many km do you have to travel from home to work?")

distance_int = int(distance_str)

walking_speed_kmh = float(input("What is your speed in km/h when walking?"))
walking_going_min = 1
walking_parking_min = 0

walking_travel_time_min = walking_going_min + 60 * (distance_int / walking_speed_kmh) + walking_parking_min

biking_speed_kmh = float(input("What is your speed in km/h when biking?"))
biking_going_min = 3
biking_parking_min = 2

biking_travel_time_min = biking_going_min + 60 * (distance_int / biking_speed_kmh) + biking_parking_min

driving_speed_kmh = float(input("What is your speed in km/h when driving?"))
driving_going_min = 5
driving_parking_min = 8

driving_travel_time_min = driving_going_min + 60 * (distance_int / driving_speed_kmh) + driving_parking_min

print("It will take you", walking_travel_time_min, "minutes to get from home to work by walking")
print("It will take you", biking_travel_time_min, "minutes to get from home to work by biking")
print("It will take you", driving_travel_time_min, "minutes to get from home to work by driving")


