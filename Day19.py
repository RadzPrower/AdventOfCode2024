def main(data):
    global workflows
    part_list, workflow_list = parse_data(data)
    workflows = generate_workflows(workflow_list)
    result = assess_parts(part_list)
    print(f"The sum of the rating numbers of accepted parts is {sum(result)}")


def parse_data(data):
    parts = []
    workflows = []
    empty_line = False
    for line in data:
        if not line:
            empty_line = True
            continue
        if empty_line:
            parts.append(Part(line.replace("{", "").replace("}", "")))
        else:
            workflows.append(line)
    return parts, workflows


def generate_workflows(workflow_list):
    workflows = []
    for line in workflow_list:
        workflows.append(Workflow(line))
    return workflows


def assess_parts(part_list):
    result = []
    for part in part_list:
        workflow = get_next_workflow("in")
        if workflow.assess_part(part):
            result.append(part.calc_rating())
    return result


def get_next_workflow(label):
    return [x for x in workflows if x.label == label][0]


class Part:
    def __init__(self, part_nums):
        for value in part_nums.split(","):
            if "x" in value:
                self.x = int(value.split("=")[1])
            elif "m" in value:
                self.m = int(value.split("=")[1])
            elif "a" in value:
                self.a = int(value.split("=")[1])
            else:
                self.s = int(value.split("=")[1])

    def __str__(self):
        return f"x={self.x}, m={self.m}, a={self.a}, s={self.s}"

    def calc_rating(self):
        return self.x + self.m + self.a + self.s


class Workflow:
    workflow = []

    def __init__(self, workflow):
        workflow = workflow[:-1]
        self.label, movements = workflow.split("{")
        self.workflow = movements.split(",")

    def __str__(self):
        return f"{self.label}"

    def assess_part(self, part):
        for movement in self.workflow:
            if "<" in movement:
                temp, action = movement.split(":")
                category, value = temp.split("<")
                value = int(value)
                match category:
                    case "x":
                        if part.x < value:
                            return self.next_action(action, part)
                    case "m":
                        if part.m < value:
                            return self.next_action(action, part)
                    case "a":
                        if part.a < value:
                            return self.next_action(action, part)
                    case "s":
                        if part.s < value:
                            return self.next_action(action, part)
            elif ">" in movement:
                temp, action = movement.split(":")
                category, value = temp.split(">")
                value = int(value)
                match category:
                    case "x":
                        if part.x > value:
                            return self.next_action(action, part)
                    case "m":
                        if part.m > value:
                            return self.next_action(action, part)
                    case "a":
                        if part.a > value:
                            return self.next_action(action, part)
                    case "s":
                        if part.s > value:
                            return self.next_action(action, part)
            else:
                return self.next_action(movement, part)

    def next_action(self, action, part):
        match action:
            case "A":
                return True
            case "R":
                return False
            case _:
                next_workflow = get_next_workflow(action)
                return next_workflow.assess_part(part)
