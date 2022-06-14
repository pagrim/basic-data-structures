from collections import deque

import logging
import sys

logging.basicConfig()

class BracketChecker:

    def __init__(self, sequence):
        self.sequence = self.init_sequence(sequence)
        self.opening_brackets = ['[', '(', '{']
        self.closing_brackets = [']', ')', '}']
        self.stack = deque()
        self.logger = logging.getLogger('bracket_checker')

    def init_sequence(self, sequence):
        if isinstance(sequence, str):
            initial = [char for char in sequence]
        elif isinstance(sequence, list):
            initial = sequence
        else:
            raise TypeError
        return initial

    def check(self):
        for idx, char in enumerate(self.sequence):
            self.logger.info('Stack: %s, Char: %s', self.stack, char)
            if char in self.opening_brackets:
                self.stack.append((char, idx))
            elif char in self.closing_brackets:
                if self.stack:
                    last_open_bracket, last_open_bracket_pos = self.stack[-1]
                    self.logger.debug('Top of stack: (%s, %s)', last_open_bracket, last_open_bracket_pos)
                    char_index = self.closing_brackets.index(char)
                    last_open_bracket_idx = self.opening_brackets.index(last_open_bracket)
                    match = char_index == last_open_bracket_idx
                    self.logger.debug('Matched: %s, %s and %s', match, last_open_bracket, char_index)
                else:
                    match = False
                if match:
                    self.stack.pop()
                else:
                    self.logger.info('Unmatched closing bracket character %s at position %s', char, idx)
                    return idx + 1
        if self.stack:
            unmatched_bracket, unmatched_bracket_idx = self.stack[0]
            self.logger.info('First unmatched bracket %s at position %s', unmatched_bracket, unmatched_bracket_idx)
            return unmatched_bracket_idx + 1
        else:
            return "Success"


if __name__ == '__main__':
    text = sys.stdin.readline().rstrip()
    bc = BracketChecker(text)
    print(bc.check())
