from django.test import TestCase
from . models import Image,location,category

class ImageTestClass(TestCase):
    '''
    Test class for testing Image Class
    '''
    def setUp(self):
        self.image = Image(name = 'Test Image',description = 'This is a random test image')
        self.image.save_image()

        self.new_category = category(name = 'testing')
        self.new_category.save()

        self.new_location = location(name = 'testing')
        self.new_location.save()

        self.image.category.add(self.new_category)
        self.image.location.add(self.new_location)

    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))
         
    def test_save_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_get_images_by_id(self):
        test_id = '3'
        images = Image.get_image_by_id(test_id)
        self.assertTrue(len(images) == 0)

    def tearDown(self):
        Image.objects.all().delete()
        category.objects.all().delete()
        location.objects.all().delete()
