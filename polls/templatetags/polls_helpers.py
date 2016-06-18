from django import template

register = template.Library()

from dateutil.relativedelta import relativedelta
import datetime

@register.simple_tag(takes_context=False)
def jeden(value): 
    today = datetime.date.today()
    delta = relativedelta(today, value)
    return str(delta.years)
    

@register.simple_tag(takes_context=False)
def allowed(choice): 
    age = int(jeden(choice.dob))
    if age > 13:
        return 'ALLOWED'
    else:
        return 'BLOCKED'
    
def BizzFuzz(i):
        if i % 3 == 0:
            o = 'Bizz'
        elif i % 5 == 0:
            o = 'Fuzz'
        else:
            o = i
        if i % 3 == 0 and i % 5 == 0:
            o = 'BizzFuzz'
        return o


@register.simple_tag(takes_context=False)
def BizzFuzzTag(number): 
    return BizzFuzz(number)
