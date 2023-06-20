from numpy import inf
class rald_lard():
    def __init__(self,delimiter = "O",special_character="C",instructions = None,max_steps=inf): 
        self.instructions  = instructions
        self.delimiter=delimiter
        self.special_character = special_character
        self.max_steps = max_steps


    def __repr__(self):
        num_rows = len(self.instructions)
        output_str = ""

        for i in range(num_rows):
            for j in range(3):
                output_str += str(self.instructions[i][j]) + ' '
            output_str += '\n'

        return output_str


    def draw_tape(self,chars,step,input_id,step_text = "Step : " ,input_text = "Input :" ):

        print(f"{step_text} {step}")
        print(f"{input_text} {input_id}")

        # Create the tape
        tape = ""
        for char in chars:
            padding_size = (3 - len(char)) // 2
            padding = " " * padding_size
            if len(char) % 2 == 1:
                padding += " "
            tape += "| " + padding + char + padding + " "
        tape += "|"
        
        # Print the tape
        print(tape)
        print("******************************************")

    # run the model on a list of inputs
    def run(self,inputs,verbose=False):
        outputs = inputs.copy()

        n_steps = 0
        instructions_length = len(self.instructions)

        instruction_id = 0

        while True and n_steps < self.max_steps:
            
            current_instruction = self.instructions[instruction_id]
            instruction_action = current_instruction[0]
            instruction_direction = current_instruction[1]
            targeted_input_id = current_instruction[2]

            # add right
            if instruction_action=='A' and instruction_direction=='R' : 
                outputs[targeted_input_id]+=self.special_character
                n_steps+=1
                if verbose:
                    self.draw_tape(outputs[targeted_input_id],n_steps,targeted_input_id)

            # add left
            elif instruction_action=='A' and instruction_direction=='L' : 
                outputs[targeted_input_id]=self.special_character + outputs[targeted_input_id]
                n_steps+=1
                if verbose:
                    self.draw_tape(outputs[targeted_input_id],n_steps,targeted_input_id)
            
            # delete right
            elif instruction_action=='D' and instruction_direction=='R' :
                if outputs[targeted_input_id].index(self.delimiter) == len(outputs[targeted_input_id])- 1:
                    break
                else:    
                    outputs[targeted_input_id]=outputs[targeted_input_id][:-1]
                    n_steps+=1
                    if verbose:
                        self.draw_tape(outputs[targeted_input_id],n_steps,targeted_input_id)
            
            # delete left
            elif instruction_action=='D' and instruction_direction=='L' : 
                if outputs[targeted_input_id].index(self.delimiter) == 0:
                    break
                else:
                    outputs[targeted_input_id]=outputs[targeted_input_id][1:]
                    n_steps+=1
                    if verbose:
                        self.draw_tape(outputs[targeted_input_id],n_steps,targeted_input_id)

            instruction_id = (instruction_id+1)%instructions_length

        if verbose:
            for output_id,output in enumerate(outputs):
                self.draw_tape(output,n_steps,output_id,step_text="Total number of steps : ",input_text="Output :")
        
        return outputs
