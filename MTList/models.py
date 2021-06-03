from django.db import models


RECORD_CHOICES = (
	("NEW" , "New Account"),
	("EXISTING" , "Existing Account ")
	)

SERVICES_CHOICES = (
	("DENTAL" , "Dental Services"),
	("APE" , "Annual Physical Examination"),
	("OPCS" ,"Out-Patient Care Services" ),
	("IPCS" ,"In-Patient Care Services"),
	("ECT" , "Emergency Care Treatment"),
	("OTHERS" , "Additional Benefits")
	)
# Create your models here.

class CompanyProfile (models.Model):
	CName = models.TextField(default="")
	CAddress = models.TextField(default="")
	TNumber = models.CharField(default="",max_length=20)
	Emailemp = models.CharField(default="",max_length=30)
	class meta:
		db_table = "ccompanyprofile"

class CompanyEmployee(models.Model):
	NPatient  = models.TextField(default=None,)
	EIdnumber = models.CharField(default=None, max_length=20)
	HPosition = models.TextField(default="")
	Phealth = models.CharField(default=None, max_length=12)
	companyp = models.TextField(default="")
	class meta:
		db_table = "companyeemployee"

class MedicalOffers(models.Model):
	Services = models.CharField(max_length = 20, choices = SERVICES_CHOICES, default ="")
	Account = models.CharField(max_length = 20, choices = RECORD_CHOICES, default ="")
	companye = models.ForeignKey(CompanyEmployee ,default="",max_length=50, on_delete = models.CASCADE)
	CNumber = models.CharField(default="",max_length=12)

	class meta:
		db_table = "servicesoffers"

class MedicalHistoryRecord(models.Model):
	companye = models.ForeignKey(CompanyEmployee, default="" , on_delete = models.CASCADE)
	Employer = models.TextField(max_length=12, default="")
	Allergies = models.TextField(max_length=100, default="")
	MedicalConditions = models.TextField(default="")
	CurrentMedications = models.TextField(default="")
	DateRecord = models.TextField(max_length=8 ,default="" )
	#DateRecord = models.ManyToManyField(primary_key=True, max_length=16 ,default="" )
	ContactPerson = models.TextField(default="",max_length=30)
	ContactNumber = models.CharField(default="",max_length=12)
	RPerson = models.TextField(default="")
	class meta:
		db_table = "medicalhistoryrecord"

class Appointment(models.Model):
	companye = models.ForeignKey(CompanyEmployee, default="", on_delete = models.CASCADE)
	medicaloffers = models.ForeignKey(MedicalOffers, default="", on_delete = models.CASCADE)
	modality = models.TextField(default="", max_length=50)
	DateApp = models.TextField(default="")
	DoctorApp = models.TextField(default="")
	class meta:
		db_table = "appointment"

'''class List(models.Model):
	pass
class Item(models.Model):
	mdepname = models.CharField(max_length=50)
	ifname = models.CharField(max_length=50)
	caddress = models.TextField()
	aReason = models.CharField(max_length=50)
	hinfo = models.CharField(max_length=50)
	Kdate = models.TextField(max_length=8)
	tsign1 = models.CharField(max_length=100)
	list = models.ForeignKey( List, default=None, on_delete=models.PROTECT)
'''