class Product_Service:
    def __init__(self,client):
        self.client=client

    def get_all_products(self):
        return self.client.get("products")

    def get_product_by_id(self,product_id):
        return self.client.get(f"products/{product_id}")


    def create_product(self,payload):
        return self.client.post(payload,"products")

    def update_product(self,product_id,payload):
        return self.client.put(payload,f"products/{product_id}")


    def delete_product(self,product_id):
        return self.client.delete(f"products/{product_id}")

    def search_products(self,query):
        return self.client.get(f"products/search?query={query}")

