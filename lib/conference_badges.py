def badge_maker(name):
    result = f"Hello, my name is {name}."
    return result

def batch_badge_creator(names):
    speaker_badges = []
    for name in names:
        speaker_badges.append(f"Hello, my name is {name}.") 
    return speaker_badges

def assign_rooms(names):
    speaker_rooms = []
    for i, name in enumerate(names, start=1):
        speaker_rooms.append(f"Hello, {name}! You'll be assigned to room {i}!")

    return speaker_rooms

def printer(names):
    speaker_badges = batch_badge_creator(names)
    for result in speaker_badges:
        print(result)

    speaker_rooms = assign_rooms(names)
    for room in speaker_rooms:
        print(room)
