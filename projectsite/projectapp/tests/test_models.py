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

#Tests for Workstation Model
class WorkstationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # setUpTestData: Run once to set up non-modified data for all class methods
        Workstation.objects.create(id=1, workstation_name='testname1', station_on=True, media_name='testmedianame1', media_type='mediatypetest1', source='abc123')
        Workstation.objects.create(id=2, workstation_name='testname2', station_on=False, media_name='testmedianame2', media_type='mediatypetest2', source='def456')
        #Testing Model value integrity
    def test_workstation__name_value(self):
        w1 = Workstation.objects.get(id=1)
        given_value = w1.getworkstation_name()
        self.assertEqual(given_value, 'testname1')   

    def test_station_on_value(self):
        w1 = Workstation.objects.get(id=2)
        given_value = w1.getstation_on()
        self.assertEqual(given_value, False)               

        #testing value constraints
        
    def test_source_max_length(self):
        w1 = Workstation.objects.get(id=1)
        max_length = w1._meta.get_field('source').max_length
        self.assertEqual(max_length, 255)         

#Tests for Dispaly Model
class DisplayModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # setUpTestData: Run once to set up non-modified data for all class methods
        Display.objects.create(id=1, display_name='testname1', display_on=True, media_name='testmedia1', media_type='testmediatype1', source='testsource1')
        Display.objects.create(id=2, display_name='testname2', display_on=False, media_name='testmedia2', media_type='testmediatype2', source='testsource2')
        #Testing Model value integrity
    def test_display__name_value(self):
        d1 = Display.objects.get(id=1)
        given_value = d1.getdisplay_name()
        self.assertEqual(given_value, 'testname1')   

    def test_display_on_value(self):
        d1 = Display.objects.get(id=2)
        given_value = d1.getdisplay_on()
        self.assertEqual(given_value, False)               

        #testing value constraints
    def test_dispaly_name_max_length(self):
        d1 = Display.objects.get(id=1)
        max_length = d1._meta.get_field('media_name').max_length
        self.assertEqual(max_length, 255)
        
    def test_source_max_length(self):
        d1 = Display.objects.get(id=1)
        max_length = d1._meta.get_field('source').max_length
        self.assertEqual(max_length, 255)  

#Tests for Media Model
class MediaModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # setUpTestData: Run once to set up non-modified data for all class methods
        Media.objects.create(id=1, media_name='testmedianame1', media_type='testmediatype1', source='sourcetest1') 
        Media.objects.create(id=2, media_name='testmedianame2', media_type='testmediatype2', source='sourcetest2') 
        #Testing Model value integrity
    def test_media__name_value(self):
        m1 = Media.objects.get(id=1)
        given_value = m1.getmedia_name()
        self.assertEqual(given_value, 'testmedianame1')   

    def test_source_value(self):
        m1 = Media.objects.get(id=2)
        given_value = m1.getsource()
        self.assertEqual(given_value, 'sourcetest2')               

        #testing value constraints  
    def test_source_max_length(self):
        m1 = Media.objects.get(id=1)
        max_length = m1._meta.get_field('source').max_length
        self.assertEqual(max_length, 255)  


#Tests for Preset Model
class PresetModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # setUpTestData: Run once to set up non-modified data for all class methods
        Preset.objects.create(id=1, preset_name='testpresetname1', lights= {'lightstest': 1, 2: 'result'}, video_Wall= {'videowalltest': 1, 2: 'result'}, workstations= {'workstationtest': 1, 2: 'result'}, displays= {'dispalytest': 1, 2: 'result'})
        Preset.objects.create(id=2, preset_name='testpresetname2', lights= {'lightstest2': 3, 4: 'result2'}, video_Wall= {'videowalltest2': 3, 4: 'result2'}, workstations= {'workstationtest2': 3, 4: 'result2'}, displays= {'dispalytest2': 3, 4: 'result2'})
        #Testing Model value integrity
    def test_preset_name_value(self):
        p1 = Preset.objects.get(id=1)
        given_value = p1.getpreset_name()
        self.assertEqual(given_value, 'testpresetname1')   

        #Tests django handling of incorrect JSONfield entry
    def test_lights_preset_value(self):
        p1 = Preset.objects.get(id=2)
        given_value = p1.getlights()
        print(given_value)
        self.assertEqual(given_value, {'lightstest2': 3, '4': 'result2'})               

        #testing value constraints
    def test_preset_name_max_length(self):
        p1 = Preset.objects.get(id=1)
        max_length = p1._meta.get_field('preset_name').max_length
        self.assertEqual(max_length, 255) 