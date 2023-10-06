def badge_maker(name):
    result = f"Hello, my name is {name}."
    return result

def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names]

def assign_rooms(names):
    return [f"Hello, {name}! You'll be assigned to room {i}!"for i, name in enumerate(names, start=1)]

def printer(names):
    speaker_badges = batch_badge_creator(names)
    for result in speaker_badges:
        print(result)

    speaker_rooms = assign_rooms(names)
    for room in speaker_rooms:
        print(room)
