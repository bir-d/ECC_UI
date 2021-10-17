from django.test import TestCase
from projectapp.models import Light, Video_Wall, Workstation, Display, Media, Preset
#from factory import DjangoModelFactory, Faker
# Create your tests here.

#Tests for Light Model
class LightModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # setUpTestData: Run once to set up non-modified data for all class methods
        Light.objects.create(id=1, name='abc123', colour='green123', brightness=50, light_on=True, selected=False)
        Light.objects.create(id=2, name='cde123', colour='blue123', brightness=1, light_on=False, selected=False)

        #Testing Model value integrity
    def test_name_value(self):
        light1 = Light.objects.get(id=1)
        given_value = light1.getname()
        self.assertEqual(given_value, 'abc123')   

    def test_colour_value(self):
        light1 = Light.objects.get(id=1)
        given_value = light1.getcolour()
        self.assertEqual(given_value, 'green123')


    def test_brightness_value(self):
        light1 = Light.objects.get(id=2)
        given_value = light1.getbrightness()
        self.assertEqual(given_value, 1) 

    def test_light_on_value(self):
        light1 = Light.objects.get(id=2)
        given_value = light1.getlight_on()
        self.assertFalse(given_value)

    def test_selected_value(self):
        light1 = Light.objects.get(id=1)
        given_value = light1.getselected()
        self.assertFalse(given_value)                

        #testing value constraints
    def test_name_max_length(self):
        light1 = Light.objects.get(id=1)
        max_length = light1._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)
        
    def test_colour_max_length(self):
        light1 = Light.objects.get(id=1)
        max_length = light1._meta.get_field('colour').max_length
        self.assertEqual(max_length, 20)        

#Tests for Video_Wall Model
class VideoWallTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # setUpTestData: Run once to set up non-modified data for all class methods
        Video_Wall.objects.create(id=1, media_name='Title1', media_type='video', source='zzz555', wall_on=True)
        Video_Wall.objects.create(id=2, media_name='Title2', media_type='picture', source='123qwe', wall_on=False)

        #Testing Model value integrity
    def test_video_wall_value(self):
        vw = Video_Wall.objects.get(id=1)
        given_value = vw.getmedia_name()
        self.assertEqual(given_value, 'Title1')   

    def test_media_type_value(self):
        vw = Video_Wall.objects.get(id=2)
        given_value = vw.getmedia_type()
        self.assertEqual(given_value, 'picture')


    def test_source_value(self):
        vw = Video_Wall.objects.get(id=1)
        given_value = vw.getsource()
        self.assertEqual(given_value, 'zzz555') 

    def test_wall_on_value(self):
        vw = Video_Wall.objects.get(id=2)
        given_value = vw.getwall_on()
        self.assertFalse(given_value)

        #testing value constraints
    def test_media_name_max_length(self):
        vw = Video_Wall.objects.get(id=1)
        max_length = vw._meta.get_field('media_name').max_length
        self.assertEqual(max_length, 255)

    def test_media_type_max_length(self):
        vw = Video_Wall.objects.get(id=1)
        max_length = vw._meta.get_field('media_type').max_length
        self.assertEqual(max_length, 255)
        
    def test_colour_max_length(self):
        vw = Video_Wall.objects.get(id=1)
        max_length = vw._meta.get_field('source').max_length
        self.assertEqual(max_length, 255) 