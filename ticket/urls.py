from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns=[
    path("home/",views.home,name="home"),
    path("event_details/",views.event_details,name='event_details'),
    path("purchasing_ticket/",views.purchase_ticket,name='purchasing_ticket'),
    path('payment/', views.payment_view, name='payment'),
    path('payment_success/', views.payment_success_view, name='payment'),
    path('aboutUs/', views.aboutUs, name='AboutUs'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
