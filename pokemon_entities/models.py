from django.db import models  

class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    image = models.ImageField(upload_to='pokemon_pics/', blank=True, null=True, verbose_name='Изображение')

    def __str__(self):
        return f'{self.title}'
    

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name='Покемон')
    Lat = models.FloatField()
    Lon = models.FloatField()
    Appeared_at = models.DateTimeField(null=True)
    Disappeared_at = models.DateTimeField(null=True)
    Level = models.IntegerField(null=True, verbose_name='Уровень')
    Health = models.IntegerField(null=True, verbose_name='Здоровье')
    Strength = models.IntegerField(null=True, verbose_name='Атака')
    Defence = models.IntegerField(null=True, verbose_name='Защита')
    Stamina = models.IntegerField(null=True, verbose_name='Выносливость')
    
    def __str__(self):
        return f'{self.pokemon.title}'
