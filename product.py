import os #operation system
products = []
if os.path.isfile('ppp.csv'):
    print('Yeah~keep going!')
    # 讀取檔案
    with open('ppp.csv', 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',')
            print([name, price])
else:
    print('File is not exist')
#使用者書輸入
while True:
    name = input('請輸入商品名稱:')
    if name == 'q':
        break
    price = input('請輸入價格:')
    price = int(price)
    products.append([name, price])
#印出使用者內容
print('以下為總結:')
for p in products:
    print(p[0], '價格是 ', p[1])
#寫入檔案
with open('ppp.csv', 'w', encoding='utf-8') as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n' )
    