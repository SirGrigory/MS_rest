from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'cities_table'
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.name

    # def get_absolut_url(self):
    #     return reverse('streets', (), self.pk)


class Street(models.Model):

    name = models.CharField(max_length=50)
    city = models.ForeignKey(
        City, related_name='street', on_delete=models.CASCADE)

    def natural_key(self):
        return(self.name,)

    def __str__(self):
        return self.name


class Shop(models.Model):

    name = models.CharField(max_length=50)
    street = models.ForeignKey(
        Street, related_name='shop', on_delete=models.CASCADE)
    house_num = models.IntegerField()
    opening_time = models.TimeField(auto_now=False, auto_now_add=False)
    closing_time = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name
