from django.contrib import admin
from .models import CompanyProfile, Companyemployee, MedicalOffers, MedicalHistoryRecord, Appointment

admin.site.register(CompanyProfile)
admin.site.register(Companyemployee)
admin.site.register(MedicalOffers)
admin.site.register(MedicalHistoryRecord)
admin.site.register(Appointment)

# Register your models here.
