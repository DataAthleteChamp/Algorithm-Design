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
        print(self.tape, self.head_position, self.state)

    def run(self):
        while self.state not in self.final_states and self.state not in self.reject_states:
            self.step()
        if self.state in self.reject_states:
            print('Rejected')
        else:
            print('Accepted')

tape = ['a', ' '] #accepted
#tape = [ ' ', ' ', ' ', 'a.',' ','a/', 'a/', 'a.', 'a.',' ','a/'] #rejected
#tape = ['a', 'a', 'a'] #accepted
initial_state = 'q0'
final_states = {'qa'}
reject_states = {'qr'}
# x - brak nowego symbolu
transition_function = {
    ('q0', ' '): ('x', 'L', 'qr'),
    ('q0', 'a'): ('a.', 'R', 'q1'),
    ('q1', 'a/'): ('x', 'R', 'q1'),
    ('q1', ' '): ('x', 'L', 'qa'),
    ('q1', 'a'): ('x', 'L', 'q2'),
    ('q2', 'a/'): ('x', 'L', 'q2'),
    ('q2', 'a.'): ('x', 'L', 'q3'),
    ('q3', 'a/'): ('x', 'R', 'q3'),
    ('q3', 'a'): ('x', 'R', 'q4'),
    ('q3', 'a.'): ('x', 'R', 'q4'),
    ('q3', ' '): ('x', 'L', 'q6'),
    ('q4', ' '): ('x', 'L', 'qr'),
    ('q4', 'a/'): ('x', 'R', 'q4'),
    ('q4', 'a'): ('a/', 'R', 'q5'),
    ('q5', 'a/'): ('x', 'R', 'q5'),
    ('q5', ' '): ('x', 'L', 'qr'),
    ('q5', 'a'): ('a/', 'R', 'q3'),
    ('q6', 'a'): ('x', 'L', 'q6'),
    ('q6', 'a/'): ('x', 'L', 'q6'),
    ('q6', 'a.'): ('x', 'R', 'q1')
}
tm = TuringMachine(tape, initial_state, transition_function, final_states, reject_states)
tm.run()
