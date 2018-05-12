import argparse
import random
import operator

terminals = set()
num_expansions = {}

def populate_terminals():
	terminals = set()
	for key, val in grammar.items():
		for word_list in val:
			for word in word_list:
				if word not in grammar:
					terminals.add(word)
	return terminals

def calc_expansions(term):
	if term in num_expansions:
		return num_expansions[term]
	if term in terminals:
		num_expansions[term] = 1
	else:
		num_exp = 0
		for sntc in grammar[term]:
			curr = 1
			for t in sntc:
				curr *= calc_expansions(t)
			num_exp += curr
		num_expansions[term] = num_exp
	return num_expansions[term]

def count_expansions():
	num_expansions = {}
	calc_expansions('Sentenca')

def analyze_stats(sentences):
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

def generate_random_sentence(print_sentence = True):
	sentence = ['Sentenca']
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
	parser.add_argument('--print_atoms', action='store_true',
					  help='Print atoms of the grammar')
	parser.add_argument('--num_sentences', type=int, default=0,
					  help='The number of random sentences to generate.')
	parser.add_argument('--include_atoms', type=bool, default=False,
					  help='Wheather to include atoms or not.')

	args = parser.parse_args()

	terminals = populate_terminals()
	
	if args.print_atoms:
		for terminal in sorted(terminals):
			print(terminal)
		print('-----------------')
		print('There are', len(terminals), 'terminals')

	sentences = []
	for i in range(args.num_sentences):
		sentences.append(generate_random_sentence(False))

	offset = 0
	if args.include_atoms:
		for terminal in sorted(terminals):
			print("%d. %s" % (offset+1, terminal.upper()))
			offset += 1

	for i in range(len(sentences)):
		print("%d. %s" % (i+offset+1, sentences[i]))