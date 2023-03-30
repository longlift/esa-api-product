fake_product_data = {
    1: {'name': 'Product 1', 'price': 100},
    2: {'name': 'Product 2', 'price': 200},
    3: {'name': 'Product 3', 'price': 300}
}


class Repository:

    def selectProductDetail(self, productId: int):
        try:
            try:
                product_details = fake_product_data[productId]
                return product_details, None
            except KeyError as e:
                return None, None
        except Exception as e:
            return None, e
