import random
emotions = set()

def load_emotions(filename):
	global emotions
	with open(filename, 'r') as file:
		for i in file.read().split('\n'):
			emotions.add(i)

def make_card(size=25):
	if len(emotions) < size:
		print(f"List only has {len(emotions)}, needs at least {size}")
		return
	e = list(emotions)
	random.shuffle(e)
	return e[:size]

def make_cards(cards, size=25):
	if len(emotions) < size:
		print(f"List only has {len(emotions)}, needs at least {size}")
		return
	e = list(emotions)
	for i in range(cards):
		random.shuffle(e)
		yield e[:size]

def continous_cards(size=25):
	if len(emotions) < size:
		print(f"List only has {len(emotions)}, needs at least {size}")
		return
	e = list(emotions)
	while True:
		random.shuffle(e)
		yield e[:25]

if __name__ == "__main__":
	import pprint
	load_emotions("emotions.txt")
	pprint.pprint(emotions)
else:
	load_emotions("emotions.txt")
