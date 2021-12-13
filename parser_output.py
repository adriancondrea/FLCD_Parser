import copy

from parser import Parser


class ParserOutput:
    def __init__(self, parser: Parser):
        self.parser = parser

    def getDerivationString(self):
        derivation_list = []
        current_derivation = ['S']
        parser_output = copy.deepcopy(self.parser.working_stack)
        while parser_output:
            symbol = parser_output[0][0]
            if symbol in self.parser.grammar.N:
                derivation_list.append(copy.deepcopy(current_derivation))
                index = current_derivation.index(symbol)
                production = self.parser.grammar.getProduction(parser_output[0])
                current_derivation = current_derivation[:index] + production + current_derivation[index + 1:]
            parser_output.pop(0)

        if current_derivation:
            derivation_list.append(current_derivation)

        resultString = ""
        for production in derivation_list:
            if not resultString:
                resultString = ' '.join(production)
            else:
                resultString = resultString + " -> " + ' '.join(production)

        return resultString
