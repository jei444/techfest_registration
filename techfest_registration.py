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

        participant = {"name": name, "track": track}
        participants.append(participant)

    print()
    print("Registered Participants:")
    for i in range(len(participants)):
        print(str(i + 1) + ".", participants[i]["name"], "-", participants[i]["track"])

    print()
    unique_tracks = set()
    for participant in participants:
        unique_tracks.add(participant["track"])

    print("Tracks offered in this event:")
    track_list = list(unique_tracks)
    tracks_output = ""
    for i in range(len(track_list)):
        if i == 0:
            tracks_output = track_list[i]
        else:
            tracks_output = tracks_output + ", " + track_list[i]
    print(tracks_output)

    print()
    if len(unique_tracks) < 2:
        print("Not enough variety in tracks.")

    print()
    seen_names = set()
    found_duplicate = False

    for participant in participants:
        name = participant["name"]
        if name in seen_names:
            print("Duplicate name found:", name)
            found_duplicate = True
            break
        seen_names.add(name)

    if found_duplicate == False:
        print("No duplicate names.")

    print()
    track_summary = {}

    for participant in participants:
        track = participant["track"]
        if track in track_summary:
            track_summary[track] = track_summary[track] + 1
        else:
            track_summary[track] = 1

    print("Participants per track:")
    for track in track_summary:
        print(track + ":", track_summary[track])