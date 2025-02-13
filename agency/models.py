from django.db import models

class PortfolioItem1(models.Model):
    # Portfolio item fields
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='portfolio/')
    
    # Modal fields
    modal_id = models.SlugField(max_length=50, unique=True,null=True)
    project_title = models.CharField(max_length=200)
    intro_text = models.CharField(max_length=200, blank=True)
    modal_image = models.ImageField(upload_to='portfolio/modals/',null=True)
    description = models.TextField()
    client = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title