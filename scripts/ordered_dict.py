from collections import OrderedDict

N = int(input())
ordered_items = OrderedDict()

for _ in range(N):
    while True:
        try:
            data = input().split()
            item_name = data[:-1]
            item = ' '.join(item_name)
            net_price = int(data[-1])
            if item not in ordered_items:
                ordered_items[item] = net_price
            else:
                ordered_items[item] += net_price
            break
        except ValueError:
            print('Only integer is allowed! Try again! ')

for k in ordered_items:
    print(k, ordered_items[k])