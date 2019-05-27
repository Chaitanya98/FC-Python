import random

passSkill=90
keepPossession=True
passCounter=0

while keepPossession==True:
	if random.randint(0,100)>passSkill:
		keepPossession=False
	else:
		passCounter+=1

print("Passes completed:",passCounter)