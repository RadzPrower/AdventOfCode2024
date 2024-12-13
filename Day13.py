import math


def main(data):
    machines = parse_data_to_machines(data)
    for machine in machines:
        machine.fewest_tokens()
        print("-------------------")
    result = "This is not yet implemented."
    print(result)
    return result
    
    
def parse_data_to_machines(data):
    machines = []
    a = (0, 0)
    b = (0, 0)
    x = 0
    y = 0
    for line in data:
        if "Button A" in line:
            directions = line.split(":")[1].split(",")
            x_direction = directions[0].split("+")[1]
            y_direction = directions[1].split("+")[1]
            a = int(x_direction), int(y_direction)
        if "Button B" in line:
            directions = line.split(":")[1].split(",")
            x_direction = directions[0].split("+")[1]
            y_direction = directions[1].split("+")[1]
            b = int(x_direction), int(y_direction)
        if "Prize" in line:
            values = line.split(":")[1].split(",")
            x = int(values[0].split("=")[1])
            y = int(values[1].split("=")[1])
        if line == "":
            machines.append(Machine(a, b, x, y))
            a = (0, 0)
            b = (0, 0)
            x = 0
            y = 0
    machines.append(Machine(a, b, x, y))
    return machines
    
    
class Machine:
    def __init__(self, a, b, x, y):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"{self.a}\n{self.b}\n{self.x}\n{self.y}"
        
    def fewest_tokens(self):
        # Consider Pythagorean Theorem to determine the hypotenuse of both
        # buttons movements
        

data = ["Button A: X+94, Y+34",
"Button B: X+22, Y+67",
"Prize: X=8400, Y=5400",
"",
"Button A: X+26, Y+66",
"Button B: X+67, Y+21",
"Prize: X=12748, Y=12176",
"",
"Button A: X+17, Y+86",
"Button B: X+84, Y+37",
"Prize: X=7870, Y=6450",
"",
"Button A: X+69, Y+23",
"Button B: X+27, Y+71",
"Prize: X=18641, Y=10279"]
main(data)
