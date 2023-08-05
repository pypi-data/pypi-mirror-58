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