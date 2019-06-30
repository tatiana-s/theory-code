grammar_file = "grammar1.txt"


class Grammar:
	def __init__(self, variables, alphabet, start, rules):
		self.variables = variables  # set of strings
		self.alphabet = alphabet  # set of strings
		self.start = start  # string
		self.rules = rules  # map string identifier -> string rule
		self.type = "Typ-0"  # string

	def __str__(self):
		string = ["V = {}\n".format(self.variables), "∑ = {}\n".format(sorted(self.alphabet)), "S = {}\n".format(self.start), "P = {"]
		count = 0
		for p in self.rules.keys():
			if count < len(self.rules) - 1:
				string.append("{}, ".format(p))
			else:
				string.append("{}}}\n".format(p))
			count += 1
		string.append("(Type: {})\n".format(self.type))
		return "".join(string)


def parse(filename):
	f = open(filename, "r")

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

	# resulting grammar object
	return Grammar(var, alph, s, rul)


test = parse(grammar_file)




