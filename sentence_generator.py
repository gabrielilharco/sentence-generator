import argparse
import random
import operator

def find_terminals(grammar):
	"""
    For a given grammar, return a set of the terminal symbols.

    :param grammar: The grammar (set of productions rules).
    :return: set of terminal symbols.
    """
	terminals = set()
	for key, val in grammar.items():
		for word_list in val:
			for word in word_list:
				if word not in grammar:
					terminals.add(word)
	return terminals

def analyze_stats(sentences):
	"""
    For a given set of sentences, print how many times each symbol appears,
    printing statistics sorted by occurrance.

    :param sentences: List of sentences.
    """
	counts = {}
	for sentence in sentences:
		for element in sentence.split():
			if element not in counts:
				counts[element] = 1
			else:
				counts[element] += 1

	# print stats
	sorted_counts = sorted(counts.items(), key = operator.itemgetter(1))
	for key, val in sorted_counts:
		print("%5d %s" % (val, key))

def generate_random_sentence(grammar, start_symbol, print_sentence = True):
	"""
    For a given grammar (set of production rules) and a starting symbol,
    randomly generate a sentence using the production rules.

    :param sentences: The grammar (set of productions rules).
    :param start_symbol: The starting symbol.
    :param print_sentence: Wether to print the generated sentence. Defaults to true.
    :returns: A randomly generated sentence.
    """
    # Starting symbol must be a part of the grammar
    assert start_symbol in grammar
    
    sentence = [start_symbol]
	idx = 0
	while idx < len(sentence):
		if sentence[idx] in terminals:
			idx += 1
		else:
			choices = grammar[sentence[idx]]
			choice = random.choice(choices)
			sentence = sentence[:idx] + choice + sentence[idx+1:]
	sentence = " ".join([word.upper() for word in sentence])
	if print_sentence:
		print(sentence)
	return sentence

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Grammar utils')
	parser.add_argument('--grammar', type='string', default='grammar.txt',
					  help='Path to grammar file.')
	parser.add_argument('--print_terminal_symbols', type=bool, default=False,
					  help='Print the terminal symbols of the grammar.')
	parser.add_argument('--num_sentences', type=int, default=0,
					  help='The number of random sentences to generate.')

	args = parser.parse_args()

	terminals = find_terminals()
	
	if args.print_atoms:
		for terminal in sorted(terminals):
			print(terminal)
		print('-----------------')
		print('There are', len(terminals), 'terminals')

	sentences = []
	for i in range(args.num_sentences):
		sentences.append(generate_random_sentence(False))

	for i in range(len(sentences)):
		print("%d. %s" % (i, sentences[i]))