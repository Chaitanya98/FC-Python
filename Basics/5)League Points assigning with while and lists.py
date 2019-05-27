points=0
GD=0
GF=[3,2,5,4,2,1,0,6,1,4,1,1,2,3,1,1]
GA=[0,0,2,1,0,0,0,1,1,2,1,0,0,1,0,1]
for i in range(len(GF)):
	if GF[i]>GA[i]:
		points+=3
	elif GF[i]==GA[i]:
		points+=1

	GD+=(GF[i]-GA[i])

print("Points:",points)
print("Goal Difference:",GD)
