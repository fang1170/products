#讀取檔案
products = []
with open ('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f :
		# s = line.strip().split(',')            #split會存成字串
		# name = s[0]
		# price = s[1]
		if '商品, 價格' in line:                  # continue 跳過進到下一迴 跳過9、10行
			continue
		name, price = line.strip().split(',')     #上面三行的簡化寫法    
		products.append([name, price])
print(products)		
#讓使用輸入
while True:
	name = input('商品名稱:')
	if name == 'q':
		break
	price = input('商品價格:')
	# p = []
	# p.append(name)
	# p.append(price)
	# products.append(p)
	products.append([name, price])         #簡化寫法
#印出購買紀錄	
print(products)	
for p in products:
	print(p[0], '的價格為:', p[1])
#寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f:        #with 關掉檔案  用utf-8編碼讀取中文字
	f.write('商品, 價格\n')
	for p in products:
		f.write(p[0]+ ','+ p[1]+ '\n')         # 加法只能字串加字串 或數字加數字


	