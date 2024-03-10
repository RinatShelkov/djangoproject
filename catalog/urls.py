from django.urls import path

from catalog.views import home, conacts

urlpatterns = [
    path('home/', home),
    path('conacts/', conacts),

]
