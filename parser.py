class Parser:
    def __init__(self, grammar, input_string):
        self.grammar = grammar
        self.s = 'q'
        self.i = 1
        self.working_stack = []
        self.input_stack = ["S"]
        self.input_string = input_string

    def expand(self):
        head = self.input_stack[0]
        if head in self.grammar.N:
            self.input_stack.pop()
            self.working_stack.append((head, 1))
            # self.input_stack.insert(0, self.grammar.P[head][0])
            self.input_stack = self.grammar.P[head][0][0].split(' ') + self.input_stack
            # self.input_stack.insert(0, self.grammar.P[head][0][0].split(' '))
        else:
            print('head of input stack is not a nonterminal!')

    def advance(self):
        head = self.input_stack[0]
        if head in self.grammar.E and head == self.input_string[self.i - 1]:
            # self.input_stack = self.input_stack[1:]
            self.input_stack.pop(0)
            self.working_stack.append((head, self.i))
            self.i += 1

    def momentary_insuccess(self):
        pass

    def back(self):
        pass

    def another_try(self):
        pass

    def success(self):
        pass

    def __str__(self):
        return f"({self.s}, {self.i}, {self.working_stack}, {self.input_stack})"
