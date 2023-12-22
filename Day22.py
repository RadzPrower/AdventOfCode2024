def main(data):
    blocks, max_height = generate_blocks(data)
    blocks = drop_blocks(blocks, max_height)
    block_connections(blocks)
    print(f"They could safely disintegrate {check_blocks_alt(blocks, max_height)} blocks.")


def generate_blocks(data):
    blocks = []
    max_height = 0
    for line in data:
        start, end = line.split("~")
        start = tuple([int(i) for i in start.split(",")])
        end = tuple([int(i) for i in end.split(",")])
        blocks.append(Block(line, start, end))
        max_height = max(max_height, start[2], end[2])
    return blocks, max_height


def drop_blocks(blocks, max_height):
    blocks_dropped = True
    while blocks_dropped:
        for z in range(2, max_height + 1):
            for idx, block in enumerate(blocks):
                if block.on_level(z):
                    blocks_dropped = blocks[idx].drop(blocks)
    return blocks


def block_connections(blocks):
    for idx, block in enumerate(blocks):
        blocks[idx].find_supports(blocks)


def check_blocks_alt(blocks, max_height):
    result = 0
    for block in blocks:
        temp_blocks = list(blocks)
        temp_blocks.remove(block)
        dropped_blocks = drop_blocks(temp_blocks, max_height)
        if temp_blocks != dropped_blocks:
            result += 1
    return result


def check_blocks(blocks):
    result = 0
    for block in blocks:
        can_be_removed = True
        for supports in block.supports:
            if len(supports.supported_by) < 2:
                can_be_removed = False
                break
        if can_be_removed:
            result += 1
    return result


class Block:
    def __init__(self, label, start, end):
        self.label = label
        self.cubes = []
        self.supports = []
        self.supported_by = []
        self.calc_cubes(start, end)

    def __str__(self):
        return "".join(str(self.cubes))

    def calc_cubes(self, start, end):
        for x in range(3):
            if start[x] != end[x]:
                for i in range(start[x], end[x] + 1):
                    match x:
                        case 0:
                            self.cubes.append((i, end[1], end[2]))
                        case 1:
                            self.cubes.append((end[0], i, end[2]))
                        case 2:
                            self.cubes.append((end[0], end[1], i))

    def on_level(self, z):
        for cube in self.cubes:
            if z == cube[2]:
                return True

    def drop(self, blocks):
        dropped = False
        for cube in self.cubes:
            temp_cube = (cube[0], cube[1], cube[2] - 1)
            if temp_cube[2] == 0:
                return
            for block in blocks:
                if block != self and temp_cube in block.cubes:
                    return
        for idx, cube in enumerate(self.cubes):
            dropped = True
            self.cubes[idx] = (cube[0], cube[1], cube[2] - 1)
            self.drop(blocks)
        return True

    def find_supports(self, blocks):
        for block in blocks:
            for cube in self.cubes:
                temp_cube_above = (cube[0], cube[1], cube[2] + 1)
                temp_cube_below = (cube[0], cube[1], cube[2] - 1)
                if temp_cube_above in block.cubes:
                    self.supports.append(block)
                if temp_cube_below in block.cubes:
                    self.supported_by.append(block)
