from grammar import Grammar

if __name__ == '__main__':
    g = Grammar.readGrammarFromFile('g2.txt')
    print(f'valid cfg: {Grammar.checkValidCFG(g.N, g.E, g.P, g.S)}')
    print(f'set of non-terminals is: {g.N}')
    print(f'set of terminals is: {g.E}')
    print('set of production rules is: ')
    for lhs in g.P.keys():
        for rhs in g.P[lhs]:
            print(f'{lhs} -> {rhs}')
    print(f'starting symbol is: {g.S}')
    print(g.P)
