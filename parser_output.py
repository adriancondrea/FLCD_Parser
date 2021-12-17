import copy

from parser import Parser


class ParserOutput:
    def __init__(self, parser: Parser):
        self.parser = parser
        self.derivation_list = []

    def compute_derivation_string(self):
        self.derivation_list = []
        current_derivation = [self.parser.grammar.S]
        parser_output = copy.deepcopy(self.parser.working_stack)
        while parser_output:
            symbol = parser_output[0][0]
            if symbol in self.parser.grammar.N:
                self.derivation_list.append(copy.deepcopy(current_derivation))
                index = current_derivation.index(symbol)
                production = self.parser.grammar.get_production(parser_output[0])
                current_derivation = current_derivation[:index] + production + current_derivation[index + 1:]
            parser_output.pop(0)

        if current_derivation:
            self.derivation_list.append(current_derivation)

        resultString = ""
        for production in self.derivation_list:
            if not resultString:
                resultString = ' '.join(production)
            else:
                resultString = resultString + " -> " + ' '.join(production)

        return resultString

    def write_derivation_list_to_file(self, is_accepted, filename='output.txt'):
        if len(self.derivation_list) > 0:
            with open(filename, "w") as myfile:
                for production in self.derivation_list[:-1]:
                    myfile.write(' '.join(production) + " ->\n")
                myfile.write(' '.join(self.derivation_list[-1]))
                myfile.write('\nis accepted: ' + str(is_accepted))

