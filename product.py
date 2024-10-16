product = []

while True:
    name = input('請輸入商品名稱:')
    if name == 'q':
        break
    product.append(name)
print(product)