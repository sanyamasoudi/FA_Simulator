from phase0.FA_class import DFA
from phase1.module1 import solve as ConvertToDFA
from phase4.module4 import FindAddresses as FindAddresses
from utils import utils
from utils.utils import imageType

def compare_transitions(dfa1, dfa2):
    for state in dfa1.states:
        for symbol in dfa1.alphabet:
            if dfa1.get_state_by_id(state.id) is not None:
                if dfa1.get_state_by_id(state.id).transitions[symbol].id != dfa2.get_state_by_id(state.id).transitions[symbol].id:
                    return False
    return True

def solve_2(json_str: str, image: imageType) -> bool:
    fa = DFA.deserialize_json(json_str)
    dfa = ConvertToDFA(image)
    return compare_transitions(fa, dfa)


def solve(json_str: str, image: imageType) -> bool:
    fa = DFA.deserialize_json(json_str)

    image_dfa = ConvertToDFA(image)
    image_str = DFA.serialize_json(image_dfa)
    address=FindAddresses(image_str)
    for item in address:
        if(item!=None):
            input_string=item
            current_state = fa.init_state
            for symbol in input_string:
                if symbol not in fa.alphabet:
                    return False
                current_state = current_state.transitions[symbol]
            if  fa.is_final(current_state)==False: return False

    return True




if __name__ == "__main__":
    print(
        solve(
            '{"states": ["q_0", "q_1", "q_2", "q_3", "q_4"], "initial_state": "q_0", "final_states": ["q_3"], '
            '"alphabet": ["0", "1", "2", "3"], "q_0": {"0": "q_1", "1": "q_1", "2": "q_2", "3": "q_2"}, "q_1": {"0": '
            '"q_3", "1": "q_3", "2": "q_3", "3": "q_4"}, "q_2": {"0": "q_4", "1": "q_3", "2": "q_3", "3": "q_3"}, '
            '"q_3": {"0": "q_3", "1": "q_3", "2": "q_3", "3": "q_3"}, "q_4": {"0": "q_4", "1": "q_4", "2": "q_4", '
            '"3": "q_4"}}',
            [[1, 1, 1, 1],
             [1, 0, 1, 0],
             [0, 1, 0, 1],
             [1, 1, 1, 1]]
        )
    )
