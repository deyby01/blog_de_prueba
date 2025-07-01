from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post
from django.urls import reverse

# Create your tests here.
class PostModelTest(TestCase):
    
    def setUp(self):
        """ 
        Este metodo es especial se ejecuta ANTES de cada metodo de prueba.
        Es perfecto para crear los objetos que usaremos en las pruebas.
        """
        User.objects.create_user(username='testuser', password='testpass')
        Post.objects.create(
            titulo='Un titulo de prueba',
            contenido='Contenido de prueba',
            autor=User.objects.get(id=1)
        )
        
    def test_contenido_de_titulo(self):
        """ 
        Nuestra primera prueba. Comprueba que el titulo del post se guardo bien.
        """
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.titulo}'
        self.assertEqual(expected_object_name, 'Un titulo de prueba')
        
        
        
class PostViewTest(TestCase):
    
    def setUp(self):
        """ 
        Creamos un usuario y un post para usar en las pruebas de las vistas.
        """
        test_user = User.objects.create_user(username='testuser', password='testpass')
        Post.objects.create(
            id=1,
            titulo='Titulo prueba1',
            contenido='Contenido de prueba1',
            autor=test_user
        )
        
    def test_vista_lista_posts(self):
        """ 
        Prueba la vista de la lista de posts (la pagina principal del blog.)
        """
        response = self.client.get(reverse('post_list'))# Visitamos la url
        
        self.assertEqual(response.status_code, 200) # Comprobamos que la respuesta es 200 (OK)
        self.assertContains(response, 'Titulo prueba1') # Comprobamos que el contenido de la pagina contiene el titulo del post
        self.assertTemplateUsed(response, 'posts/post_list.html') # Comprobamos que se usa la plantilla correcta
        
    def test_vista_detalle_post(self):
        """
        Prueba la vista de detalle para un post especifico
        """
        post = Post.objects.get(id=1) # Obtenemos el post que creamos en setUp
        response = self.client.get(reverse('post_detail', args=[str(post.id)])) # Visitamos la url del detalle del post
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Titulo prueba1') # Comprobamos que el contenido de la pagina contiene el titulo del post
        self.assertTemplateUsed(response, 'posts/post_detail.html') # Comprobamos que se usa la plantilla correcta