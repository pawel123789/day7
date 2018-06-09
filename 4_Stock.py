import copy

"Initialize class Stock"

class Stock:

    def __init__(self, initial):
        self.products = copy.deepcopy(initial)

    def resupply(self, product, count):
        if count <= 0:
            raise ValueError('Only positive count')
        self.products[product] = self.products.get(product, 0) + count

    def withdraw(self, products, count):
       if count <= 0:
           raise ValueError('Tego produktu nie ma na stanie')
        if products not in self.products:
            raise ValueError('Unknown product' + product)
       if self.products[product] < count:
           raise ValueError('Insufficent number of items in stock')
       seld.products[product] -= count

    def available_items(self, products, count):
        items = {}
        for products, count in self.products.itmes()
            if count > 0
                items[product] = count
        return items



products = {'orange' :2, 'lemon': 3}
stock = Stock(products)
print(stock.products)