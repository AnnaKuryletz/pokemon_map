from django.db import models  

class Pokemon(models.Model):
    title_ru = models.CharField(null=True, blank=True, max_length=200, verbose_name='название покемона на русском')
    title_en = models.CharField(null=True, blank=True, max_length=200, verbose_name='название покемона на английском')
    title_jp = models.CharField(null=True, blank=True, max_length=200, verbose_name='название покемона на японском')
    image = models.ImageField(upload_to='pokemon_pics/', blank=True, null=True, verbose_name='Изображение')
    description = models.TextField(null=True, blank=True, verbose_name="описание")

    def __str__(self):
        return f'{self.title_ru}'
    

class PokemonEntity(models.Model): 
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name='Покемон')
    Lat = models.FloatField()
    Lon = models.FloatField()
    Appeared_at = models.DateTimeField(null=True, blank=True)  
    Disappeared_at = models.DateTimeField(null=True, blank=True)  
    Level = models.IntegerField(null=True, blank=True, verbose_name='Уровень')
    Health = models.IntegerField(null=True, blank=True, verbose_name='Здоровье')
    Strength = models.IntegerField(null=True, blank=True, verbose_name='Атака')
    Defence = models.IntegerField(null=True, blank=True, verbose_name='Защита')
    Stamina = models.IntegerField(null=True, blank=True, verbose_name='Выносливость')

    def __str__(self):
        return f'{self.pokemon.title_ru}'

