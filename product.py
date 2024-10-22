import os #operation system
# 讀取檔案
def read_file(filename):
        products = []
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                if '商品,價格' in line:
                    continue
                name, price = line.strip().split(',')
                print([name, price])
                products.append([name, price])
            return products
#使用者書輸入
def input_products(products):
    while True:
        name = input('請輸入商品名稱:')
        if name == 'q':
            break
        price = input('請輸入價格:')
        price = int(price)
        products.append([name, price])
    return products
#印出使用者內容
def print_result(products):
    print('以下為總結:')
    for p in products:
        print(p[0], '價格是 ', p[1])
#寫入檔案
def write_file(filename, products):
    with open('products.csv', 'w', encoding='utf-8') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n' )

def main():
    filename = 'products.csv'
    if os.path.isfile(filename):
        print('Yeah~keep going!')
        products = read_file(filename)
    else:
        print('File is not exist')
        products = []
    products = input_products(products)
    print_result(products)
    write_file('products.csv', products)

main()