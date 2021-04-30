from django.contrib import admin
from .models import *


admin.site.register(Invoices)
admin.site.register(Quotes)
admin.site.register(Article_Inv)
admin.site.register(Article_Quotes)
admin.site.register(PaymentsMethods)



