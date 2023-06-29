
from django.urls import path, include
from core.views import Home

app_name = 'core'
urlpatterns = [
    path('shop/', include('shop.urls')),
    path('', Home.as_view(), name='index'),
]

handler404 = 'core.views.custom_page_not_found_view'
handler500 = 'core.views.custom_error_view'