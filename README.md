# sentence-generator

Random sentence generator from context-free grammars.


#### Usage:

For example, to generate 10 random sentences using a grammar described in the file grammar.txt, run:

```python sentence_generator.py --grammar=grammar.txt --num_sentences=10```

#### Grammar file:

Grammar file must follow a specific format. 
The first line should be the starting symbol of the grammar.
The following lines are the production rules of the grammar. The set of terminal and non-terminal symbols are inferred from the grammar. 

Each production rule must have the format X -> A B .. C
The left side should be a single non-terminal symbol.
The right side should be a list of symbols (terminal or non-terminal), separated by spaces.

#### Examples:

We provide 2 sample grammars: A very simple toy grammar, in the file `simple_grammar.txt`, and a grammar designed to represent a subset of Brazilian Sign Language (Libras) syntax, in the file `libras_grammar.txt`.
