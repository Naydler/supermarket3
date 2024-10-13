from django.db import models

# El campo default_price = models.DecimalField, que estaba en el diagrama no lo he añadido, creo que es un
#campo que deberia ir en producto, aqui añadiria el campo "si tenemos o no descuentos -->discount"
class Supplier(models.Model):
    name = models.CharField(max_length=200)
    web_link = models.CharField(max_length=200)
    address = models.CharField(max_length=255)  
    email = models.EmailField(max_length=255)  
    phone = models.CharField(max_length=20)  
    nif = models.CharField(max_length=15)

    def __str__(self):
        return self.name

