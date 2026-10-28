import random
print("Random integer:",random.randint(1,100))
print("Random number:",random.random())
print("Random choice:",random.choice([10,20,30,40]))
print("Random sample:",random.sample([1,2,3,4,5],3))
numbers=[1,2,3,4,5]
random.shuffle(numbers)
print("Shuffled list:",numbers)
print("Random range:",random.randrange(1,10))
print("Random uniform:",random.uniform(1,10))
