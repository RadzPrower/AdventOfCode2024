import copy
import numpy as np


def main(data):
    disk_map = convert_data_to_disk_map(data)
    max_compressed_disk_map = compact_data_disk(copy.copy(disk_map))
    compressed_disk_map = unfragmented_compacting(copy.copy(disk_map))
    result = ("The checksum of the newly compressed data disk is " +
              str(calculate_checksum(max_compressed_disk_map)) + ".")
    result += ("\nThe checksum of the newly compressed data disk \n" +
               "(without fragmentation) is " + str(calculate_checksum(compressed_disk_map)) + ".")
    return result


def convert_data_to_disk_map(data):
    disk_map = []
    file_index = 0
    data = data[0]
    for i in range(len(data)):
        if i % 2 == 0:
            disk_map.extend([file_index] * int(data[i]))
            file_index += 1
        else: disk_map.extend(["."] * int(data[i]))
    return disk_map


def compact_data_disk(disk_map):
    left_index = find_leftmost_empty_block(disk_map, 0)
    for i in reversed(range(left_index, len(disk_map))):
        if left_index >= i: break
        if disk_map[i] != ".":
            disk_map[left_index], disk_map[i] = disk_map[i], disk_map[left_index]
            left_index = find_leftmost_empty_block(disk_map, left_index)
    return disk_map


def unfragmented_compacting(disk_map):
    np_disk_map = np.array(disk_map)
    file_id_list = np.sort(np.array(np.delete(np.unique(np_disk_map), 0), dtype=np.dtype('i')))
    for i in reversed(file_id_list):
        file_blocks = np.where(np_disk_map == str(i))
        memory_chunk = ["."] * len(file_blocks[0])
        open_memory = find_empty_blocks(disk_map, memory_chunk)
        block_start = file_blocks[0][0]
        if block_start > open_memory > 0:
            block_end = file_blocks[0][-1] + 1
            memory_end = open_memory + len(memory_chunk)
            disk_map[block_start:block_end], disk_map[open_memory:memory_end] = \
                disk_map[open_memory:memory_end], disk_map[block_start:block_end]
            np_disk_map = np.array(disk_map)
    return disk_map


def find_leftmost_empty_block(disk_map, index):
    return disk_map.index(".", index)


def calculate_checksum(data_disk):
    checksum = 0
    for idx, block in enumerate(data_disk):
        if block == ".": continue
        checksum += idx * block
    return checksum


def find_empty_blocks(disk_map, memory_block):
    block_start = -1
    for i in range(disk_map.index("."), len(disk_map)):
        if disk_map[i:i + len(memory_block)] == memory_block:
            block_start = i
            break
    return block_start