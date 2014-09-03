from pprint import pprint

flowers = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

def makeFold(data,foldNumber,totalFolds):
	for flower in data:
		start = int(len(flower) * foldNumber / totalFolds)
		end = int(len(flower) * (foldNumber + 1) / totalFolds)

with open('data.txt','r') as f:
	rawData = f.read()

data = [[] for _ in flowers]

for example in rawData.split('\n'):
	if example:
		flower = example.split(',')[-1]
		data[flowers.index(flower)].append( example.split(',')[:-1])

makeFold(data, 0, 6)
