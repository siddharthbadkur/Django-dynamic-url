from django.urls import path
from.views import *

urlpatterns=[
    path('home/',home,name='home'),
    # # path('integer/<int:pk>',integer123,name='integer'),
    # # path('string/<str:ab>',string123,name='string'),
    # # path('slug/<slug:abc>',slug123,name='slug'),
    # path('path/<path:pkabc>',path123,name='path')
    path('comb/<int:pk>,<str:abc>,<slug:pkabc>',combination,name='combination')
]