from phase0.FA_class import DFA
from phase1.module1 import solve as ConvertToDFA
from utils import utils
from utils.utils import imageType


def solve(json_str: str, image: imageType) -> bool:
    fa = DFA.deserialize_json(json_str)
    dfa= ConvertToDFA(image)

    totalCounter=0
    accepterCounter=0
    for state in  dfa.states:
        for symbol in  dfa.alphabet:
            if fa.get_state_by_id(state.id)!=None and state.transitions[symbol].id==fa.get_state_by_id(state.id).transitions[symbol].id:
                accepterCounter=accepterCounter+1
            totalCounter=totalCounter+1

    if(accepterCounter==totalCounter): return True
    else: return False
    


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
