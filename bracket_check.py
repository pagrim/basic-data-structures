from collections import deque

import logging
import sys

logging.basicConfig()

class BracketChecker:

    def __init__(self, sequence):
        self.sequence = sequence
        self.brackets = {'[': ']', '(': ')', '{': '}'}
        self.stack = deque()
        self.logger = logging.getLogger('bracket_checker')

    def check(self):
        for idx, char in enumerate(self.sequence):
            self.logger.info('Stack: %s, Char: %s', self.stack, char)
            if char in self.brackets.keys():
                self.stack.append((char, idx))
            elif char in self.brackets.values():
                if self.stack and self.brackets[self.stack[-1][0]] == char:
                    self.stack.pop()
                else:
                    self.logger.info('Unmatched closing bracket %s at %s', char, idx)
                    return idx + 1
            else:
                continue

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
