from django.db import models  

class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    image = models.ImageField(upload_to='pokemon_pics/', blank=True, null=True, verbose_name='Изображение')

    def __str__(self):
        return f'{self.title}'
    

class PokemonEntity(models.Model):
    Lat = models.FloatField()
    Lon = models.FloatField()
