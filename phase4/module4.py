from math import log2
from phase0.FA_class import DFA, State
from phase1.module1 import split_into_fourths
from typing import List
from utils.utils import imageType
import queue

def FindAddresses(json_str: str) -> []:
    fa = DFA.deserialize_json(json_str)
    diction = {}
    for state in fa.states:
        diction[state]=[]
    
    initstate = fa.init_state
    que = queue.Queue()
    que.put(initstate)
    diction[initstate].append('')

    while not que.empty():
        s = que.get()
        if(fa.final_states.__contains__(s)): 
            break
        for value in s.transitions.values():
            for key in s.transitions.keys():
                if s.transitions[key]==value :
                    for prev in diction[s]:
                        if diction[value].__contains__(f"{prev}{key}")==False: 
                            diction[value].append(f"{prev}{key}")
            que.put(value)
    return diction[fa.final_states[0]]



def solve(json_str: str, resolution: int) -> imageType:

    fa = DFA.deserialize_json(json_str)
    base_address =  FindAddresses(json_str)
            
    empty_array = [[0 for _ in range(resolution)] for _ in range(resolution)]

    
    for address in base_address:
        # print(address)
        i0_size=0
        i1_size=resolution-1
        i_n_size=resolution
        
        j0_size=0
        j1_size=resolution-1
        j_n_size=resolution
        
        while(True):
            for char in address:
                # print(char)
                i_n_size//=2
                j_n_size//=2
                if(i1_size==i0_size or j1_size==j0_size):
                    empty_array[i0_size][j0_size]=1
                    #print(f"{i0_size}-->{i1_size}\n{j0_size}-->{j1_size}")
                    break
                else:
                    if char=='0':
                        i0_size+=0
                        i1_size=i0_size+ i_n_size-1
                        
                        j0_size+=0
                        j1_size=j0_size + j_n_size-1
                        
                    elif char=='1':
                        i0_size+=0
                        i1_size=i0_size+ i_n_size-1

                        j0_size+=j_n_size
                        j1_size=j0_size+ j_n_size -1
                        
                    elif char=='2':
                        i0_size+=i_n_size
                        i1_size=i0_size+i_n_size-1
                        
                        j0_size+=0
                        j1_size=j0_size + j_n_size-1
                        
                    elif char=='3':
                        i0_size+=i_n_size
                        i1_size=i0_size+i_n_size-1
                        
                        j0_size+=j_n_size
                        j1_size=j0_size+ j_n_size-1
                        
                        

                # print(f"{i_n_size}--{j_n_size}")
            # print(empty_array)
                # print(f"{i0_size}-->{i1_size}\n{j0_size}-->{j1_size}")
                # print(f"{i0_size}-->{i1_size}\n{j0_size}-->{j1_size}")
                
            if(i1_size==i0_size or j1_size==j0_size):
                empty_array[i0_size][j0_size]=1
                break
            # empty_array[i0_size][j0_size]=1
            # break



    # print(empty_array)    
    return empty_array

if __name__ == "__main__":
    pic_arr = solve(
        '{"states": ["q_0", "q_1", "q_2", "q_3", "q_4"], "initial_state": "q_0", "final_states": ["q_3"], '
        '"alphabet": ["0", "1", "2", "3"], "q_0": {"0": "q_1", "1": "q_1", "2": "q_2", "3": "q_2"}, "q_1": {"0": '
        '"q_3", "1": "q_3", "2": "q_3", "3": "q_4"}, "q_2": {"0": "q_4", "1": "q_3", "2": "q_3", "3": "q_3"}, '
        '"q_3": {"0": "q_3", "1": "q_3", "2": "q_3", "3": "q_3"}, "q_4": {"0": "q_4", "1": "q_4", "2": "q_4", '
        '"3": "q_4"}}',
        4
    )
    # print(pic_arr)
