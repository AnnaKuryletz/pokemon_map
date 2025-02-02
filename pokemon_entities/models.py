from django.db import models   

class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200, verbose_name='Название покемона на русском')  
    title_en = models.CharField(blank=True, max_length=200, verbose_name='Название покемона на английском')  
    title_jp = models.CharField(blank=True, max_length=200, verbose_name='Название покемона на японском')  
    image = models.ImageField(upload_to='pokemon_pics/', blank=True, null=True, verbose_name='Изображение')  
    description = models.TextField(blank=True, verbose_name="Описание")  
    previous_evolution = models.ForeignKey('Pokemon', on_delete=models.SET_NULL, null=True, blank=True,  
                                           related_name='next_evolutions', verbose_name='Предыдущая эволюция покемона')  

    def __str__(self):  
        return f'{self.title_ru}'  


class PokemonEntity(models.Model):   
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name='покемон', related_name='entities') 
    lat = models.FloatField(verbose_name='Широта')  
    lon = models.FloatField(verbose_name='Долгота')  
    appeared_at = models.DateTimeField(verbose_name='Когда появился')    
    disappeared_at = models.DateTimeField(null=True, blank=True, verbose_name='Когда исчез')    
    level = models.IntegerField(null=True, blank=True, verbose_name='Уровень')  
    health = models.IntegerField(null=True, blank=True, verbose_name='Здоровье')  
    strength = models.IntegerField(null=True, blank=True, verbose_name='Атака')  
    defence = models.IntegerField(null=True, blank=True, verbose_name='Защита')  
    stamina = models.IntegerField(null=True, blank=True, verbose_name='Выносливость')  

    def __str__(self):  
        return f'{self.pokemon.title_ru}'  
