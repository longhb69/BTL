from django.db import models
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.
CATEGORY_CHOICES = (
    ('Hành Động','Hành Động'),
    ('DRAMA','DRAMA'),
    ('Viễn Tưởng','Viễn Tưởng'),
    ('Trinh Thám', 'Trinh Thám')
)
STATUS_CHOICES = (
    ('RA', 'Gần Đây'),
    ('MW', 'Xem Nhiều Nhất'),
    ('TR', 'Lựa Chọn Hàng Đầu')
)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='movies')
    banner = models.ImageField(upload_to='movies_banner', blank=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10)
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)
    year_of_production = models.DateField()
    views_count = models.IntegerField(default=0)
    cast = models.CharField(max_length=100)
    movie_trailer = models.URLField()
    flim = models.FileField(upload_to='movies', blank=True) 
    subtitle = models.FileField(upload_to='subs',blank=True)
    imbd = models.FloatField(null=True)
    created = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(blank=True,null=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Movie, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    def get_year(self):
        return self.year_of_production.year

