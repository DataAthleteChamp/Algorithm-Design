import json

class TuringMachine:
    def __init__(self, tape, initial_state, transition_function, final_states, reject_states):
        self.tape = tape
        self.transition_function = transition_function
        self.final_states = final_states
        self.head_position = 0
        self.state = initial_state
        self.reject_states = reject_states

    def step(self):
        current_symbol = self.tape[self.head_position]
        new_symbol = None
        direction = None
        new_state = None
        for t in self.transition_function:
            if t['current_state'] == self.state and t['symbol'] == current_symbol:
                new_symbol = t['write_symbol']
                direction = t['move']
                new_state = t['next_state']
                print(new_symbol, direction, new_state)
                break
            elif t == self.transition_function[-1]:
                print('Error')
                return 0

        self.tape[self.head_position] = new_symbol
        self.state = new_state
        if direction == 'R':
            self.head_position += 1
            if self.head_position == len(self.tape):
                self.tape.append(' ')
        elif direction == 'L':
            self.head_position -= 1
            if self.head_position == -1:
                self.head_position = 0

    def run(self):
        while self.state not in self.final_states and self.state not in self.reject_states:
            # print(self.tape, self.head_position, self.state)
            self.step()
        if self.state in self.reject_states:
            print('Rejected')
        else:
            print('Accepted')


# tape = ['a', 'a', 'x', 'b', 'b']
tape = ['1', '0', '1', '1', '0', '1']

with open('zadanie5.json') as f:
    data = json.load(f)

initial_state = data['initial_state']
final_states = data['accept_states']
reject_states = data['reject_states']
transition_function = data['transitions']
#print(transition_function)

tm = TuringMachine(tape, initial_state, transition_function, final_states, reject_states)
tm.run()
