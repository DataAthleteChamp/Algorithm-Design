class TuringMachine:
    def __init__(self, alphabet, states, transitions, start_state, accept_state, reject_state):
        self.alphabet = alphabet
        self.states = states
        self.transitions = transitions
        self.start_state = start_state
        self.accept_state = accept_state
        self.reject_state = reject_state
        self.current_state = start_state
        self.head_position = 0

    def run(self, tape):
        while self.current_state != self.accept_state and self.current_state != self.reject_state:
            current_symbol = tape[self.head_position]
            transition_key = (self.current_state, current_symbol)
            if transition_key in self.transitions:
                next_state, next_symbol, move = self.transitions[transition_key]
                tape[self.head_position] = next_symbol
                self.current_state = next_state
                self.head_position += 1 if move == 'R' else -1
            else:
                break

        return self.current_state == self.accept_state


def create_language_A_machine():
    alphabet = {'a', 'b', 'x', ' '}
    states = {'q0', 'q1', 'q2', 'qa', 'qr'}
    transitions = {
        ('q0', 'a'): ('q1', 'b', 'R'),
        ('q0', 'b'): ('q0', ' ', 'L'),
        ('q0', 'x'): ('qr', ' ', 'R'),
        ('q1', 'a'): ('q2', ' ', 'R'),
        ('q1', 'b'): ('q1', ' ', 'L'),
        ('q1', 'x'): ('qr', ' ', 'R'),
        ('q2', 'a'): ('qa', ' ', 'R'),
        ('q2', 'b'): ('qa', ' ', 'R'),
        ('q2', 'x'): ('q1', ' ', 'L')
    }
    start_state = 'q0'
    accept_state = 'qa'
    reject_state = 'qr'

    return TuringMachine(alphabet, states, transitions, start_state, accept_state, reject_state)


def test_language_A_machine(tape):
    tm = create_language_A_machine()
    tape = list(tape)
    result = tm.run(tape)
    return result


if __name__ == "__main__":
    #test_case = 'aabx' #true
    test_case = 'aabxa' #true
    #test_case = 'baax' #false
    result = test_language_A_machine(test_case)
    print(f"Result for input {test_case}: {result}")