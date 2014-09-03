from pprint import pprint
import neuralnetwork.py

flowers = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

def extractTest(flower,foldNumber,totalFolds):
	start = int(len(flower) * foldNumber / totalFolds)
	end = int(len(flower) * (foldNumber + 1) / totalFolds)
	return flower[start:end]

def extractTraining(flower,foldNumber,totalFolds):
	start = int(len(flower) * foldNumber / totalFolds)
	end = int(len(flower) * (foldNumber + 1) / totalFolds)
	return flower[0:start] + flower[end:]

def makeFold(data,foldNumber,totalFolds):
	test_data = [extractTest(flower,foldNumber,totalFolds) for flower in data]
	training_data = [extractTraining(flower,foldNumber,totalFolds) for flower in data]
	return test_data, training_data

def kFoldTesting(data,totalFolds):
	accuracy = 0
	for foldNumber in range(totalFolds):
		test, training = makeFold(data,foldNumber,totalFolds)
		accuracy += neuralNetwork(test, training)
	accuracy /= totalFolds
	return accuracy

with open('data.txt','r') as f:
	rawData = f.read()

data = [[] for _ in flowers]

for example in rawData.split('\n'):
	if example:
		flower = example.split(',')[-1]
		data[flowers.index(flower)].append( example.split(',')[:-1])
