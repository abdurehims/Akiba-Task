Destination = input("Enter Destination: ")
Distance = float(input("Enter distance in kilometers: "))
Average_speed = float(input("Enter Average speed in km/h: "))
Time = Distance / Average_speed

print(f" Destination: {Destination} \n Distance: {Distance}km \n Average Speed: {Average_speed} km/h \n ")
print(f"Estimated Travel Time: {Average_speed}hours")
