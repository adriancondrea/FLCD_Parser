Statement: Implement a parser algorithm


1. Parsing method: 1.a. recursive descendent


2. The representation of the parsing tree (output) will be (decided by the team):

    2.a. productions string (max grade = 8.5)

    2.b. derivations string (max grade = 9)

    2.c. table (using father and sibling relation) (max grade = 10)



PART 1: Deliverables 

Class Grammar (required operations: read a grammar from file, print set of nonterminals, set of terminals, set of productions, productions for a given nonterminal, CFG check)

Input files: g1.txt (simple grammar from course/seminar), g2.txt (grammar of the minilanguage - syntax rules from Lab 1b)


PART 2: Deliverables

Functions corresponding to the assigned parsing strategy + appropriate tests,  as detailed below:

Recursive Descendent - functions corresponding to moves:
   - expand
   - advance
   - momentary insuccess
   - back
   - another try
   - success