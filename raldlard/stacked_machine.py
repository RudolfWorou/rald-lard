class stacked_rarld_lard():
    def __init__(self):
        self.models_adjacency_list = {}
        self.models_list = {}
        self.entry_point = None
        
    def add_model(self, model,model_id)->None:
        if model_id not in self.models_list:
            self.models_adjacency_list[model_id] = None
            self.models_list[model_id] = model
            self.special_character = self.models_list[model_id].special_character
            self.delimiter = self.models_list[model_id].delimiter

    def add_transition(self, model_1_id, model_2_id, transition_instructions):
        if model_1_id in self.models_list and model_2_id in self.models_list:
            self.models_adjacency_list[model_1_id]=(model_2_id, transition_instructions)
    
    def __repr__(self) -> str:
        output_str = ""
        for model_id in self.models_list:
            output_str += f"Model {model_id}------- >: {self.models_adjacency_list[model_id]}\n"
        return output_str
    def set_entry_point(self,model_id):
        self.entry_point = model_id

    def apply_transitions_instructions(self,inputs,instructions):
        outputs = inputs.copy()
        instruction_failed = False
        for current_instruction in instructions:
            instruction_action = current_instruction[0]
            instruction_direction = current_instruction[1]
            targeted_input_id = current_instruction[2]


            # add right
            if instruction_action=='A' and instruction_direction=='R' : 
                outputs[targeted_input_id]+=self.special_character

            # add left
            elif instruction_action=='A' and instruction_direction=='L' : 
                outputs[targeted_input_id]=self.special_character + outputs[targeted_input_id]
            
            # delete right
            elif instruction_action=='D' and instruction_direction=='R' :
                if outputs[targeted_input_id].index(self.delimiter) == len(outputs[targeted_input_id])- 1:
                    instruction_failed = True
                else:    
                    outputs[targeted_input_id]=outputs[targeted_input_id][:-1]
            
            # delete left
            elif instruction_action=='D' and instruction_direction=='L' : 
                if outputs[targeted_input_id].index(self.delimiter) == 0:
                    instruction_failed = True
                else:
                    outputs[targeted_input_id]=outputs[targeted_input_id][1:]
        return outputs,instruction_failed
        
    def run(self,inputs,verbose=False):
        if verbose:
            print(f"Inputs : {inputs}")
            print("----------------------------------------------")
        current_model_id = self.entry_point
        instruction_failed = False
        while not instruction_failed:
            if verbose:
                print(f"Model {current_model_id} runs")
            current_model = self.models_list[current_model_id]
            inputs = current_model.run(inputs,verbose=False)
            if verbose:
                print(inputs)
            ## add instructions
            current_model_id, instructions = self.models_adjacency_list[current_model_id]
            inputs,instruction_failed = self.apply_transitions_instructions(inputs,instructions)
            
        if verbose:
            print("----------------------------------------------")
            print(f"Outputs : {inputs}")
        return inputs