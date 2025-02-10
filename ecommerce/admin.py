from django.contrib import admin

from .models import UserProfile, PetType, PetProfile, ProductCategory, Product, Clinic, Doctor, Appointment, \
    MedicalRecord, Order, Status

class ReadOnlyFieldsAdmin(admin.ModelAdmin):
    readonly_fields = ('created_by', 'created_at', 'modified_by', 'modified_at')


admin.site.register(UserProfile, ReadOnlyFieldsAdmin)
admin.site.register(PetType, ReadOnlyFieldsAdmin)
admin.site.register(Status, ReadOnlyFieldsAdmin)
admin.site.register(PetProfile, ReadOnlyFieldsAdmin)
admin.site.register(ProductCategory, ReadOnlyFieldsAdmin)
admin.site.register(Product, ReadOnlyFieldsAdmin)
admin.site.register(Clinic, ReadOnlyFieldsAdmin)
admin.site.register(Doctor, ReadOnlyFieldsAdmin)
admin.site.register(Appointment, ReadOnlyFieldsAdmin)
admin.site.register(MedicalRecord, ReadOnlyFieldsAdmin)
admin.site.register(Order, ReadOnlyFieldsAdmin)
