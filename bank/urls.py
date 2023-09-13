from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register('addresses', views.AddressViewSet, basename='addresses')
router.register('all', views.BankViewSet, basename='all')
router.register('branches', views.BranchViewSet, basename='branches')
# router.register('accounts', views.AccountSerializer, basename='accounts')

urlpatterns = router.urls