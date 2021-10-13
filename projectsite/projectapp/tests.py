from django.test import TestCase
from models import Light
from factory import DjangoModelFactory, Faker
# Create your tests here.

class Light(DjangoModelFactory):
    id = Faker('1')
    name = Faker('text')
    colour = Faker('FFFFFF')
    brightness = Faker(100)
    light_on = Faker(True)
    selected = Faker(True)

    class Meta:
        model = Light

class LightTestCase(TestCase):
    def test_str(self):
        light = Light()
        self.assertEqual(str(light), light.name )
