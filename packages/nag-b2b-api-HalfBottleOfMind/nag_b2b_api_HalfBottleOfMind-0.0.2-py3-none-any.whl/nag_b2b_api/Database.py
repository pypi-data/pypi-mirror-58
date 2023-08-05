import sqlite3
import requests

class Database:
    def __init__(self, database = ':memory:', api_key = ''):
        self.api_key = api_key
        
        self.__connection = sqlite3.connect(database)
        self.__cursor = self.__connection.cursor()

        self.__cursor.execute('CREATE TABLE IF NOT EXISTS brands (guid string PRIMARY KEY, title string)')
        self.__cursor.execute('CREATE TABLE IF NOT EXISTS products (guid string PRIMARY KEY, sku string, title string, mainCategory string, brandGuid string)')
        self.__cursor.execute('CREATE TABLE IF NOT EXISTS properties (productGuid string, title string, value string)')
        self.__cursor.execute('CREATE TABLE IF NOT EXISTS prices (productGuid string, price )')
        self.__cursor.execute('CREATE TABLE IF NOT EXISTS descriptions (description text, productGuid string PRIMARY KEY, shortDescription text, features text)')
        self.__cursor.execute('CREATE TABLE IF NOT EXISTS stocks (guid string PRIMARY KEY, name string)')
        self.__cursor.execute('CREATE TABLE IF NOT EXISTS product_stocks (stockGuid string, itemGuid string, free integer, full integer, unit string, date string)')
        self.__connection.commit()

    def execute(self, sql):
        return self.__cursor.execute(sql)

    def refreshDatabase(self):
        print('Renewing database...')
        self.__downloadBrands()
        self.__downloadProducts()
        self.__downloadDescriptions()
        self.__downloadStocks()
        self.__downloadProductsStocks()
        print('Database renewed')

    def __downloadBrands(self):
        url = 'https://b2b-api.nag.ru/api/export/brands'
        brands = requests.get(url, {'hash': self.api_key}).json()

        self.__cursor.execute('DELETE FROM brands')

        for brand in brands:
            self.__cursor.execute('INSERT INTO brands VALUES (?, ?)', (
                brand['guid'],
                brand['title']
            ))

        self.__connection.commit()
        print('\tBrands table renewed')

    def __downloadProducts(self):
        url = 'https://b2b-api.nag.ru/api/export/products'
        products = requests.get(url, {'hash': self.api_key}).json()

        self.__cursor.execute('DELETE FROM products')
        self.__cursor.execute('DELETE FROM properties')

        for product in products:
            titles = []

            for productProperty in product['properties']:
                if not productProperty['propertyTitle'] in titles:
                    titles.append(productProperty['propertyTitle'])

            properties = {}

            for productProperty in product['properties']:
                if productProperty['propertyTitle'] in properties:
                    if not productProperty['propertyValue'] in properties.get(productProperty['propertyTitle']):
                        properties.get(productProperty['propertyTitle']).append(productProperty['propertyValue'])
                else:
                    properties[productProperty['propertyTitle']] = [productProperty['propertyValue'],]

            for productProperty in properties:
                for value in properties[productProperty]:
                    self.__cursor.execute('INSERT INTO properties VALUES (?, ?, ?)', (
                        product['guid'],
                        productProperty,
                        value
                    ))

            self.__cursor.execute('INSERT INTO products VALUES (?, ?, ?, ?, ?)', (
                product['guid'],
                product['sku'],
                product['title'],
                product['itemMainCategory'],
                product['brandGuid'],
            ))

        self.__connection.commit()
        print('\tProduct properties table renewed')
        print('\tProducts table renewed')

    def __downloadDescriptions(self):
        url = 'https://b2b-api.nag.ru/api/export/product_descriptions'
        descriptions = requests.get(url, {'hash': self.api_key}).json()

        self.__cursor.execute('DELETE FROM descriptions')

        for description in descriptions:
            self.__cursor.execute('INSERT INTO descriptions VALUES (?, ?, ?, ?)', (
                description['description'],
                description['itemGuid'],
                description['shortDescription'],
                description['features']
            ))

        self.__connection.commit()

        print('\tDescriptions table renewed')

    def __downloadStocks(self):
        url = 'https://b2b-api.nag.ru/api/export/stocks'
        stocks = requests.get(url, {'hash': self.api_key}).json()

        self.__cursor.execute('DELETE FROM stocks')

        for stock in stocks:
            self.__cursor.execute('INSERT INTO stocks VALUES (?, ?)', (
                stock['guid'],
                stock['name']
            ))

        self.__connection.commit()

        print('\tStocks table renewed')

    def __downloadProductsStocks(self):
        url = 'https://b2b-api.nag.ru/api/export/product_stocks'
        stocks = requests.get(url, {'hash': self.api_key}).json()

        self.__cursor.execute('DELETE FROM product_stocks')

        for stock in stocks:
            self.__cursor.execute('INSERT INTO product_stocks VALUES (?, ?, ?, ?, ?, ?)', (
                stock['stockGuid'],
                stock['itemGuid'],
                stock['free'],
                stock['full'],
                stock['unit'],
                stock['date'],
            ))

        self.__connection.commit()

        print('\tProduct stocks table renewed')

    def __downloadPrices(self):
        url = 'https://b2b-api.nag.ru/api/export/product_prices'
        prices = requests.get(url, {'hash': self.api_key}).json()

        self.__cursor.execute('DELETE FROM prices')

        for price in prices:
            self.__cursor.execute('INSERT INTO prices VALUES (?, ?)', (
                price['itemGuid'],
                price['price']
            ))

        self.__connection.commit()

        print('\tPrices table renewed')

    def getProducts(self):
        return self.__buildProducts(self.__cursor.execute('SELECT guid, sku, title, brandGuid FROM products').fetchall())

    def getProductsByBrand(self, brandGuid):
        return self.__buildProducts(self.__cursor.execute("SELECT guid, sku, title, brandGuid FROM products WHERE brandGuid = '"+brandGuid+"'").fetchall())

    def __buildProducts(self, products):
        output = []

        for product in products:
            properties = {}
            for props in self.__cursor.execute("SELECT title, value FROM properties WHERE productGuid = '"+product[0]+"'").fetchall():
                if props[0] in properties:
                    properties.get(props[0]).append(props[1])
                else:
                    properties[props[0]] = [props[1],]
            description = self.__cursor.execute("SELECT description, shortDescription, features FROM descriptions WHERE productGuid = '"+product[0]+"'").fetchone()
            output.append(Product(
                guid = product[0],
                sku = product[1],
                title = product[2],
                brandGuid = product[3],
                properties = properties,
                description = description[0] if not description == None else None,
                shortDescription = description[1] if not description == None else None,
                features = description[2] if not description== None else None,
                price = self.__getPrice(product[0]),
                stocks = self.__buildStocks(product[0])
            ))

        return output

    def getBrands(self):
        brands = []

        for brand in self.__cursor.execute('SELECT * FROM brands').fetchall():
            brands.append(Brand(title=brand[1], guid=brand[0]))

        return brands

    def __getStocks(self):
        stocks = []

        for stock in self.__cursor.execute('SELECT * FROM stocks').fetchall():
            stocks.append((stock[0], stock[1]))

        return stocks

    def __getStockName(self, guid):
        return self.__cursor.execute("SELECT name FROM stocks WHERE guid = '"+guid+"'").fetchone()[0]

    def __buildStocks(self, itemGuid):
        output = []

        for stock in self.__cursor.execute("SELECT stockGuid, free, unit FROM product_stocks WHERE itemGuid = '"+itemGuid+"'").fetchall():
            output.append({
                'name': self.__getStockName(stock[0]) if not stock[0] == None else 'Неизвестный склад',
                'free': int(stock[1]),
                'unit': stock[2]
            })

        return output

    def __getPrice(self, productGuid):
        result = self.__cursor.execute("SELECT price FROM prices WHERE productGuid = '"+productGuid+"'").fetchone()
        return float(result[0] if not result == None else 0)

class Brand:
    def __init__(self, title, guid):
        self.title = title
        self.guid = guid

    def __str__(self):
        return 'title:\t' + self.title + '\nguid:\t' + self.guid

    def __repr__(self):
        return {
            'title': self.title,
            'guid': self.guid
        }

class Product:
    def __init__(
        self,
        guid,
        sku,
        title,
        brandGuid,
        properties,
        description,
        shortDescription,
        features,
        price,
        stocks
    ):
        self.guid = guid
        self.sku = sku
        self.title = title
        self.brandGuid = brandGuid
        self.properties = properties
        self.description = description
        self.shortDescription = shortDescription
        self.features = features
        self.price = price
        self.stocks = stocks