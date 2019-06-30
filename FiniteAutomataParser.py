# deterministic finite automaton
class DFA:
	def __init__(self, states, alphabet, initial_state):
		self.states = states  # map state identifier -> state
		self.alphabet = alphabet  # set of strings
		self.initial_state = initial_state
		self.current_state = initial_state  # string

	def __str__(self):
		string = ["S = {"]
		count = 0
		for s in self.states.keys():
			if count != len(self.states)-1:
				string.append("{}, ".format(s))
			else:
				string.append("{}}}\n".format(s))
			count = count+1
		string.append("∑ = {}\n".format(sorted(self.alphabet)))
		string.append("Initial State = {}\n".format(self.current_state))
		return "".join(string)

	def transition(self, input):
		self.current_state = self.states[self.current_state].transition(input)

	def is_in_end_state(self):
		return self.states[self.current_state].is_end_state

	def reset(self):
		self.current_state = self.initial_state


# state
class State:
	def __init__(self, identifier):
		self.identifier = identifier  # string
		self.is_end_state = False  # boolean
		self.accepted_input = set()  # set of strings (for DFA just alphabet)
		self.transitions = {}  # map input -> resulting state identifier

	def transition(self, input):
		if self.accepted_input.__contains__(input):
			return self.transitions[input]
		else:
			print("Input {} not accepted".format(input))
			return None


# turns a description of an automaton into an object which can be processed further
def parse(is_deterministic, filename):
	if is_deterministic:
		f = open(filename, "r")

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
				states[s] = State(s)

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
		number_of_rules = len(states)*len(alph)
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
		return DFA(states, alph, initial)

	print("Automaton isn't deterministic")  # at the moment user has to know whether this is the case
	return None


# checks whether given word is accepted by given automaton
def word_accepted(automaton, word):
	for char in word:
		if automaton.alphabet.__contains__(char):
			automaton.transition(char)
	result = automaton.is_in_end_state()
	automaton.reset()
	return result


# test example should accept all words where: (number of a's) - (number of b's) congruent to 3 (mod 4)
description_file = "dfa1.txt"
test = parse(True, description_file)

# w1 = "aaa"
# w2 = "aaaab"
# w3 = "a"
# w4 = "b"
# w5 = "abababaaa"
# w6 = "bbbaaaaaaa"

# print("{} is accepted: {} (should be: True)".format(w1, word_accepted(test, w1)))
# print("{} is accepted: {} (should be: True)".format(w2, word_accepted(test, w2)))
# print("{} is accepted: {} (should be: False)".format(w3, word_accepted(test, w3)))
# print("{} is accepted: {} (should be: True)".format(w4, word_accepted(test, w4)))
# print("{} is accepted: {} (should be: True)".format(w5, word_accepted(test, w5)))
# print("{} is accepted: {} (should be: False)".format(w6, word_accepted(test, w6)))


