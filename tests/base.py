import json

import pytest
from flask import url_for
from werkzeug.datastructures import Headers


@pytest.mark.usefixtures('client_class')
class Base:
    headers = None

    def set_jwt(self, jwt_item=None):
        if jwt_item is not None:
            item = jwt_item
            jwt_name = 'Bearer {}'.format(item)
            self.headers = Headers()
            self.headers.add_header('Authorization', jwt_name)

    def get(self, endpoint, jwt=None, **kwargs):
        url = url_for(endpoint, **kwargs)
        self.set_jwt(jwt)
        response = self.client.get(url, headers=self.headers)
        return response

    def post(self, endpoint, data, jwt=None, **kwargs):
        url = url_for(endpoint, **kwargs)
        self.set_jwt(jwt)
        response = self.client.post(
            url,
            data=json.dumps(data),
            content_type='application/json',
            headers=self.headers,
        )
        return response

    def put(self, endpoint, data, jwt=None, **kwargs):
        url = url_for(endpoint, **kwargs)
        self.set_jwt(jwt)
        response = self.client.put(
            url,
            data=json.dumps(data),
            content_type='application/json',
            headers=self.headers,
        )
        return response

    def patch(self, endpoint, data, csrf=None, **kwargs):
        url = url_for(endpoint, **kwargs)
        self.set_jwt(csrf)
        response = self.client.patch(
            url,
            data=json.dumps(data),
            content_type='application/json',
            headers=self.headers,
        )
        return response

    def delete(self, endpoint, jwt=None, **kwargs):
        url = url_for(endpoint, **kwargs)
        self.set_jwt(jwt)
        response = self.client.delete(url, headers=self.headers)
        return response

    def login(self, endpoint, user, password):
        data = {
            'email': user.email,
            'password': password,
        }

        response = self.post(endpoint, data)

        self.access = response.json['access']
        self.refresh = response.json['refresh']

        self.set_jwt(self.access)

        return response
