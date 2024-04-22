import json


class State:
    __counter = 0

    def __init__(self, id: None) -> None:
        if id is None:
            self.id = State._get_next_id()
        else:
            self.id = id
        self.transitions: dict[str, 'State'] = {}

    def add_transition(self, symbol: str, state: 'State') -> None:
        self.transitions[symbol] = state

    @classmethod
    def _get_next_id(cls) -> int:
        current_id = cls.__counter
        cls.__counter += 1
        return current_id


class DFA:
    def __init__(self) -> None:
        self.init_state = None
        self.states: list['State'] = []
        self.alphabet: list['str'] = []
        self.final_states: list['State'] = []

    @staticmethod
    def deserialize_json(json_str: str) -> 'DFA':
        fa = DFA()
        json_fa={}
        with open(json_str) as f:
            json_fa = json.load(f)

        fa.alphabet = json_fa["alphabet"]

        for state_str in json_fa["states"]:
            fa.add_state(int(state_str[2:]))

        fa.init_state = fa.get_state_by_id(json_fa["initial_state"][2:])

        for final_str in json_fa["final_states"]:
            fa.add_final_state(fa.get_state_by_id(final_str[2:]))

        for state_str in json_fa["states"]:
            for symbol in fa.alphabet:
                fa.add_transition(fa.get_state_by_id(state_str[2:]), fa.get_state_by_id(json_fa[state_str][symbol][2:]),
                                    symbol)

        return fa

    def serialize_json(self) -> str:
        fa = {
            "states": list(map(lambda s: f"q_{s.id}", self.states)),
            "initial_state": f"q_{self.init_state.id}",
            "final_states": list(map(lambda s: f"q_{s.id}", self.final_states)),
            "alphabet": self.alphabet
        }

        for state in self.states:
            fa[f"q_{state.id}"] = {}
            for symbol in self.alphabet:
                fa[f"q_{state.id}"][symbol] = f"q_{state.transitions[symbol].id}"

        return json.dumps(fa)

    def add_state(self, id: int | None = None) -> State:
        state = State(id)
        self.states.append(state)
        return state

    def add_transition(self, from_state: State, to_state: State, input_symbol: str) -> None:
        from_state.add_transition(input_symbol, to_state)

    def assign_initial_state(self, state: State) -> None:
        self.init_state = state

    def add_final_state(self, state: State) -> None:
        self.final_states.append(state)

    def get_state_by_id(self, id) -> State | None:
        for state in self.states:
            if state.id == id:
                return state
        return None

    def is_final(self, state: State) -> bool:
        return state in self.final_states
class NFAState:
    __counter = 0

    def __init__(self, id: None) -> None:
        if id is None:
            self.id = NFAState._get_next_id()
        else:
            self.id = id
        self.transitions: dict[str, list['NFAState']] = {}

    def add_transition(self, symbol: str, state: 'NFAState') -> None:
        if symbol not in self.transitions:
            self.transitions[symbol] = []
        self.transitions[symbol].append(state)

    @classmethod
    def _get_next_id(cls) -> int:
        current_id = cls.__counter
        cls.__counter += 1
        return current_id
    
class NFA:
    def __init__(self) -> None:
        self.init_state = None
        self.states: list['NFAState'] = []
        self.alphabet: list['str'] = []
        self.final_states: list['NFAState'] = []

    @staticmethod
    def deserialize_json(json_str: str) -> 'NFA':
        fa = NFA()
        json_fa={}
        with open(json_str) as f:
            json_fa = json.load(f)
        fa.alphabet = json_fa["alphabet"]
        fa.alphabet.append(" ")
        for state_str in json_fa["states"]:
            fa.add_state(int(state_str[2:]))

        fa.init_state = fa.get_state_by_id(int(json_fa["initial_state"][2:]))

        for final_str in json_fa["final_states"]:
            fa.add_final_state(fa.get_state_by_id(int(final_str[2:])))

        for state_str in json_fa["states"]:
            for symbol in fa.alphabet:
                ss=json_fa[state_str].get(symbol)
                if(ss is not None):
                    for to_state_str in ss:
                        fa.add_transition(fa.get_state_by_id(int(state_str[2:])), fa.get_state_by_id(int(to_state_str[2:])),
                                        symbol)
        return fa

    def serialize_to_json(self) -> str:
        fa = {
            "states": list(map(lambda s: f"q_{s.id}", self.states)),
            "initial_state": f"q_{self.init_state.id}",
            "final_states": list(map(lambda s: f"q_{s.id}", self.final_states)),
            "alphabet": self.alphabet
        }

        for state in self.states:
            fa[f"q_{state.id}"] = {symbol: [] for symbol in state.transitions.keys()}

            for symbol in state.transitions.keys():
                for to_state in state.transitions[symbol]:
                    fa[f"q_{state.id}"][symbol].append(f"q_{to_state.id}")

        return json.dumps(fa)

    def add_state(self, id: int | None = None) -> NFAState:
        state = NFAState(id)
        self.states.append(state)
        return state

    def add_transition(self, from_state: NFAState, to_state: NFAState, input_symbol: str) -> None:
        from_state.add_transition(input_symbol, to_state)

    def assign_initial_state(self, state: NFAState) -> None:
        self.init_state = state

    def add_final_state(self, state: NFAState) -> None:
        self.final_states.append(state)

    def get_state_by_id(self, id) -> NFAState | None:
        for state in self.states:
            if state.id == id:
                return state
        return None

    def is_final(self, state: NFAState) -> bool:
        return state in self.final_states

    @staticmethod
    def create_NewMachine(machine1: 'NFA', machine2: 'NFA') -> 'NFA':
        newMachine = NFA()
        newMachine.alphabet.append(" ")

        for state in machine1.states:
            newMachine.add_state(state.id)
        for state in machine2.states:
            newMachine.add_state(state.id)

        for state in machine1.states:
            for alphabet, to_states in state.transitions.items():
                for to_state in to_states:
                    newMachine.add_transition(newMachine.get_state_by_id(
                        state.id), newMachine.get_state_by_id(to_state.id), alphabet)
                if (alphabet in newMachine.alphabet) == False:
                    newMachine.alphabet.append(alphabet)

        for state in machine2.states:
            for alphabet, to_states in state.transitions.items():
                for to_state in to_states:
                    newMachine.add_transition(newMachine.get_state_by_id(
                        state.id), newMachine.get_state_by_id(to_state.id), alphabet)
                if (alphabet in newMachine.alphabet) == False:
                    newMachine.alphabet.append(alphabet)

        return newMachine

    @staticmethod
    def convert_DFA_instanse_to_NFA_instanse(dfa_machine: 'DFA') -> 'NFA':
        newMachine = NFA()
        newMachine.alphabet.append(" ")

        for state in dfa_machine.states:
            newMachine.add_state(state.id)

        for state in dfa_machine.states:
            for alphabet, to_states in state.transitions.items():
                for to_state in to_states:
                    newMachine.add_transition(newMachine.get_state_by_id(
                        state.id), newMachine.get_state_by_id(to_state.id), alphabet)
                if (alphabet in newMachine.alphabet) == False:
                    newMachine.alphabet.append(alphabet)

        return newMachine

    @staticmethod
    def union(machine1: 'NFA', machine2: 'NFA') -> 'NFA':
        newMachine = NFA.create_NewMachine(machine1, machine2)

        newInitState = newMachine.add_state(machine2.final_states[-1].id + 1)

        newMachine.add_transition(newMachine.get_state_by_id(
            newInitState.id), newMachine.get_state_by_id(machine1.init_state.id), " ")
        newMachine.add_transition(newMachine.get_state_by_id(
            newInitState.id), newMachine.get_state_by_id(machine2.init_state.id), " ")

        newMachine.assign_initial_state(
            newMachine.get_state_by_id(newInitState.id))

        for fState_machine1 in machine1.final_states:
            newMachine.add_final_state(
                newMachine.get_state_by_id(fState_machine1.id))

        for fState_machine2 in machine2.final_states:
            newMachine.add_final_state(
                newMachine.get_state_by_id(fState_machine2.id))

        return newMachine

    @staticmethod
    def concat(machine1: 'NFA', machine2: 'NFA') -> 'NFA':
        newMachine = NFA.create_NewMachine(machine1, machine2)

        for fState_machine1 in machine1.final_states:
            newMachine.add_transition(
                newMachine.get_state_by_id(fState_machine1.id), newMachine.get_state_by_id(machine2.init_state.id), " ")

        newMachine.assign_initial_state(
            newMachine.get_state_by_id(machine1.init_state.id))

        for fState_machine2 in machine2.final_states:
            newMachine.add_final_state(
                newMachine.get_state_by_id(fState_machine2.id))

        return newMachine

    @staticmethod
    def star(machine: 'NFA') -> 'NFA':
        for fState in machine.final_states:
            machine.add_transition(fState, machine.init_state, " ")
            machine.add_transition(machine.init_state, fState, " ")
        return machine


# nfa = NFA()
# nfa_alphabet = ['0', '1']
# q0 = nfa.add_state(0)
# q1 = nfa.add_state(1)
# q2 = nfa.add_state(2)
# nfa.alphabet = nfa_alphabet
# nfa.assign_initial_state(q0)
# nfa.add_final_state(q2)
# nfa.add_transition(q0, q1, '0')
# nfa.add_transition(q1, q2, '1')
# print(NFA.star(nfa))

# nfa2 = NFA()
# nfa2_alphabet = ['0', '1']
# q3 = nfa2.add_state(3)
# q4 = nfa2.add_state(4)
# q5 = nfa2.add_state(5)
# nfa2.alphabet = nfa2_alphabet
# nfa2.assign_initial_state(q3)
# nfa2.add_final_state(q5)
# nfa2.add_transition(q3, q4, '0')
# nfa2.add_transition(q4, q5, '1')

# # newNFA = NFA.star(nfa)
# newNFA = NFA.union(nfa, nfa2)
# # newNFA = NFA.concat(nfa, nfa2)
# print(newNFA.init_state.id)
# for fState in newNFA.final_states:
#     print(fState.id)

# for state in newNFA.states:
#     for alphabet, nextStates in state.transitions.items():
#         for nstate in nextStates:
#             print(f"{state.id}-->{alphabet}-->{nstate.id}")


# x=NFA()
# x=x.deserialize_json('json_fa.json')
# x.serialize_to_json()
