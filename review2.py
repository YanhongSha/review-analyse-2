# review List and File 



#1. 读取清单, 确定读取速度 每10000次显示一次

data = []
count = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))

print('There are', len(data), 'in total.')

print(data[0])

wc = {}  # word count
for d in data:    #d是字串   data是清单
	words = d.split()     #所有空格键都会直接跳过
	for word in words:
		if word in wc:
			wc[word] += 1   #如果存在 +1
		else:
			wc[word] = 1  #如果不存在，追加一行，值为1
for word in wc:
	if wc[word] > 1000000:      #打印出现100次以上的单词   
		print(word,wc[word])	
print(len(wc))     #len(wc)字典的长度，条数

while True:
	word = input('which word do you want to check: ')
	if word == 'q':
		print('Thanks for checking!!!')
		break
	else:	
		if word in wc:
			print('The',  word,  'appears',  wc[word], 'times.')
		elif word not in wc:
			print('It is not in the dictionary!!!')






