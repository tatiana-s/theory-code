# Theory Code
Work in Progress dealing with concepts from theoretical computer science such as formal languages and finite automata.

## Current Status
- GrammarParser: 
    - reads grammar descriptions in a format following EBNF:
    ```
    V = {v1, v2}  # variables
    A = {a, b, c}  # alphabet
    S = v1  # start variable
    P = 2  # number of production rules
    v1 -> v2 | "a".v1 | "a"  # rules 
    v2 -> "b" | "c" 
    ```
- FiniteAutomataParser: 
    - reads DFA descriptions in the following format:

    ```
    S = {z0, z1, z2, z3}  # states
    A = {a, b}  # alphabet
    I = z0  # initial state
    E = {z3}  # end states
    d(z0, a) = z1  # transition rules
    d(z0, b) = z3
    d(z1, a) = z2
    d(z1, b) = z0
    d(z2, a) = z3
    d(z2, b) = z1
    d(z3, a) = z0
    d(z3, b) = z2
    ```
    - checks whether a word is accepted by a DFA
 
## Sources

For theory background I'm currently mostly using *'Theoretische Informatik - kurz gefasst'* by Uwe Schöning.
