import os #作業系統operating system。我們寫的程式權限沒這麼大，只好載入作業系統檢查有沒有此檔案

data = []
if os.path.isfile('data.csv'): #檢查檔案有沒有在相對路徑中(同資料夾中)
	print('找到檔案了')
	#找到後開始讀取檔案(讀取完可再重新寫入)
	data = []
	with open('data.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if '虛擬貨幣,價格' in line: #跳過標題
				continue #放棄這回下一回繼續重新再來(並不會因此跳出迴圈)，通常放在for或while的高位(才有東西可以跳過)
			virtual, price = line.strip().split(',')
			data.append([virtual, price])
	print(data)

else:
	print('找不到檔案')

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


data1 = [1, 3, 5, 7, 9]
with open('data1.csv', 'w', encoding = 'utf-8') as f:
	for d1 in data1:
		f.write(str(d1) + '\n')


data2 = []
data2.append(['珍奶', 30])
print(data2)
with open('data2.csv', 'w', encoding = 'utf-8') as f:
	for d2 in data2:
		f.write(d2[0] + ',' + str(d2[1]) + '\n')