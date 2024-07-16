from django.test import TestCase
from reviews.models import Critico
from reviews.serializers import CriticoSerializer
from django.core.files.uploadedfile import SimpleUploadedFile
import os

class CriticoSerializerTestCase(TestCase):

    def setUp(self):
        # Acessar a simulação de um vídeo e de uma imagem para os testes
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        media_root = os.path.join(base_dir, 'media_root')
        image_path = os.path.join(media_root, 'isabelaboscov.jpg')
        video_path = os.path.join(media_root, 'The_Last_of_Us__ep._1__então_é_assim_que_se_faz_VKXbsHY.mp4')

        with open(image_path, 'rb') as image_file:
            foto_simulada = SimpleUploadedFile(
                name='isabelaboscov.jpg',
                content=image_file.read(), 
                content_type='image/jpeg'
            )
        
        with open(video_path, 'rb') as video_file:
            video_simulado = SimpleUploadedFile(
                name='The_Last_of_Us__ep._1__então_é_assim_que_se_faz.mp4',     
                content=video_file.read(), 
                content_type='video/mp4'
            )

        self.programa = Critico.objects.create(
            nome = 'Jp',
            foto = foto_simulada,
            email = 'joao@gmail.com',
            descricao = 'Crítico',
            review = 'Batman é bom',
            video = video_simulado
        )
        self.serializer = CriticoSerializer(instance=self.programa)

    def test_verifica_campos(self):
        """Teste que verifica os campos que estão sendo serializados"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'nome', 'foto', 'email', 'descricao', 'review', 'video']))

    def test_verifica_conteudo_campos(self):
        """Teste que verifica o conteúdo dos campos serializados"""
        data = self.serializer.data
        self.assertEqual(data['id'], self.programa.id)
        self.assertEqual(data['nome'], self.programa.nome)
        self.assertEqual(data['foto'], self.programa.foto.url)
        self.assertEqual(data['email'], self.programa.email)
        self.assertEqual(data['descricao'], self.programa.descricao)
        self.assertEqual(data['review'], self.programa.review)
        self.assertEqual(data['video'], self.programa.video.url)