from pprint import pprint

flowers = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

with open('data.txt','r') as f:
	rawData = f.read()

data = [[] for _ in flowers]

for example in rawData.split('\n'):
	if example:
		flower = example.split(',')[-1]
		data[flowers.index(flower)].append( example.split(',')[:-1])

pprint (data)

