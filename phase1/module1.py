from phase0.FA_class import DFA, State
from visualization import visualizer
from utils import utils
from utils.utils import imageType
from collections import deque

def solve(image: imageType) -> 'DFA':
    np_array = utils.convert_pictures_to_gray_scale_and_binary_array("temp.png")

    dfa = DFA()
    dfa.alphabet = ['0', '1', '2', '3']
    i = 0
    j = 0
    dfa.add_state(i)
    dfa.assign_initial_state(dfa.get_state_by_id(i))
    
    q = deque()
    q.append(len(np_array))

    while len(q) > 0:
        i=j
        dequed = q.popleft()
        if dequed//4 > 0:
            print(dequed)
            for k in range(0, 4):
                dfa.add_state(j)
                dfa.add_transition(dfa.get_state_by_id(i), dfa.get_state_by_id(j), k)
                j += 1
                q.append(dequed//4)


        # if :
        #     dfa.add_final_state(dfa.get_state_by_id(i))

    return dfa


if __name__ == "__main__":
    image = [[1, 1, 1, 1],
             [1, 0, 1, 0],
             [0, 1, 0, 1],
             [1, 1, 1, 1]]

    utils.save_image(image)
    fa = solve(image)
    # print(fa.serialize_json())
