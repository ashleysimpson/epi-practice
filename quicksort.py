import os

x = []

def quicksort(low_wall, high_wall):
	if (low_wall >= high_wall):
		return
	
	wall = low_wall

	for y in range(low_wall, high_wall):
		
 		if (x[y] <= x[high_wall]):
			temp = x[wall]
			x[wall] = x[y]
			x[y] = temp
			wall = wall + 1

	temp = x[wall]
	x[wall] = x[high_wall]
	x[high_wall] = temp


	print "wall/inded: " + str(wall) + " list: " + str(x)

	quicksort(low_wall,wall-1)
	quicksort(wall+1,high_wall)

x = [6,5,4,3,2,1,2,1,4,6,8,6,5,3,2,3,4,67,9,0,7,5,2]

quicksort(0, len(x) - 1)

print x