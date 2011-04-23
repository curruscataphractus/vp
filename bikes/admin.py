
from bikes.models import Brand, Model, Client, Invoice, Bike
from django.contrib import admin

from django.utils.translation import ugettext as _

## class ClientAdmin(admin.ModelAdmin):

##     def formfield_for_foreignkey(self, db_field, request, **kwargs):
##         if db_field.name == "":
##             kwargs["queryset"] = Car.objects.filter(owner=request.user)
##             return super(MyModelAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

class ChoiceInline(admin.StackedInline):
    model = Bike
    extra = 1

class InvoiceAdmin(admin.ModelAdmin):
    fields = ['date', 'number', 'client', 'bike']
    list_display = ('date','number', 'client')
    search_fields = ['number', 'date']
    # inlines = [ChoiceInline]

class BikeAdmin(admin.ModelAdmin):
    list_display = ('model', 'plate', 'client')

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ModelAdmin(admin.ModelAdmin):
    list_display = ('brand', 'name', 'year', 'cc',)

class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'file_no', 'id_no')

admin.site.register(Brand, BrandAdmin)
admin.site.register(Model, ModelAdmin)
admin.site.register(Client, ClientAdmin)
# admin.site.register(Client, ClientAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Bike, BikeAdmin)
