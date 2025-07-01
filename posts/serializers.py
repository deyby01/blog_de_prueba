from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Post. Lo que hace es convertir nuestros datos u objetos post 
    a formatos JSON o similares.
    En la clase meta le indicamos el modelo y los campos que queremos serializar.
    """
    class Meta:
        model = Post
        fields = ('id', 'titulo', 'contenido', 'autor', 'fecha_publicacion')