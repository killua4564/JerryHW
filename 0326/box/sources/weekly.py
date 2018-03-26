def forecast():
	import random
	possibilities = ['下雨', '下雪', '起霧', '晴天', '誰知道']
	return random.choice(possibilities)