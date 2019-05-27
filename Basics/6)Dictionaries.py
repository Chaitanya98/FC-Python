Player={"Name":"Messi","Position":["SS","RW","CF"],"Jersey No":10}
Player["Goals"]=48
Player["Assists"]=18
GA=0

for key in Player:
	print(key,":",Player[key])
	if key=="Goals" or key=="Assists":
		GA+=Player[key]

print("G+A:",GA)