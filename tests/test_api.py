import unittest
from app import app

class TestBookAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.headers = {"Authorization": "secret-token"}

    def test_get_books(self):
        response = self.client.get("/books", headers=self.headers)
        self.assertEqual(response.status_code, 200)

    def test_add_book(self):
        response = self.client.post(
            "/books",
            json={"title": "New Book", "author": "Author", "published_year": 2024},
            headers=self.headers,
        )
        self.assertEqual(response.status_code, 201)

if __name__ == "__main__":
    unittest.main()
