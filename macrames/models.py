from django.db import models


class Category(models.Model):
    """ A category of the products with a user-friendly name """

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=250)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        """ A method to show name of the category """
        return self.name

    def get_friendly_name(self):
        """ A method to show user-friendly name of the categories """
        return self.friendly_name


class Macrame(models.Model):
    """ A class for macrame items """
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ImageField(null=False, blank=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        """ A method to show the name of the product  """
        return self.name