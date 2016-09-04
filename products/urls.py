from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^import_excel/$',views.import_excel,name='import_excel'),

]