products = []
while True:
	name = input('商品名稱')
	if name == 'q':
		break
	price = input('商品價格')
	products.append([name, price])
print(products)	

	