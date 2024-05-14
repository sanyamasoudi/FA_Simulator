from math import log2
from phase0.FA_class import DFA, State
from typing import List
from utils.utils import imageType
import queue


def map_to_string(i, j, resolution):
    map_str = ''
    while resolution > 1:
        part_height = resolution // 2
        part_width = resolution // 2
        if i < part_height and j < part_width:
            map_str = '0' + map_str
        elif i < part_height and j >= part_width:
            map_str = '1' + map_str
        elif i >= part_height and j < part_width:
            map_str = '2' + map_str
        else:
            map_str = '3' + map_str

        i %= part_height
        j %= part_width
        resolution //= 2
    ans=''
    for i in range(len(map_str)):
        ans += map_str[len(map_str)-i-1]
    return ans

def solve(json_str: str, resolution: int) -> imageType:
    fa = DFA.deserialize_json(json_str)
    image_array = [[0 for _ in range(resolution)] for _ in range(resolution)]
    

    for i in range(resolution):
        for j in range(resolution):
            mapped_string = map_to_string(i, j, resolution)
            final_state = fa.process_input(mapped_string)
            image_array[i][j] = 1 if final_state in fa.final_states else 0
    
    return image_array


def process_input(self, input_string: str) -> State:
    current_state = self.init_state
    for symbol in input_string:
        current_state = current_state.transitions.get(symbol)
        if current_state is None:
            break
    return current_state


DFA.process_input = process_input



if __name__ == "__main__":
    pic_arr = solve(
        '{"states": ["q_0", "q_1", "q_2", "q_3", "q_4"], "initial_state": "q_0", "final_states": ["q_3"], '
        '"alphabet": ["0", "1", "2", "3"], "q_0": {"0": "q_1", "1": "q_1", "2": "q_2", "3": "q_2"}, "q_1": {"0": '
        '"q_3", "1": "q_3", "2": "q_3", "3": "q_4"}, "q_2": {"0": "q_4", "1": "q_3", "2": "q_3", "3": "q_3"}, '
        '"q_3": {"0": "q_3", "1": "q_3", "2": "q_3", "3": "q_3"}, "q_4": {"0": "q_4", "1": "q_4", "2": "q_4", '
        '"3": "q_4"}}',
        4
    )
    print(pic_arr)
