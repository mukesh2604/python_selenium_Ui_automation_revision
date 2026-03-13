from api.services.product_service import Product_Service

class TestProductAPI:

    def test_get_all_products(self, api_client):
        service = Product_Service(api_client)
        response = service.get_all_products()

        assert response.status_code == 200


    def test_get_product_by_id(self, api_client):
        service = Product_Service(api_client)
        response = service.get_product_by_id(1)

        assert response.status_code == 200

    def test_create_product(self, api_client):
        service = Product_Service(api_client)
        payload = {
            "name": "Test Product",
            "price": 9.99,
            "description": "This is a test product"
        }
        response = service.create_product(payload)

        assert response.status_code == 201

    def test_update_product(self, api_client):
        service = Product_Service(api_client)
        payload = {
            "name": "Updated Test Product",
            "price": 19.99,
            "description": "This is an updated test product"
        }
        response = service.update_product(1, payload)

        assert response.status_code == 200

    def test_delete_product(self, api_client):
        service = Product_Service(api_client)
        response = service.delete_product(1)

        assert response.status_code == 200