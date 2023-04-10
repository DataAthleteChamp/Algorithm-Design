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
        new_symbol, direction, new_state = self.transition_function[(self.state, current_symbol)]
        if new_symbol != 'x':
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
            print('Rejected')
        else:
            print('Accepted')


tape = ['b', ' '] #accepted
#tape = ['0','1','b','1'] #rejected
initial_state = 'q0'
final_states = {'qa'}
reject_states = {'qr'}
# x - brak nowego symbolu
transition_function = {
    ('q0', 'b'): ('x', 'R', 'q1'),
    ('q0', '0'): ('0/', 'R', 'q2'),
    ('q0', '1'): ('1/', 'R', 'q3'),
    ('q1', '0/'): ('x', 'R', 'q1'),
    ('q1', '1/'): ('x', 'R', 'q1'),
    ('q1', ' '): ('x', 'L', 'qa'),
    ('q1', '1'): ('x', 'L', 'qr'),
    ('q1', '0'): ('x', 'L', 'qr'),
    ('q2', ' '): ('x', 'R', 'qr'),
    ('q2', 'b'): ('x', 'R', 'q4'),
    ('q2', '0'): ('x', 'R', 'q2'),
    ('q2', '1'): ('x', 'R', 'q2'),
    ('q3', ' '): ('x', 'R', 'qr'),
    ('q3', 'b'): ('x', 'R', 'q5'),
    ('q3', '0'): ('x', 'R', 'q3'),
    ('q3', '1'): ('x', 'R', 'q3'),
    ('q4', '0/'): ('x', 'R', 'q4'),
    ('q4', '1/'): ('x', 'R', 'q4'),
    ('q4', ' '): ('x', 'R', 'qr'),
    ('q4', '1'): ('x', 'R', 'qr'),
    ('q4', '0'): ('0/', 'L', 'q6'),
    ('q5', '0/'): ('x', 'R', 'q5'),
    ('q5', '1/'): ('x', 'R', 'q5'),
    ('q5', ' '): ('x', 'R', 'qr'),
    ('q5', '0'): ('x', 'R', 'qr'),
    ('q5', '1'): ('1/', 'L', 'q6'),
    ('q6', 'b'): ('x', 'L', 'q7'),
    ('q6', '0/'): ('x', 'L', 'q6'),
    ('q6', '1/'): ('x', 'L', 'q6'),
    ('q7', '0'): ('x', 'L', 'q7'),
    ('q7', '1'): ('x', 'L', 'q7'),
    ('q7', '0/'): ('x', 'R', 'q0'),
    ('q7', '1/'): ('x', 'R', 'q0')
}
tm = TuringMachine(tape, initial_state, transition_function, final_states, reject_states)
tm.run()
