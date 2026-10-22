
import unittest
import os

os.environ["TODO_DATABASE_URI"] = "sqlite:///:memory:"

import app as todo_app


class TodoApiTest(unittest.TestCase):

    def setUp(self):
        todo_app.app.config["TESTING"] = True
        self.client = todo_app.app.test_client()
        self.ctx = todo_app.app.app_context()
        self.ctx.push()
        todo_app.db.drop_all()
        todo_app.db.create_all()

    def tearDown(self):
        todo_app.db.session.remove()
        self.ctx.pop()

    def test_만든_것이_목록에_그대로_나온다(self):
        self.client.post(
            "/api/todos/",
            json={"text": "우유 사기", "done": True}
        )
        self.client.post(
            "/api/todos/",
            json={"text": "책 반납"}
        )

        r = self.client.get("/api/todos/")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.get_json()), 2)

    def test_만들면_201_과_만들어진_것이_온다(self):
        r = self.client.post(
            "/api/todos/",
            json={"text": "우유 사기"}
        )

        self.assertEqual(r.status_code, 201)
        self.assertEqual(
            r.get_json()["text"],
            "우유 사기"
        )

    def test_없는_번호는_404_다(self):
        r = self.client.get("/api/todos/999")
        self.assertEqual(r.status_code, 404)

    def test_patch_는_보낸_칸만_바꾼다(self):
        made = self.client.post(
            "/api/todos/",
            json={"text": "책 반납"}
        ).get_json()

        r = self.client.patch(
            f"/api/todos/{made['id']}",
            json={"done": True}
        )

        self.assertEqual(
            r.get_json()["text"],
            "책 반납"
        )
        self.assertTrue(r.get_json()["done"])

    def test_지우면_204_고_다시_찾으면_404_다(self):
        made = self.client.post(
            "/api/todos/",
            json={"text": "지울 것"}
        ).get_json()

        self.assertEqual(
            self.client.delete(
                f"/api/todos/{made['id']}"
            ).status_code,
            204
        )

        self.assertEqual(
            self.client.get(
                f"/api/todos/{made['id']}"
            ).status_code,
            404
        )


if __name__ == "__main__":
    unittest.main()
