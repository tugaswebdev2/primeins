from django.db import models


RECORD_CHOICES = (
	("NEW" , "New Account"),
	("EXISTING" , "Existing Account ")
	)

DEPARTMENT_CHOICES = (
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
	Nemp = models.IntegerField(default='')
	Emailemp = models.CharField(default="", max_length=30)
	TNumber = models.CharField(default="",max_length=20)

	class meta:
		db_table = "ccompanyprofile"

class Companyemployee(models.Model):
	NPatient  = models.TextField(default=None, max_length=50)
	EIdnumber = models.CharField(default=None, max_length=20)
	Phealth = models.CharField(default=None, max_length=20)
	companyp = models.ForeignKey(CompanyProfile,default="",max_length=50, on_delete = models.CASCADE)
	class meta:
		db_table = "companyeemployee"

class MedicalOffers(models.Model):

	companyemployee = models.ForeignKey(Companyemployee ,default="",max_length=50, on_delete = models.CASCADE)
	CNumber = models.CharField(default="",max_length=12)
	DepartmentS = models.TextField(max_length=80, default="")
	Services = models.CharField(max_length = 20, choices = DEPARTMENT_CHOICES, default ="")
	Account = models.CharField(max_length = 20, choices = RECORD_CHOICES, default ="")

	class meta:
		db_table = "servicesoffers"

class MedicalHistoryRecord(models.Model):
	companyemployee = models.ForeignKey(Companyemployee, default="" , on_delete = models.CASCADE)

	Allergies = models.TextField(max_length=100, default="")
	MedicalConditions = models.TextField(default="")
	CurrentMedications = models.TextField(default="")
	DateRecord = models.TextField(max_length=8 ,default="" )
	#DateRecord = models.ManyToManyField(primary_key=True, max_length=16 ,default="" )
	modality = models.TextField(default="", max_length=50)
	ContactPerson = models.TextField(default="",max_length=30)
	ContactNumber = models.CharField(default="",max_length=12)
	RPerson = models.TextField(default="")
	class meta:
		db_table = "medicalhistoryrecord"

class Appointment(models.Model):
	companyemployee = models.ForeignKey(Companyemployee, default="", on_delete = models.CASCADE)
	DOBirth = models.CharField(default="", max_length=8)
	Emailemp = models.CharField(default="", max_length=50)
	DName = models.TextField(default="", max_length=30)
	Hospital = models.TextField(default="", max_length=50)
	department = models.TextField(default="", max_length=30)
	ServiceSS = models.TextField(default="", max_length=50)
	ADate = models.TextField(default="", max_length=8)
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