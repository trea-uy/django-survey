from django.core.exceptions import ValidationError

from dynamicForms.fieldtypes.Field import Field
from dynamicForms.statistics.ListStatistics import ListStatistics

class ListField(Field):
    """
    List field validator, render and analize methods
    """
    def get_methods(self, **kwargs):
        base = super(ListField, self).get_methods(**kwargs)
        base.append(self.belong_check)    
        return base
    
    def belong_check(self, value, **kwargs):
        v = int(value)
        top = int(kwargs['options'])
        if not (v > 0 and v <= top):
            raise ValidationError("Invalid value, not among options.")
        
    
    def check_consistency(self, **kwargs):
        options = kwargs['options']
        if (options == []):
            raise ValidationError("List fields need at least one option.")
    
    def get_option_labels(self, field):
        options = []
        for option in field['options']:
            options.append(option['label'])            
        return options
    
    def get_statistics(self, data_list, field):
        options = self.get_options_labels(field)
        listStatistics = ListStatistics(data_list,options)
        return listStatistics.getSerializedData()

    def get_options(self, json, f_id):
        for page in json['pages']:
            for field in page['fields']:
                if (field['field_id'] == f_id):
                    return field['max_id']
                
        


    class Meta:
        abstract = True
