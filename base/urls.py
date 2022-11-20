from django.urls import path
from .views import Planlist, Plandetail, Plancreate, Planupdate, DeleteView

urlpatterns = [
    path('', Planlist.as_view(), name='plans'),
    path('plan/<int:pk>/', Plandetail.as_view(), name='plan'),
    path('create-plan/', Plancreate.as_view(), name='plan-create'),
    path('update-plan/<int:pk>/', Planupdate.as_view(), name='update-plan'),
    path('delete-plan/<int:pk>/', DeleteView.as_view(), name='delete-plan'),
]