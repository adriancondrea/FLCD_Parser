from grammar import Grammar
from parser import Parser
from parser_output import ParserOutput


def test_grammar():
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


def test_parser_methods():
    g = Grammar.readGrammarFromFile('g1.txt')

    print("test expand: ")
    parser = Parser(g, ['a', 'b', 'a', 'c'])
    print(parser)
    parser.expand()
    print(parser, "\n")

    print("test advance: ")
    print(parser)
    parser.advance()
    print(parser, "\n")

    print("test back: ")
    print(parser)
    parser.back()
    print(parser, "\n")

    print("test momentary insuccess: ")
    parser = Parser(g, ["b"])
    print(parser)
    parser.momentary_insuccess()
    print(parser, "\n")

    print('test success: ')
    parser = Parser(g, ['c'])
    print(parser)
    parser.expand()
    print(parser)
    parser.another_try()
    print(parser)
    parser.another_try()
    print(parser)
    parser.advance()
    print(parser)
    parser.success()
    print(parser, '\n')

    print('test another try: ')
    parser = Parser(g, ['c'])
    print(parser)
    parser.expand()
    print(parser)
    parser.another_try()
    print(parser)
    parser.another_try()
    print(parser)
    parser.another_try()
    print(parser, '\n')


def test_parse():
    g = Grammar.readGrammarFromFile('g2_simplified.txt')
    g2_input = read_from_file('pif2.out')
    parser = Parser(g, g2_input, g.S)
    print(parser)
    parser.parse()
    parser_output = ParserOutput(parser)
    print("Parser output is: ", parser_output.getDerivationString())


if __name__ == '__main__':
    # test_parser_methods()
    test_parse()
