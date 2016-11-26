import nltk
grammar1=nltk.CFG.fromstring("""
S -> VP NP PP | ADV NP VP | NP VP | P S P S | NP VP PP | S P S
ADV -> 'hopefully' | 'not' | 'most' | 'now' | 'somehow' | 'can'
VP -> Det V | V V | VP NP | V | V ADV V | V ADV JJ
NP -> N N | Det JJ N | Det N | N | JJ N | N V | Det ADV JJ ADV | NP N | PP NP ADV VP
PP -> P P N N | P NP | N P
Det -> 'that' | 'the'
JJ -> 'electoral' | 'whatever' | 'viable' | 'no' | 'unacceptable'
V -> 'is' | 'will' | '#voteforhillary' |'watching' | 'did' | 'own'
V -> 'got' | 'grope' | 'disregard'
N -> 'madam' | 'president' | 'tomorrow' | '#strongertogether' | 'college' | 'world'
N -> 'electoralcollge' | '#voteforhillary' | 'you' | 'reason' | 'clinton' | '#imwithher'
N -> 'green' | 'day' | 'singing' | 'trump' | 'kkk' | 'saying' | 'women' | 'something' | 'half'
N -> 'america' | 'he'
P -> 'as' | 'of' | 'if' | 'then' | 'for' | 'what' | 'but'

""")

sent='green day singing no trump no kkk is somehow unacceptable but trump saying he can grope women is something half of america can disregard'.split()
parser=nltk.ChartParser(grammar1)
for tree in parser.parse(sent):
    print(tree)

#sent1='Mary saw Bob'.split()
#rd_parser=nltk.RecursiveDescentParser(grammar1)
#for tree in rd_parser.parse(sent1):
    #print(tree)

