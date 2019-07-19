import Automata as automata
import Grammar as grammar


def parse_grammar(file_path):
	# open file
	f = open(file_path, "r")

	# variables
	line = f.readline()
	line = line.replace(" ", "")
	line = line.replace("\n", "")
	var = set()
	tokens = line.split("=")
	if tokens[0] != "V":
		return None
	else:
		tokens[1] = tokens[1].replace("{", "")
		tokens[1] = tokens[1].replace("}", "")
		tokens = tokens[1].split(",")
		for v in tokens:
			var.add(v)

	# alphabet
	line = f.readline()
	line = line.replace(" ", "")
	line = line.replace("\n", "")
	alph = set()
	tokens = line.split("=")
	if tokens[0] != "A":
		print("Grammar description isn't valid")
		return None
	else:
		tokens[1] = tokens[1].replace("{", "")
		tokens[1] = tokens[1].replace("}", "")
		tokens = tokens[1].split(",")
		for a in tokens:
			alph.add(a)

	# start variable
	line = f.readline()
	line = line.replace(" ", "")
	line = line.replace("\n", "")
	tokens = line.split("=")
	if tokens[0] != "S":
		print("Grammar description isn't valid")
		return None
	else:
		s = tokens[1]

	# production rules
	line = f.readline()
	line = line.replace(" ", "")
	line = line.replace("\n", "")
	line.replace(" ", "")
	tokens = line.split("=")
	if tokens[0] != "P":
		print("Grammar description isn't valid")
		return None
	else:
		number_of_rules = int(tokens[1])
	rul = {}
	for i in range(number_of_rules):
		line = f.readline()
		line = line.replace(" ", "")
		line = line.replace("\n", "")
		tokens = line.split("->")
		rul[tokens[0]] = tokens[1]

	f.close()

	# resulting grammar object
	return grammar.Grammar(var, alph, s, rul)


def parse_dfa(file_path):
	# open file
	f = open(file_path, "r")

	# states
	line = f.readline()
	line = line.replace(" ", "")
	line = line.replace("\n", "")
	states = {}
	tokens = line.split("=")
	if tokens[0] != "S":
		print("Automaton description isn't valid")
		return None
	else:
		tokens[1] = tokens[1].replace("{", "")
		tokens[1] = tokens[1].replace("}", "")
		tokens = tokens[1].split(",")
		for s in tokens:
			states[s] = automata.State(s)
	# alphabet
	line = f.readline()
	line = line.replace(" ", "")
	line = line.replace("\n", "")
	alph = set()
	tokens = line.split("=")
	if tokens[0] != "A":
		print("Automaton description isn't valid")
		return None
	else:
		tokens[1] = tokens[1].replace("{", "")
		tokens[1] = tokens[1].replace("}", "")
		tokens = tokens[1].split(",")
		for a in tokens:
			alph.add(a)
	for s in states.values():
		s.accepted_input = alph

	# initial state
	line = f.readline()
	line = line.replace(" ", "")
	line = line.replace("\n", "")
	tokens = line.split("=")
	if tokens[0] != "I":
		print("Automaton description isn't valid")
		return None
	else:
		initial = tokens[1]

	# end states
	line = f.readline()
	line = line.replace(" ", "")
	line = line.replace("\n", "")
	tokens = line.split("=")
	if tokens[0] != "E":
		print("Automaton description isn't valid")
		return None
	else:
		tokens[1] = tokens[1].replace("{", "")
		tokens[1] = tokens[1].replace("}", "")
		tokens = tokens[1].split(",")
		for e in tokens:
			states[e].is_end_state = True

	# transition function
	number_of_rules = len(states) * len(alph)
	for r in range(number_of_rules):
		line = f.readline()
		line = line.replace(" ", "")
		line = line.replace("\n", "")
		tokens = line.split("=")
		tokens[0] = tokens[0].replace("d", "")
		tokens[0] = tokens[0].replace("(", "")
		tokens[0] = tokens[0].replace(")", "")
		t = tokens[0].split(",")
		if alph.__contains__(t[1]):
			states[t[0]].transitions[t[1]] = tokens[1]
		else:
			print("Automaton description isn't valid")
			return None

	f.close()

	# resulting dfa object
	return automata.DFA(states, alph, initial)
