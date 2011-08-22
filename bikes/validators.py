from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from re import compile 


def validate_id_no(value):
    r = compile(r'\d{8}-\w{1}')
    data = value.upper()
    if not r.match(data):
        raise ValidationError(_('Invalid Id number. Remember must be in the form 8 numbers followed by a letter'))

def validate_plate(value):
    r = compile(r'\d{4}-\w{3}')
    r_old = compile(r'\w{1,2}-\d{4}-\w{2}')
    data = value.upper()
    if not r.match(data):
        if not r_old.match(data):
            raise ValidationError(_('Invalid plate number. Remember must be in the form NNNN-LLL or LL-NNNN-LL for old ones'))

