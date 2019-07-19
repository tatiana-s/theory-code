import DescriptionParser as dp
import Toolbox as tb

# grammar example
test1 = dp.parse_grammar("grammar1.txt")
print(test1)

# dfa test example should accept all words where: (number of a's) - (number of b's) congruent to 3 (mod 4)
test2 = dp.parse_dfa("dfa1.txt")

w1 = "aaa"
w2 = "aaaab"
w3 = "a"
w4 = "b"
w5 = "abababaaa"
w6 = "bbbaaaaaaa"

print("{} is accepted: {} (should be: True)".format(w1, tb.word_accepted(test2, w1)))
print("{} is accepted: {} (should be: True)".format(w2, tb.word_accepted(test2, w2)))
print("{} is accepted: {} (should be: False)".format(w3, tb.word_accepted(test2, w3)))
print("{} is accepted: {} (should be: True)".format(w4, tb.word_accepted(test2, w4)))
print("{} is accepted: {} (should be: True)".format(w5, tb.word_accepted(test2, w5)))
print("{} is accepted: {} (should be: False)".format(w6, tb.word_accepted(test2, w6)))