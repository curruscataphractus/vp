
from datetime import date, datetime

from django.db.models import Model as DBModel, AutoField, CharField, PositiveIntegerField, ForeignKey,\
     EmailField, DateField, PositiveSmallIntegerField, TextField

from django.utils.translation import ugettext as _


class Brand(DBModel):
    id = AutoField(primary_key=True)
    name = CharField(_('name'), help_text=_('Brand name'), max_length=50, unique=True)

    class Meta:
        verbose_name = _('brand')
        verbose_name_plural = _('brands')

    def __str__(self):
        return '<Brand: %s>' % (self.name)

    def __repr__(self):
        return self.__str__()

    def __unicode__(self):
        return self.name

class Model(DBModel):
    id = AutoField(primary_key=True)
    name = CharField(_('name'), help_text=_('Model name'), max_length=50, unique=True)
    cc = PositiveIntegerField(_('Cubic centimeters'), help_text=_('Cubic centimeters'), blank=True)
    year = PositiveIntegerField(_('year'), help_text=_('Model year'), blank=True)
    
    brand = ForeignKey('Brand', verbose_name=_('brand'))

    class Meta:
        verbose_name = _('model')
        verbose_name_plural = _('models')


    def __str__(self):
        return '<Model: %s, brand: %s, cc: %d, year: %d>' % (self.name, self.brand.name,
                                                             self.cc, self.year)

    def __repr__(self):
        return self.__str__()

    def __unicode__(self):
        ret = self.name
        if self.cc is not None and self.cc > 0:
            ret += ' - %d cc' % self.cc
        if self.year is not None and self.year > 0:
            ret += ' - %d' % self.year
        
        return ret


class Client(DBModel):
    id = AutoField(primary_key=True)
    first_name = CharField(_('First name'), help_text=_('First name'), max_length=100)
    last_name = CharField(_('Last name'), help_text=_('Last name'), max_length=100)
    id_no = CharField(_('Id #'), help_text=_('ID'), max_length=50, unique=True, blank=True)
    address = CharField(_('Address'), help_text=_('Postal address'), blank=True, null=True, max_length=100)
    zip_code = PositiveSmallIntegerField(_('Zip code'), help_text=_('Address zip code'), blank=True, null=True)
    email = EmailField(unique=True, blank=True)
    file_no = CharField(_('File #'), help_text=_('Internal file #'), max_length=50, unique=True, blank=True)
    notes = TextField(_('Notes'), help_text=_('Notes'))
    
    class Meta:
        verbose_name = _('client')
        verbose_name_plural = _('clients')


    def __str__(self):
        return '<Client: %s %s, id: %s, file_no: %s>' % (self.first_name, self.last_name,
                                                         self.id_no, self.file_no)
        

    def __repr__(self):
        return self.__str__()

    def __unicode__(self):
        return '%s, %s (%s)' % (self.last_name, self.first_name, self.file_no)



BIKE_TYPE = (
    ('N', _('New')),
    ('U', _('Used')),
    )
    
BIKE_STATE = (
    ('ST', _('Stored')),
    ('PP', _('Pre paid')),
    ('SD', _('Sold')),
    )

class Invoice(DBModel):
    id = AutoField(primary_key=True)
    number = CharField(_('Invoice #'), help_text=_('Invoice #'), unique=True, null=False, max_length=70)
    date = DateField(_('Date'), help_text=_('Date'), null=False, default=date.today())

    client = ForeignKey('Client', verbose_name=_('client'))
    
    class Meta:
        verbose_name = _('invoice')
        verbose_name_plural = _('invoice')


    def __str__(self):
        return '<Invoice: %s, date: %s>' % (self.number, self.date)
                                            

    def __repr__(self):
        return self.__str__()

    def __unicode__(self):
        ret = '%s' % (self.number)
        if self.client is not None:
            ret += self.client
        return ret
    
class Bike(DBModel):
    id = AutoField(primary_key=True)
    serial = CharField(_('Serial'), help_text=_('Bike serial'), unique=True, null=False, max_length=70)
    color = CharField(_('Color'), help_text=_('Color'), max_length=70)
    key_code = CharField(_('Key code'), help_text=_('Key code'), unique=True, null=False, max_length=10)
    plate = CharField(_('plate'), help_text=_('Plate'), max_length=16, unique=True, null=True, blank=True)
    source = CharField(_('Source'), help_text=_('Bike source'), max_length=1, choices=BIKE_TYPE, default='N')
    state = CharField(_('State'), help_text=_('Bike state'), max_length=2, choices=BIKE_STATE, default='ST')

    model = ForeignKey('Model', verbose_name=_('model'))
    client = ForeignKey('Client', verbose_name=_('client'), null=True, blank=True)
    invoice = ForeignKey('Invoice', verbose_name=_('invoice'), null=True, blank=True)
    
    class Meta:
        verbose_name = _('bike')
        verbose_name_plural = _('bikes')


    def __str__(self):
        return '<Model: %s, brand: %s, cc: %d, year: %d>' % (self.name, self.brand.name,
                                                             self.cc, self.year)

    def __repr__(self):
        return self.__str__()

    def __unicode__(self):
        ret = ''
        if self.plate is not None:
            ret += self.plate + ' - '
        ret += '%s' % self.model
        return ret         
        
    

