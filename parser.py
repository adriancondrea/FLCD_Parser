class Parser:
    def __init__(self, grammar, input_string):
        self.grammar = grammar
        self.s = 'q'
        self.i = 1
        self.working_stack = []
        self.input_stack = ["S"]
        self.input_string = input_string
        self.input_string_initial_length = len(input_string)

    def expand(self):
        print("expand")
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
        print("advance")
        head = self.input_stack[0]
        if head in self.grammar.E and head == self.input_string[self.i - 1]:
            # self.input_stack = self.input_stack[1:]
            self.input_stack.pop(0)
            self.working_stack.append((head, self.i))
            self.i += 1
        else:
            print("Can not perform advance!")

    def momentary_insuccess(self):
        head = self.input_stack[0]
        if not (head in self.grammar.E and head == self.input_string[self.i - 1]):
            print("momentary insuccess")
            self.s = "b"

    def back(self):
        head = self.working_stack[-1][0]
        if head in self.grammar.E:
            print("back")
            self.i = self.i - 1
            self.input_stack = [head] + self.input_stack
            self.working_stack.pop()

    def another_try(self):
        head, production_index = self.working_stack[-1]

        if head in self.grammar.N:
            print('another try')
            productionRules = self.grammar.P[head]
            # if len(productionRules) <= production_index:
            #     print('no other productions left!')
            #     return
            next_production = []
            current_production = []

            for production in productionRules:
                if production[1] == production_index:
                    current_production = production[0].split(' ')
                elif production[1] == production_index + 1:
                    next_production = production[0].split(' ')

            if not current_production:
                print('current production not found!')
                return

            while current_production:
                current_production.pop(0)
                self.input_stack.pop(0)

            if not next_production:
                if self.i == 1 and head == 'S':
                    print('S is the first symbol, and no more productions found. Error state!')
                    self.s = 'e'
                    return
                self.s = 'b'
                nonterminal = self.working_stack.pop()
                self.input_stack = [nonterminal[0]] + self.input_stack
                return

            self.working_stack[-1] = (head, production_index + 1)
            self.input_stack = next_production + self.input_stack

    def success(self):
        if self.s == 'q' and self.i == self.input_string_initial_length + 1 and len(self.input_stack) == 0:
            print('success')
            self.s = 'f'

    def __str__(self):
        return f"({self.s}, {self.i}, {self.working_stack}, {self.input_stack})"
