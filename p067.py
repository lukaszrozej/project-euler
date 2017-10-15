# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'),
# a 15K text file containing a triangle with one-hundred rows.

# Reusing function from problem 18

def max_path_in_triangle(text):
	# text to triangle
	triangle = []
	for line in text.strip().split('\n'):
		row_of_str = line.split(' ')
		row_of_int = list( map(int, row_of_str) )
		triangle.append(row_of_int)
	# dynamic programing
	for i in range(1, len(triangle)):
		triangle[i][0] += triangle[i-1][0]
		triangle[i][i] += triangle[i-1][i-1]
		for j in range(1, i):
			triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

	return max(triangle[-1])

with open('p067_triangle.txt') as file:
	text = file.read()

print( max_path_in_triangle(text) )