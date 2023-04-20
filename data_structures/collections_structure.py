from collections import Counter

answers = [
    'yes',  'no',  'yes',  'no',  'no',  'wrong',  'right',  'yes',
    'no answer',  'right',  'wrong',  'no',  'no answer',  'yes',  'yes',
    'yes',  'yes',  'yes',  'yes',  'yes',  'yes',  'yes',  'no',  'yes',
]

print(len(answers))
counted_answers = Counter(answers)
print(counted_answers)
print(counted_answers.most_common()) # returns a list of tuples, where the first element is the count and the second element is the word

from collections import defaultdict

store = defaultdict(float)

store['apple'] = 1.8
store['orange'] = 2.5
store['banana'] = 3.2
store['peach'] # uses the default value of the given data type

print(store)
print(store['apple'])