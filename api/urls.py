from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import EmailTokenObtainPairView, SignUpView, ResetPasswordView,  EIADataView, CrudeOilView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='token_obtain_pair'),
    path('reset/', ResetPasswordView.as_view(), name='reset_password'),
    path('token/', EmailTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('crude/', CrudeOilView.as_view(), name='crude_oil'),
    path('eia/', EIADataView.as_view(), name='eia_data'),
]
