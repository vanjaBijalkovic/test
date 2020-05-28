from .base import Base
from random import randint

class TestRole(Base):
    def test_get_all(self, user_factory):
        user = user_factory()
        user.save()
        response = self.login('auth.login', user, 'Sekrit')
        assert response.status_code == 200
        response = self.get('roles.list')
        assert response.status_code == 200

    def test_post(self, user_factory, role_factory):
        user = user_factory()
        role = role_factory()
        role.save()
        user.save()
        response = self.login('auth.login', user, 'Sekrit')
        assert response.status_code == 200

        data = {
            'description': 'Admin role.{}'.format(randint(0,100001)),
            'name': 'Admin',
        }

        response = self.post('roles.list', data)
        assert response.status_code == 200
        json_data = response.get_json()
        assert data['name'] == json_data['name']
        newrole = role.get(id=json_data['id'])
        assert newrole.description == data['description']

    def test_get(self, user_factory, role_factory):
        user = user_factory()
        role = role_factory()
        user.save()
        role.save()
        response = self.login('auth.login', user, 'Sekrit')
        assert response.status_code == 200
        response = self.get('roles.detail', role_id=role.id)
        assert response.status_code == 200

    def test_patch(self, user_factory, role_factory):
        user = user_factory()
        role = role_factory()
        user.save()
        role.save()
        response = self.login('auth.login', user, 'Sekrit')
        assert response.status_code == 200
        data = {
            'description': 'Admin role',
        }
        response = self.patch('roles.detail', data, role_id=role.id)
        assert response.status_code == 200
        role = role.get(id=role.id)
        assert role.description == data['description']

    def test_delete(self, user_factory, role_factory):
        user = user_factory()
        user.save()
        response = self.login('auth.login', user, 'Sekrit')
        assert response.status_code == 200
        newrole = role_factory()
        newrole.save()
        response = self.delete('roles.detail', role_id=newrole.id)
        assert response.status_code == 200

    def test_assign_deassign_role(self, user_factory, role_factory):
        user = user_factory()
        role = role_factory()
        user.save()
        role.save()
        response = self.login('auth.login', user, 'Sekrit')
        assert response.status_code == 200
        user = user_factory()
        user.save()
        data = {
            "id": user.id
        }
        response = self.post('roles.user_assign',
                             data,
                             role_id=role.id)
        assert response.status_code == 200
        response = self.delete('roles.user_deassign',
                               user_id=user.id,
                               role_id=role.id)
        assert response.status_code == 200
