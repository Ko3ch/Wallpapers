from django.db import models

class category(models.Model):
    '''
    class that defines a category object
    '''
    name = models.CharField(max_length =30,default='Wildlife')

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.name

class location(models.Model):
    '''
    class that defines a category object
    '''
    name = models.CharField(max_length =30)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def all_locations(cls):
        return cls.objects.all()

    def __str__(self):
        return self.name

class Image(models.Model):
    '''
    class that defines an instance of Image
    '''
    image_url = models.ImageField(upload_to='images/',null=True)
    name = models.CharField(max_length =30)
    description = models.CharField(max_length=50)
    category = models.ForeignKey(category,on_delete=models.CASCADE,null=True)
    location = models.ForeignKey(location,on_delete=models.CASCADE,null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class meta:
        ordering =['name']
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod 
    def all_images(cls):
        return cls.objects.all()

    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(id = id)
        return image

    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(category__name__icontains=search_term)
        return images
    
    @classmethod
    def images_by_location(cls,location):
        location_name = location.objects.get(name = location)
        images = cls.objects.filter(location=location_name.id)
        return images
    