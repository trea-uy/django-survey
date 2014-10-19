from django.core.exceptions import ValidationError

from dynamicForms.fieldtypes.Field import Field


class ListField(Field):
    """
    List field validator, render and analize methods
    """
    def get_methods(self, **kwargs):
        base = super(ListField, self).get_methods(**kwargs)
        base.append(self.belong_check)    
        return base
    
    def belong_check(self, value, **kwargs):
        pass
    
    def check_consistency(self, **kwargs):
        options = kwargs['options']
        if (options == []):
            raise ValidationError("List fields need at least one option.")
       
    class Meta:
        abstract = True