from grammar import Grammar

if __name__ == '__main__':
    g = Grammar.readGrammarFromFile('g1.txt')
    print(f'valid cfg: {Grammar.checkValidCFG(g.N, g.E, g.P, g.S)}')
    print(f'set of non-terminals is: {g.N}')
    print(f'set of terminals is: {g.E}')
    print('set of product rules is: ')
    for key in g.P.keys():
        for element in g.P[key]:
            print(f'{key} -> {element[0]}')
    print(f'starting symbol is: {g.S}')
    print(g.P)
