class Resource:
    def __init__(self, client):
        self.client = client


class SessionResource(Resource):

    PATH_LOGIN = "/api/session"

    def get_token(self, username: str, password: str):
        headers = {"Content-Type": "application/json"}
        auth_data = {"username": username, "password": password}
        response = self.client.request(
            "post", self.PATH_LOGIN, headers=headers, json=auth_data
        )
        return response.json().get("id")


class CardResource(Resource):

    PATH_LIST_CARDS = "/api/card"

    def list(self, auth_token: str):
        response = self.client.authenticated("get", self.PATH_LIST_CARDS, auth_token)
        return response.json()
