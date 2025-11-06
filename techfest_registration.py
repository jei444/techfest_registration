print("Welcome to SMIT TechFest!")
print("Event organized by Brylle Ladic of APPDAET BTCS2")
print()

num_participants = int(input("How many participants will register? "))

if num_participants <= 0:
    print("Invalid number of participants.")
else:
    participants = []

    for i in range(num_participants):
        name = input("Enter participant name: ")
        track = input("Enter chosen track: ")

        participant = {
            "name": name,
            "track": track
        }
        participants.append(participant)

        print()
        print("Registered Participants:")
        for i in range(len(participants)):
            print(str(i + 1) + ".", participants[i]["name"], "-", participants[i]["track"])

