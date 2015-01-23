from django.db import models

CATEGORIES = (
    ('Music', 'Music'),
    ('Movie', 'Movie'),
    ('TV', 'TV'),
    ('LifeStyle', 'LifeStyle'),
)

class Posts(models.Model):
    post_number = models.IntegerField()
    title = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    category = models.CharField(max_length=30, choices=CATEGORIES)
    thumbnail = models.FileField(upload_to="./amaztv_app/static/data/", max_length=1000)
    sourceUrl = models.URLField(max_length=500)
    description = models.TextField(blank=True)
    embed_link = models.TextField(max_length=2000, blank=True)
    img_link = models.ImageField(upload_to="./amaztv_app/static/data/", max_length=1000, blank=True)
    tags = models.CharField(max_length=500)
    

    def __str__(self):
        return self.title