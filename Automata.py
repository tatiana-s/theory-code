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



