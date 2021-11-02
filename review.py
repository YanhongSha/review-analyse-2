# review analysis
# % 用于求余数
data = []
count = 0
x = 0 
l = 0
sum = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1	
print('Fully read, the number is', len(data), 'cases')

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print(len(new))
print(new[0])
