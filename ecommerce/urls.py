# urls.py
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from .views import (
    UserProfileViewSet,
    PetProfileViewSet,
    ProductViewSet,
    ClinicViewSet,
    DoctorViewSet,
    AppointmentViewSet,
    MedicalRecordViewSet,
    OrderViewSet
)

# Define the schema view
schema_view = get_schema_view(
    openapi.Info(
        title="Pet Clinic API",
        default_version='v1',
        description="API documentation for the Pet Clinic project",
        contact=openapi.Contact(email="saif780@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[AllowAny],
)

# Initialize the router
router = DefaultRouter()

# Register the viewsets with the router
router.register(r'userprofiles', UserProfileViewSet)
router.register(r'petprofiles', PetProfileViewSet)
router.register(r'products', ProductViewSet)
router.register(r'clinics', ClinicViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'medicalrecords', MedicalRecordViewSet)
router.register(r'orders', OrderViewSet)

# Include the router URLs in the urlpatterns
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-ui'),
    path('api/schema/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
