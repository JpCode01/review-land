from django.test import TestCase
from reviews.models import Critico

class ProgramaModelTestCase(TestCase):

    def setUp(self):
        self.programa = Critico(
            nome = 'Jp',
            email = 'joao@gmail.com',
            descricao = 'Crítico',
            review = 'Batman é bom'
        )

    def test_verifica_atributos_do_programa(self):
        """Teste verifica os atributos de um programa com valores default"""
        self.assertEqual(self.programa.nome, 'Jp')
        self.assertEqual(self.programa.email, 'joao@gmail.com')
        self.assertEqual(self.programa.descricao, 'Crítico')
        self.assertEqual(self.programa.review, 'Batman é bom')