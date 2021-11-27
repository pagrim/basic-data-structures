from stack import Stack

class BracketChecker:

    def __init__(self, sequence):
        self.sequence = self.init_sequence(sequence)
        self.opening_brackets = ['[', '(', '{']
        self.closing_brackets = [']', ')', '}']

    def init_sequence(self, sequence):
        if isinstance(sequence, str):
            initial = [char for char in sequence]
        elif isinstance(sequence, list):
            initial = sequence
        else:
            raise TypeError
        return initial

    def check(self):
        stack = Stack()
        for idx, char in enumerate(self.sequence):
            print('Stack:', stack)
            print('Char:', char)
            if char in self.opening_brackets:
                stack.push((char, idx))
            elif char in self.closing_brackets:
                last_open_bracket, last_open_bracket_pos = stack.top()
                print('Topped from stack:', last_open_bracket, last_open_bracket_pos)
                char_index = self.closing_brackets.index(char)
                last_open_bracket_idx = self.opening_brackets.index(last_open_bracket)
                match = char_index == last_open_bracket_idx 
                print('Matched:', match, last_open_bracket, char_index)
                if match:
                    stack.pop()
                else:
                    print('Unmatched closing bracket character', char, 'at position', idx)
                    return idx
        if not stack.is_empty():
            unmatched_braket, unmatched_bracket_idx = stack.top_left()
            print('First unmatched bracket', unmatched_braket, 'at position', unmatched_bracket_idx)
            return unmatched_bracket_idx
        else:
            print('Success')
            return "success"
