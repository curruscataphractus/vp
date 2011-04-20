
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
    

admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Client)
# admin.site.register(Client, ClientAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Bike)
