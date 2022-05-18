
#data = ['比特幣', 30000]
#data.append('比特幣', 30000)


data = []
while True:
	virtual = input('請輸入虛擬貨幣名稱')
	if virtual == 'q':
		break
	price = input('請輸入虛擬貨幣價格')
	data.append([virtual, price])

#for d in data: 
print(data)

with open('data.csv', 'w', encoding = 'utf-8') as f:
	f.write('虛擬貨幣,價格\n')
	for d in data:
		f.write(d[0] + ',' + str(d[1]) + '\n')
