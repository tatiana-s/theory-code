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
	
