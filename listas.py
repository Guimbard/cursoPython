productos = ['notebook', 'lentes', 'iphones', 'parlantes']

productos[0]= 'laptops'
new_products = productos.copy()
new_products.append('Printer')

new_products.extend(productos)
productos.insert(1, 'iPad')

#productos.clear()

productos.pop(2)
productos.remove('parlantes')

print (productos)
#print(new_products)