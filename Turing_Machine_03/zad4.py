class TuringMachine:
    def __init__(self, tape, transition_function, initial_state, final_states, reject_states):
        self.tape = tape
        self.head_position = 0
        self.eks = False
        self.state = initial_state
        self.final_states = final_states
        self.reject_states = reject_states
        self.transition_function = transition_function

    def step(self):
        current_symbol = self.tape[self.head_position]
        new_symbol, direction, new_state = self.transition_function[(self.state, current_symbol)]
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
            self.step()
        if self.state in self.reject_states:
            print('Stan odrzucony\n', ''.join(self.tape))
            return False
        else:
            print('Stan zaakceptowany\n', ''.join(self.tape))
            return True


tape = ['[', '(', 'n', 'n', ',', 'n', 'n', ')', ',', '(', 'n', ',', 'n', ')', '#', 'n', 'n', ',', 'n', 'n', ']'] #accepted
#tape = ['n','(',',','n',')'] #rejected
initial_state = 'q0'
final_states = {'qa'}
reject_states = {'qr'}
transition_function = {
    ('q0', '['): ('[', 'R', 'q1'),
    ('q1', '('): ('(', 'R', 'q2'),
    ('q1', '#'): ('#', 'R', 'q7'),
    ('q2', 'n'): ('n', 'R', 'q3'),
    ('q3', 'n'): ('n', 'R', 'q3'),
    ('q3', ','): (',', 'R', 'q4'),
    ('q4', 'n'): ('n', 'R', 'q5'),
    ('q5', 'n'): ('n', 'R', 'q5'),
    ('q5', ')'): (')', 'R', 'q6'),
    ('q6', '#'): ('#', 'R', 'q7'),
    ('q6', ','): (',', 'R', 'q1'),
    ('q7', 'n'): ('n', 'R', 'q8'),
    ('q8', ','): (',', 'R', 'q7'),
    ('q8', 'n'): ('n', 'R', 'q8'),
    ('q8', ']'): (']', 'R', 'qa')
}
tm = TuringMachine(tape, transition_function, initial_state, final_states, reject_states)
tm.run()