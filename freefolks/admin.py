from django.contrib import admin
from .models import DynamicOption, Account, Transaction, Vendor,Stockpile,Stockpiling

# Register your models here.
class DynamicOptionAdmin(admin.ModelAdmin):
    list_display=('field_name','description')

class AccountAdmin(admin.ModelAdmin):
    list_display=('user_name','bank_name', 'created_date','modified_date')

class TransactionAdmin(admin.ModelAdmin):
    list_display=('title','date_time', 'created_date','modified_date')    



admin.site.register(DynamicOption,DynamicOptionAdmin)
admin.site.register(Account,AccountAdmin)
admin.site.register(Transaction,TransactionAdmin)
admin.site.register(Vendor)
admin.site.register(Stockpile)
admin.site.register(Stockpiling)