from phase0.FA_class import DFA
from phase1.module1 import solve as ConvertToDFA
from utils import utils
from utils.utils import imageType

def compare_transitions(dfa1, dfa2):
    for state in dfa1.states:
        for symbol in dfa1.alphabet:
            if dfa1.get_state_by_id(state.id) is not None:
                if dfa1.get_state_by_id(state.id).transitions[symbol].id != dfa2.get_state_by_id(state.id).transitions[symbol].id:
                    return False
    return True

def solve(json_str: str, image: imageType) -> bool:
    fa = DFA.deserialize_json(json_str)
    dfa = ConvertToDFA(image)

    return compare_transitions(fa, dfa)


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
