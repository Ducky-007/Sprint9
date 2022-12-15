# import pandas as pd 
# df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
# print(df.head())

import random

adj = ['blue', 'large', 'grainy', 'substantial', 'potent', 'thermonuclear']
nouns = ['food', 'house', 'tree', 'bicycle', 'toupee', 'phone']

def random_phrase(adj, noun):
    adj = random.choice(adj)
    noun = random.choice(noun)
    return adj + ' ' + noun

if __name__ == '__main__':
    print(random_phrase(adj, nouns))