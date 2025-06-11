from rest_framework.test import APIClient

class TestCategoryViewSetNotImplemented:
    def test_category_list_returns_404_when_view_not_implemented(self):

        client = APIClient()
        url = "/api/categories/"
        response = client.get(url)
        assert response.status_code == 404
