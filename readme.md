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

PART 3: Deliverables

1. Algorithms corresponding to parsing table (if needed) and parsing strategy

2. Class ParserOutput - DS and operations corresponding to choice 2.a/2.b/2.c (Lab 5) (required operations: transform parsing tree into representation; print DS to screen and to file)

Remark: If the table contains conflicts, you will be helped to solve them. It is important to print a message containing row (symbol in LL(1), respectively state in LR(0)) and column (symbol) where the conflict appears. For LL(1), values (α,i) might also help.

Statement: Implement a parser algorithm (final tests)

Input: 1) g1.txt + seq.txt

          2) g2.txt + PIF.out (result of Lab 3)

Output: out1.txt, out2.txt

Run the program and generate: 

- out1.txt (result of parsing if the input was g1.txt); 

- out2.txt (result of parsing if the input was g2.txt)

-messages (if conflict exists/if syntax error exists - specify location if possible)

PART 4: Deliverables

Source code for the parser + in/out files + documentation

Code review

Grading:

Program works for g1.txt, max grade = 8

Program works for g1.txt and g2.txt, max grade = 10
