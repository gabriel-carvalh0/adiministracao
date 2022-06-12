from django.db import models
from django.db.models.fields import DateTimeField
from django.urls import reverse

# Create your models here.

class Category(models.Model):

	name = models.CharField('Nome', max_length=100, unique=True)
	slug = models.SlugField('identificador', max_length=100, unique=True)

	created = models.DateTimeField('Criado em:', auto_now_add= True)
	modified = models.DateTimeField('Modificado em:', auto_now_add= True)

	class Meta:
		verbose_name = 'Categoria'
		verbose_name_plural = 'Categorias'
		ordering = ['name']

	def __str__(self):
		return self.name





class Anime(models.Model):
    name = models.CharField('Nome', max_length=100, unique=True)
    slug = models.SlugField('Identificador', max_length=100, unique=True)
    category = models.ForeignKey('core.Category', on_delete=models.CASCADE)
    description = models.TextField('Descrição', blank=True)
    tempo = models.DecimalField('Tempo', decimal_places=2, max_digits=8)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models,DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Anime'
        verbose_name_plural = 'Animes'
        ordering = ['name']

    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('core:Anime', kwargs={'slug': self.slug})