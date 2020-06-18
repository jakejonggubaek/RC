from django.db import models
from core import models as core_models

# Create your models here.


class AbstractItem(core_models.TimeStampedModel):

    name = models.CharField(max_length=80)

    class Meta:

        abstract = True

    def __str__(self):
        return self.name


class ClothCategory(AbstractItem):
    class Meta:

        verbose_name = "Cloth Category"
        ordering = ["created"]


class ClothColor(AbstractItem):
    class Meta:

        verbose_name = "Cloth Color"
        ordering = ["created"]


class ClothSize(AbstractItem):
    class Meta:

        verbose_name = "Cloth Size"
        ordering = ["created"]


class Cloth(core_models.TimeStampedModel):

    """Cloth model definition"""

    name = models.CharField(max_length=80)
    category = models.ManyToManyField(ClothCategory, related_name="clothes", blank=True)
    description = models.TextField()
    color = models.ManyToManyField(ClothColor, related_name="clothes", blank=True)
    size = models.ManyToManyField(ClothSize, related_name="clothes", blank=True)
    fabric = models.CharField(max_length=40)
    is_new = models.BooleanField(default=True)
    price = models.IntegerField()
    available_date = models.DateField()

    def __str__(self):
        return self.name


class Photo(core_models.TimeStampedModel):

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="cloth_photos")
    cloth = models.ForeignKey(Cloth, related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
