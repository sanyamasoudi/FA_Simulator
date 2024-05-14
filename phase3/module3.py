from utils.utils import imageType
from phase0.FA_class import DFA
from phase2.module2 import solve_2 as CompareDfaImage
from phase1.module1 import solve as ConvertToDFA

def Compare(json_str: str, image: imageType) -> int:
    fa = DFA.deserialize_json(json_str)
    dfa= ConvertToDFA(image)
    totalCounter=0
    accepterCounter=0
    for state in  dfa.states:
        for symbol in  dfa.alphabet:
            if fa.get_state_by_id(state.id)!=None and state.transitions[symbol].id==fa.get_state_by_id(state.id).transitions[symbol].id:
                accepterCounter=accepterCounter+1
            totalCounter=totalCounter+1
    return (accepterCounter/totalCounter )* 100

def solve(json_fa_list: list[str], images: list[imageType]) -> list[int]:
    def compare_dfa_image(json_fa: str, image: imageType) -> float:
        compareResult=0
        if(CompareDfaImage(json_fa,image)==False):
            compareResult=Compare(json_fa,image)
        else:
            compareResult=100
        
        return compareResult

    best_matches = []
    for image in images:
        best_match_index = -1
        best_similarity_score = 0.0

        for idx, json_fa in enumerate(json_fa_list):
            similarity_score = compare_dfa_image(json_fa, image)
            if similarity_score > best_similarity_score:
                best_similarity_score = similarity_score
                best_match_index = idx

        best_matches.append(best_match_index)

    return best_matches


if __name__ == "__main__":
    CompareDfaImage(
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
