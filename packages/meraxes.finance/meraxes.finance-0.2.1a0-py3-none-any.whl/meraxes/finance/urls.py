from rest_framework.routers import DefaultRouter

from meraxes.finance import views


router = DefaultRouter()
router.register('accounts', views.AccountViewSet)
router.register('institutes', views.InstituteViewSet)
router.register('transactions', views.TransactionViewSet)
