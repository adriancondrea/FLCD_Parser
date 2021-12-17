from grammar import Grammar
from parser import Parser
from parser_output import ParserOutput


def test_grammar():
    g = Grammar.read_grammar_from_file('input/grammars/g2.txt')
    print(f'valid cfg: {Grammar.check_valid_cfg(g.N, g.E, g.P, g.S)}')
    print(f'set of non-terminals is: {g.N}')
    print(f'set of terminals is: {g.E}')
    print('set of production rules is: ')
    for lhs in g.P.keys():
        for rhs in g.P[lhs]:
            print(f'{lhs} -> {rhs}')
    print(f'starting symbol is: {g.S}')
    print(g.P)


def test_parser_methods():
    g = Grammar.read_grammar_from_file('input/grammars/g1.txt')

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


def test_parse(grammar_path, input_sequence_path, output_path):
    g = Grammar.read_grammar_from_file(grammar_path)
    input_sequence = read_from_file(input_sequence_path)

    parser = Parser(g, input_sequence, g.S)
    print(parser)
    parser.parse()
    parser_output = ParserOutput(parser)
    print("Parser output is: ", parser_output.compute_derivation_string())

    parser_output.write_derivation_list_to_file(parser.is_accepted(), output_path)


def read_from_file(filename):
    input_list = []
    with open(filename, 'r') as reader:
        for line in reader:
            input_list.append(line.strip())

    return input_list


if __name__ == '__main__':
    # test_parser_methods()
    # print(read_from_file())
    test_parse('input/grammars/g1.txt', 'input/sequences/seq.txt', 'output/out1.txt')
    test_parse('input/grammars/g2_simplified.txt', 'input/sequences/pif.out', 'output/out2.txt')
