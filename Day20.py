def main(data):
    modules = create_modules(data)
    map_inputs(data, modules)
    low_pulses, high_pulses = press_button(modules, 1000)
    print(f"The total number of pulses sent was {low_pulses * high_pulses}.")


def create_modules(data):
    result = {}
    for line in data:
        label, outputs = line.split(" -> ")
        if label == "broadcaster":
            result[label] = Broadcaster()
        if "%" in label:
            label = label[1:]
            result[label] = FlipFlop(label)
        if "&" in label:
            label = label[1:]
            result[label] = Conjunction(label)
        for output in outputs.split(", "):
            result[label].add_output(output)
    return result


def map_inputs(data, modules):
    for line in data:
        label, inputs = line.split(" -> ")
        label = label.replace("%", "").replace("&", "")
        for input in inputs.split(", "):
            if input in modules.keys() and isinstance(modules[input], Conjunction):
                modules[input].add_input(label)


def press_button(modules, count):
    low_pulse = 0
    high_pulse = 0
    for x in range(count):
        fifo_outputs = []
        low_pulse += 1 # button press
        pulse, new_destinations = modules["broadcaster"].process_pulse(False)
        fifo_outputs = process_results(pulse, "broadcaster", new_destinations, fifo_outputs)
        for output in fifo_outputs:
            origin, pulse, destination = output
            if destination not in modules.keys():
                continue
            pulse, new_destinations = modules[destination].process_pulse(pulse, origin)
            if pulse is None:
                continue
            fifo_outputs = process_results(pulse, destination, new_destinations, fifo_outputs)
        for output in fifo_outputs:
            if output[1]:
                high_pulse += 1
            else:
                low_pulse += 1
    return low_pulse, high_pulse


def process_results(pulse, origin, destinations, fifo_outputs):
    high_pulse = 0
    low_pulse = 0
    for destination in destinations:
        fifo_outputs.append((origin, pulse, destination))
    if pulse:
        high_pulse += len(destinations)
    else:
        low_pulse += len(destinations)
    return fifo_outputs


class FlipFlop:
    def __init__(self, label):
        self.label = label
        self.on = False
        self.outputs = []

    def process_pulse(self, pulse, input=None):
        if pulse:
            return None, []
        self.on = not self.on
        return self.on, self.outputs

    def add_output(self, output):
        self.outputs.append(output)


class Conjunction:
    def __init__(self, label):
        self.label = label
        self.inputs = {}
        self.outputs = []

    def process_pulse(self, pulse, input):
        self.inputs[input] = pulse
        if False not in self.inputs.values():
            return False, self.outputs
        return True, self.outputs

    def add_input(self, input):
        self.inputs[input] = False

    def add_output(self, output):
        self.outputs.append(output)


class Broadcaster:
    def __init__(self):
        self.label = "broadcaster"
        self.outputs = []

    def process_pulse(self, pulse, input=None):
        return pulse, self.outputs

    def add_output(self, output):
        self.outputs.append(output)
