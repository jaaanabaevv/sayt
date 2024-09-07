from django.db import models
from django.contrib.auth.models import User
class Category(models.Model):
    category_name = models.CharField(
        verbose_name='Kategoriyasi:',
        max_length=255,)
    category_slug = models.SlugField(
        verbose_name='Slug:',
        max_length=255,
        unique=True
    )

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'
    def __str__(self) -> str:
        return self.category_name


class movies(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='kinonin avtori')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    title = models.CharField(max_length=255,verbose_name='kinonin ati : ')
    actors = models.TextField(verbose_name='kinoda oynagan actyorlar: ')
    image1 = models.ImageField(verbose_name='постер:',blank=True,null=True,)
    pub_date = models.DateField(verbose_name='Kinonin shiqqan waqiti:',)
    country = models.CharField(verbose_name='Kino tusirilgen mamleket:',max_length=255)
    
    movie = models.FileField(upload_to='media/movies',verbose_name='Kinonin ozi:')

    class Meta:
        verbose_name = 'kino'
        verbose_name_plural = 'kinolar'
    def __str__(self) -> str:
        return self.title

class Janr(models.Model):
    janr_name = models.CharField(
        verbose_name='Janri:',
        max_length=255,)
    janr_slug = models.SlugField(
        verbose_name='Slug:',
        max_length=255,
        unique=True
    )
    
    class Meta:
        verbose_name = 'Janr'
        verbose_name_plural = 'Janrlar'
    def __str__(self) -> str:
        return self.janr_name


class Comments(models.Model):
    text = models.TextField(verbose_name='Komment text:')
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    movie = models.ForeignKey(movies,on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True,verbose_name='Qosilgan waqit')
