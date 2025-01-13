from django.contrib import admin

# Register your models here.


from .models import Questionpolls,Choicepolls

admin.site.register(Questionpolls)
admin.site.register(Choicepolls)


