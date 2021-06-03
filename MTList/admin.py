from django.contrib import admin
from .models import CompanyProfile, CompanyEmployee, MedicalOffers, MedicalHistoryRecord, Appointment

admin.site.register(CompanyProfile)
admin.site.register(CompanyEmployee)
admin.site.register(MedicalOffers)
admin.site.register(MedicalHistoryRecord)
admin.site.register(Appointment)

# Register your models here.
