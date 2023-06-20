from typing import List

def integer_to_rald_lard_input(n:int,direction:str="R",delimiter:str = "O",special_character:str="C") -> str:
    input=f"{delimiter}"
    if direction=="R":
        input = input + n*special_character
    elif direction=="L":
        input = n*special_character + input
    return input

def outputs_to_integers(outputs:List[str],delimiter:str = "O",special_character:str="C"):
    converted_outputs = [None]*len(outputs)
    for i,output in enumerate(outputs):
        if output==delimiter:
            converted_outputs[i] = 0
        elif output[0]==delimiter:
            s = output[1:]
            assert (s.count(s[0]) == len(s))  and (s[0]==special_character)
            converted_outputs[i] = len(s)
        elif output[-1]==delimiter:
            s = output[:-1]
            assert (s.count(s[0]) == len(s))  and (s[0]==special_character)
            converted_outputs[i] = len(s)
    return converted_outputs
      