class Grammar:
    def __init__(self, N, E, P, S):
        self.N = N  # non_terminals
        self.E = E  # terminals
        self.P = P  # prod rules
        self.S = S  # starting symb

    #     P = {"A": ...}
    '''
    P e un dictionar unde cheia e elementul din stanga al production-ului (lhs), iar valoarea e o lista a elementelor din dreapta [rhs]
    Verificam ca left hand side-ul sa fie un non-terminal, iar fiecare element din rhs sa fie fie terminal, non-terminal sau epsilon.
    '''
    @staticmethod
    def checkValidCFG(N, E, P, S):
        if S not in N:
            print(f"{S} not in nonterminals!")
            return False
        for lhs in P.keys():
            if lhs not in N:
                print(f"{lhs} not in nonterminals!")
                return False
            for rhs in P[lhs]:
                for element in rhs.split(' '):
                    if element not in N and element not in E and element != 'E':
                        print(f"{element} not in N or E or = Epsilon!")
                        return False
        return True

    @staticmethod
    def parseLine(line):
        tokens = line.strip().split('=', 1)
        return [element.strip() for element in tokens[1].strip().split(',')]

    @staticmethod
    def readGrammarFromFile(filename):
        with open(filename, 'r') as file:
            N = Grammar.parseLine(file.readline())
            E = Grammar.parseLine(file.readline())
            S = Grammar.parseLine(file.readline()).pop()
            P = Grammar.parseRules(Grammar.parseLine(''.join([line for line in file])))

            return Grammar(N, E, P, S)

    @staticmethod
    def parseRules(rules):
        result = {}
        index = 1

        for rule in rules:
            # print('parsing rule ' + rule)
            lhs, rhs = rule.split('->')
            lhs = lhs.strip()
            rhs = [value.strip() for value in rhs.strip().split('|')]

            for value in rhs:
                if lhs in result.keys():
                    result[lhs].append(value)
                else:
                    result[lhs] = [value]
                index += 1

        return result
