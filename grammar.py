class Grammar:
    def __init__(self, N, E, P, S):
        self.N = N  # non_terminals
        self.E = E  # terminals
        self.P = P  # prod rules
        self.S = S  # starting symb

    #     P = {"A": ...}
    '''
    P is a dictionary where the key is the production's left element (lhs), and the value is the list of elements
    from the right [rhs].
    We verify that the lhs is a non-terminal, and for each element in rhs we check that it is either a terminal, a
    non-terminal, or epsilon.
    '''

    @staticmethod
    def check_valid_cfg(N, E, P, S):
        if S not in N:
            print(f"{S} not in nonterminals!")
            return False
        for lhs in P.keys():
            if lhs not in N:
                print(f"{lhs} not in nonterminals!")
                return False
            for rhs in P[lhs]:
                for element in rhs[0].split(' '):
                    if element not in N and element not in E and element != 'E':
                        print(f"{element} not in N or E or = Epsilon!")
                        return False
        return True

    @staticmethod
    def parse_line(line):
        tokens = line.strip().split('=', 1)
        return [element.strip() for element in tokens[1].strip().split(',')]

    @staticmethod
    def read_grammar_from_file(filename):
        with open(filename, 'r') as file:
            N = Grammar.parse_line(file.readline())
            E = Grammar.parse_line(file.readline())
            S = Grammar.parse_line(file.readline()).pop()
            P = Grammar.parse_rules(Grammar.parse_line(''.join([line for line in file])))

            return Grammar(N, E, P, S)

    @staticmethod
    def parse_rules(rules):
        result = {}

        for rule in rules:
            # print('parsing rule ' + rule)
            lhs, rhs = rule.split('->')
            lhs = lhs.strip()
            rhs = [value.strip() for value in rhs.strip().split('|')]

            for value in rhs:
                if lhs in result.keys():
                    result[lhs].append((value, len(result[lhs]) + 1))
                else:
                    result[lhs] = [(value, 1)]

        return result

    def get_production(self, production):
        symbol = production[0]
        index = production[1] - 1
        return self.P[symbol][index][0].split(' ')
