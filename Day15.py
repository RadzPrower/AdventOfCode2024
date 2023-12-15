def main(data):
    print(f"The sum of the HASH results is {sum_of_hash(data)}")
    print(f"The focusing power of the lens configuration is {calc_focal_power(data)}.")


def calc_focal_power(data):
    result = 0
    boxes = init_boxes()
    for step in data[0].split(","):
        if "=" in step:
            box = calc_label_hash(step, "=")
            add_lens(boxes, box, step)
            continue
        if "-" in step:
            box = calc_label_hash(step, "-")
            remove_lens(boxes, box, step)
            continue
    for box_num, box in boxes.items():
        for slot_num, focal_length in enumerate(box.values()):
            result += calc_individual_focus(box_num, slot_num, focal_length)
    return result


def calc_individual_focus(box, slot, focal):
    return (box + 1) * (slot + 1) * focal


def init_boxes():
    boxes = {}
    for x in range(256):
        boxes[x] = {}
    return boxes


def calc_label_hash(string, operation):
    current_value = 0
    for char in string.split(operation)[0]:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value


def add_lens(boxes, box, step):
    label, focal_length = step.split("=")
    boxes[box][label] = int(focal_length)


def remove_lens(boxes, box, step):
    label = step.split("-")[0]
    if label in boxes[box]:
        del boxes[box][label]


def sum_of_hash(data):
    result = []
    for step in data[0].split(","):
        result.append(calc_full_hash(step))
    return sum(result)


def calc_full_hash(string):
    current_value = 0
    for char in string:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value
