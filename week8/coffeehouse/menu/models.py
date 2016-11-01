from django.db import models

class Special(models.Model):
    created_user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    picture = models.FileField()

    @property
    def image_url(self):
        if self.picture:
            return self.picture.url
        return "http://www.publicdomainpictures.net/pictures/10000/velka/coffee-latte-11284391087Ksg2.jpg"
    # this property is necessary for two cases:
        # if you add this FileField after migrating the model
        # or if adding an image is optional so you have a default until the file is changed/added
