# MIT License
# 
# Copyright (c) 2022 Patrick Peled
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import pandas as pd


class gen_stock:
    ''' General stock class used to define different stock types '''
    def __init__(self, stock: int = 0):
        ''' function to initiate the stock of the stock type
        stock: int of the amount of stock available of the stock type upon beginning'''
        self.stock = stock

    def add_stock(self, addition: int):
        ''' function to add to the stock of the stock type
        addition: int of the amount of stock to add to the stock of the stock type'''
        self.stock += addition

    def remove_stock(self, substraction):
        ''' function to remove from the stock of the stock type
        addition: int of the amount of stock to remove from the stock of the stock type'''
        if self.stock < substraction: #if there is less stock available than we want to transfer out, the transfer is cancelled
            return "Not enough stock in warehouse"
        else:
            self.stock -= substraction

class banana(gen_stock):
    def __init__(self):
        super().__init__()
        self.type = "banana"

class apple(gen_stock):
    def __init__(self):
        super().__init__()
        self.type = "apple"

class kiwi(gen_stock):
    def __init__(self):
        super().__init__()
        self.type = "kiwi"

class gen_warehouse:
    ''' General warehouse class used to provide the functionality '''
    def __init__(self, warehouse_name: str):
        ''' function to initiate the warehouse
        warehouse_name: str of the name we would like to call the warehouse internally'''
        self.name = warehouse_name
        self.banana = banana()
        self.apple = apple()
        self.kiwi = kiwi()

    def stock_available(self, own_stock: object) -> int:
        ''' function to get an overview of the stock available of a stock type in the given warehouse
        own_stock: object of warehouse.stock_type that we would like to know the stock of
        output: int of the stock available'''
        return own_stock.stock


    def create_report(self) -> pd.DataFrame:
        ''' function to get a report of the stock available in a given warehouse
        output: df of the stock_types in stock and the stock available'''
        report = {"Type": [], "Stock": []}
        stock_types = [self.banana, self.apple, self.kiwi]
        for stock_type in stock_types:
            if stock_type.stock > 0:
                report["Type"].append(stock_type.type)
                report["Stock"].append(stock_type.stock)
        report_df = pd.DataFrame(data = report)

        return report_df

        

    def share_stock(self, own_stock: object, other_stock: object, amount: int):
        ''' function to transfer stocks between two warehouses
        own_stock: obj of the warehouse.stock_type that we want to transfer stock out of
        other_stock: obj of the warehouse.stock_type that we want to transfer stock to
        amount: int of the amount of stock we would like to move'''
        own_stock.remove_stock(amount)
        other_stock.add_stock(amount)




if __name__ == "__main__":
    #instantiating the two warehouses
    wh_south = gen_warehouse("Barcelona, South")
    wh_north = gen_warehouse("Barcelona, North")

    #Adding some stocks to the warehouses
    wh_south.apple.add_stock(10)
    wh_south.banana.add_stock(15)
    wh_north.kiwi.add_stock(8)
    wh_north.banana.add_stock(5)

    #checking the availabilities after adding the stock
    wh_south.stock_available(wh_south.banana)
    wh_north.stock_available(wh_north.apple)

    #Transferring stock between warehouses
    wh_south.share_stock(wh_south.banana, wh_north.banana, 5)

    #Getting the full report of stocks in each warehouse
    wh_south.create_report()
    wh_north.create_report()
    
    
