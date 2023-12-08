from math import lcm


def main(incoming):
    global data
    data = incoming
    steps, ghost_steps = calculate_steps()
    if steps is not None:
        print(f"The number of steps to reach the goal is is {steps}")
    print(f"The number of ghost steps to reach the goal is {ghost_steps}")


def calculate_steps():
    global instructions
    global directions
    directions = {}
    for idx, line in enumerate(data):
        match idx:
            case 0:
                instructions = line
            case 1:
                continue
            case _:
                temp = line.split(" = ")
                temp[1] = temp[1].replace("(","").replace(")","")
                directions[temp[0]] = temp[1].split(", ")
    if "AAA" in directions.keys():
        steps = normal_steps("AAA")
    else:
        steps = None
    return steps, ghost_steps()


def normal_steps(location, any_z=False):
    steps = 0
    while True:
        for direction in instructions:
            match direction:
                case "L":
                    location = directions[location][0]
                case "R":
                    location = directions[location][1]
            steps += 1
            if any_z and location.endswith("Z"):
                return steps
            elif location == "ZZZ":
                return steps


def ghost_steps():
    steps_to_goal = []
    startpoints = [x for x in directions if x.endswith("A")]
    for location in startpoints:
        steps_to_goal.append(normal_steps(location, True))
    result = lcm(*steps_to_goal)
    return result
