import networkx as nx
import matplotlib.pyplot as plt
import FiniteAutomataParser as ap


def draw_automaton(automaton, current_state):
	G = nx.DiGraph()
	pos = nx.spring_layout(G)
	normal_nodes = []
	end_nodes = []
	current_nodes = []
	count = 0
	for s in automaton.states.values():
		if s.is_end_state:
			end_nodes.append(count)
		else:
			if s.identifier == current_state:
				current_nodes.append(count)
			else:
				normal_nodes.append(count)
		count = count+1

	plt.figure()
	plt.axis('off')
	plt.show()


description_file = "dfa1.txt"
test = ap.parse(True, description_file)
draw_automaton(test, "z0")






