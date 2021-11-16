# Django
from django.test import TestCase

import json
from datetime import datetime

# Django Rest Framework
from rest_framework.test import APIClient
from rest_framework import status

# Models
from list.models import Lista


class UserTestCase(TestCase):
    def setUp(self):

        # Creamos un libro
        lista = Lista(
        description = "Description test",
        status = True,
        creation_date = datetime.today().strftime('%Y-%m-%d')
        )
        lista.save()

    def test_insert_lista(self):
        """Check if we can create a list"""

        client = APIClient()
        response = client.post(
            '/todoList/', {
            "description":"Description Test", 
            },
            format='multipart'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json.loads(response.content), {
            "id":2, 
            "description":"Description Test", 
            "status":False, 
            "creation_date":datetime.today().strftime('%Y-%m-%d')
            })

    def test_get_book(self):
        """Get todolist"""

        client = APIClient()
        response = client.get('/todoList/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), [{
            "id":1, 
            "description":"Description test", 
            "status":True, 
            "creation_date":datetime.today().strftime('%Y-%m-%d')
            }])

    def test_update_book(self):
        """update list"""

        client = APIClient()
        response = client.put('/updateTodoList/1/', {
	        "description":"Descripcion de listados"
            },
            format='multipart')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {
            "id":1, 
            "description":"Descripcion de listados", 
            "status":True, 
            "creation_date":datetime.today().strftime('%Y-%m-%d')
            })

    def test_update_status(self):
        """update status"""

        client = APIClient()
        response = client.put('/updateStatus/1/',
            format='multipart')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {
            "id":1, 
            "description":"Description test", 
            "status":True, 
            "creation_date":datetime.today().strftime('%Y-%m-%d')
            })


    def test_delete_book(self):
        """delete list"""

        client = APIClient()
        response = client.delete('/deleteTodoList/1/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), "El id 1 fue eliminado con exito")