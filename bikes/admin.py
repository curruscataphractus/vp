
from bikes.models import Brand, Model, Client, Invoice, Bike
from django.contrib import admin

## class ClientAdmin(admin.ModelAdmin):

##     def formfield_for_foreignkey(self, db_field, request, **kwargs):
##         if db_field.name == "":
##             kwargs["queryset"] = Car.objects.filter(owner=request.user)
##             return super(MyModelAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Client)
# admin.site.register(Client, ClientAdmin)
admin.site.register(Invoice)
admin.site.register(Bike)
