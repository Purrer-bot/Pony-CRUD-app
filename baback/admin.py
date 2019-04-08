from django.contrib import admin
from .models import Owner
from .models import Lab
from .models import Color
from .models import Genotype
from .models import Horse
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from baback.models import CustomUser



# Register your models here.

admin.site.register(Owner)
admin.site.register(Horse)
admin.site.register(Color)
admin.site.register(Genotype)
admin.site.register(Lab)


#Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class CustomInLine(admin.StackedInline):
    model = CustomUser
    can_delete = False
    verbose_name_plural = 'customuser'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (CustomInLine,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
