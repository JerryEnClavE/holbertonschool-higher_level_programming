#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    else:
        return (len(sentence), sentence[0])
print(multiple_returns("At school, I learnt C!"))
print(multiple_returns(""))
