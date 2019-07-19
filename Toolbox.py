# checks whether given word is accepted by given automaton
def word_accepted(automaton, word):
	for char in word:
		if automaton.alphabet.__contains__(char):
			automaton.transition(char)
	result = automaton.is_in_end_state()
	automaton.reset()
	return result
