import json

sentence = "Michael can both read and write."

# <><><><><><> For paragraphs to sentences <><><><>
# sentece_chop = sentence.split('.')
# for sentence in sentence.split('.'):
# ......
# <><><><><><><><><><><><><><><><><><><><><><><><><
word_chopped = sentence.split(' ')

# Building the conjunctions definitions from https://eslforums.com/list-of-conjunctions/


conjunctions = {
    "both": [1,3], # + Word value to the right (index +1). + Word value to the word after "and" (index +3).
    "and": [-1,1], # + Word value to the left and right. (index -1 and +1)
    "the": [1] # I believe this is not a conjuction... but I think its the right behavior?
}

def chopsuey(valued_words, origin, order):
    for addto in order:
        valued_words[words[origin + addto]] += 1
    valued_words[words[origin]] = 0 #(possibly?) del valued_words[words[origin]]
    return valued_words

valued_words = {}
words = sentence.split(' ')
for word in words:
    valued_words[word] = 1


for conjunction in conjunctions.keys():
    if conjunction in words:
        valued_words = chopsuey(valued_words, words.index(conjunction), conjunctions[conjunction])
print(valued_words) 

# <><><><><><> For later implementation: <><><><><>
# Not only ... but also || ex. Not only Mary but also Gabriel is from Italy.
sentence = "Not only Mary but also Gabriel is from Italy."
# Goal: to define the Not, only, but, also
# {"Not":0, "only":0, "Mary":3, 
# "but":0, "also":0, "Gabriel":3, 
# "is":1, "from":1, "Italy.":1 }
# <><><><><><><><><><><><><><><><>
# {"Mary":3, "Gabriel":3, "is":1, "from":1, "Italy.":1}
# {"from":1, "Italy": {"Gabriel":3, "Mary":3}} 

sentence = "I can have either cola or tea."
# Goal: to be able to nest json by definition of "or" and "either" 
# {"I": 1, "can": 1, "have": 1, 
# "either":0, "cola":3, "or":0, "tea.":3}
# <><><><><><><><><><><><><><><><><><><><>
# {"I": 1, "can": 1, "have": 1, "either": {"cola":"3","tea":"3"}}

sentence = "Her story isn't so boring as theirs."