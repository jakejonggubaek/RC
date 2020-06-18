from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.ClothCategory)
class ClothCategoryAdmin(admin.ModelAdmin):
    """Cloth Category admin definition"""

    pass


@admin.register(models.ClothColor)
class ClothColorAdmin(admin.ModelAdmin):
    """Cloth Color admin definition"""

    pass


@admin.register(models.ClothSize)
class ClothSizeAdmin(admin.ModelAdmin):
    """Cloth Size admin definition"""

    pass


class photoInline(admin.TabularInline):
    model = models.Photo


@admin.register(models.Cloth)
class ClothAdmin(admin.ModelAdmin):
    """Cloth admin definition"""

    inlines = [
        photoInline,
    ]
    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Photo admin definition"""

    pass
