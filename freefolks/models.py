from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

""" Excepton handling """
class ModelManager(models.Manager):
	def get_or_none(self, **kwargs):
		try:
			return self.get(**kwargs)
		except ObjectDoesNotExist:
			return None

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class DynamicOption(models.Model):
	objects = ModelManager()
	FIELDS = [(p['key'], p['value']) for p in settings.APP_CONSTANTS['FIELDS']]
	field_name = models.CharField(max_length=50,null=False,choices=FIELDS,verbose_name="Form field name")
	value = models.CharField(max_length=50,null=False, verbose_name="Form field value")
	description = models.CharField(max_length=50,null=False, verbose_name="Form field description")

	def __unicode__(self):
		return self.description

class Account(BaseModel):
	objects = ModelManager()
	BANKS = [(t.value, t.description) for t in DynamicOption.objects.filter(field_name="bank")]
	user_name = models.CharField(max_length=50,null=False, verbose_name="User name")
	bank_name = models.CharField(max_length=50,null=False, choices=BANKS, verbose_name="Select your bank")
	branch = models.CharField(max_length=200,null=False, verbose_name="Branch name")
	account_number = models.CharField(max_length=200,null=True, blank=True, verbose_name="Account number")
	access_user = models.ForeignKey(User)

	def __unicode__(self):
		return self.user_name

class Transaction(BaseModel):
	objects = ModelManager()
	TRANSACTION_TYPE = [(t.value, t.description) for t in DynamicOption.objects.filter(field_name="transaction_type")]
	title = models.CharField(max_length=50, null=False, verbose_name="Title")
	account = models.ForeignKey(Account, null=False)
	transaction_type = models.CharField(max_length=50, choices=TRANSACTION_TYPE, null=False, verbose_name="Transaction type")
	amount = models.DecimalField(default=0.0, null=False, decimal_places=2, max_digits=12, verbose_name="Transaction amount")
	date_time = models.DateTimeField(auto_now_add=False, blank=True, null=True, verbose_name="Transaction date")
	access_user = models.ForeignKey(User)

	def __unicode__(self):
		return self.title

class Vendor(BaseModel):
	objects = ModelManager()
	name = models.CharField(max_length=50, null=False, verbose_name="Vendor name")
	phone = models.CharField(max_length=50, null=True, blank=True, verbose_name="Vendor phone number")
	address = models.TextField(null=True, blank=True, verbose_name="Address")

	def __unicode__(self):
		return self.name

class Stockpile(BaseModel):
	objects = ModelManager()
	title = models.CharField(max_length=50, null=False, verbose_name="Title for stockpile")
	stockpile_date = models.DateTimeField(auto_now_add=False, blank=True, null=True, verbose_name="Stockpile date")
	grand_total =  models.DecimalField(default=0.0, null=False, decimal_places=2, max_digits=12, verbose_name="Stockpile amount")
	number_of_stockpile = models.IntegerField(default=20, null=False,verbose_name="Number of Stockpile")
	description = models.TextField(null=True, blank=True, verbose_name="Description of Stockpile")
	vendor = models.ForeignKey(Vendor)
	access_user = models.ForeignKey(User)

	def __unicode__(self):
		return self.title

class Stockpiling(BaseModel):
	objects = ModelManager()
	NUMBERS = [(i+1,"stockpile_"+str(i+1)) for i in range(20)]
	stockpile = models.ForeignKey(Stockpile)
	title = models.CharField(max_length=50, null=False, verbose_name="Title for stockpile with month")
	stockpile_number = models.CharField(max_length=50, choices=NUMBERS, null=False, verbose_name="Transaction type")
	amount_paid =  models.DecimalField(default=0.0, null=False, decimal_places=2, max_digits=12, verbose_name="Stockpile amount paid")
	grand_taken =  models.DecimalField(default=0.0, null=True,blank=True, decimal_places=2, max_digits=12, verbose_name="Stockpile amount paid")
	stockpile_month = models.DateTimeField(auto_now_add=False, blank=True, null=True, verbose_name="Stockpile monthly date")
	class Meta:
		unique_together = ('stockpile', 'stockpile_number',)
	def __unicode__(self):
		return self.title





	
		


