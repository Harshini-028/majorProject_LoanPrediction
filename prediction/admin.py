from django.contrib import admin

# Register your models here.
from .models import Formerdata,District, Taluk, Hobali, Village, Surveynumber, HissaNO, Peroid, Owner

admin.site.register(Formerdata)
admin.site.register(District)
admin.site.register(Taluk)
admin.site.register(Hobali)
admin.site.register(Village)
admin.site.register(Surveynumber)
admin.site.register(HissaNO)
admin.site.register(Peroid)
admin.site.register(Owner)
