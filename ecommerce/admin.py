from django.contrib import admin

from .models import UserProfile, PetType, PetProfile, ProductCategory, Product, Clinic, Doctor, Appointment, \
    MedicalRecord, Order

admin.site.register(UserProfile)
admin.site.register(PetType)
admin.site.register(PetProfile)
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Clinic)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(MedicalRecord)
admin.site.register(Order)
