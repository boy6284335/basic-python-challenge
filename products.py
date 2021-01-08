
def count_products(data):
    new_data = []
    pro_dict = {}
    for i in data:
        s = i.split(' ')
        new_data.append(s)
    for j in new_data:
        product = j[0]
        if product not in pro_dict:
            pro_dict[product] = int(j[1])
        else:
            pro_dict[product] += 1

    return(pro_dict)

data = ['麥香奶茶 2', '御飯糰 1', '可可 10', '麥香奶茶 1']
print(count_products(data))
    
