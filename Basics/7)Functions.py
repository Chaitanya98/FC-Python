# def DoubleMe(i):
# 	return i*2
# print(DoubleMe(81))


def newTweet(player,action,success):
	tweet=player+" plays a "+action+"."
	if (success):
		if action=="pass":
			tweet+=" The team keeps possession"
		if action=="shot":
			tweet+=" GOAL!"
	else:
		if action=="pass":
			tweet+=" Pass is intercepted"
		if action=="shot":
			tweet+=" Hits the cross bar"

	print(tweet)

newTweet("Messi","shot",True)
