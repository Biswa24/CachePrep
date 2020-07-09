from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from ApiHandler import views,Api

urlpatterns = [
    # Webpages
    path('',views.home,name='home'),

    path('api/', Api.all_question,name='all_question'),
    path('api/add/',Api.add_question,name='add_question'),
    path('api/update/<str:pk>/',Api.update_question,name='update_question'),
    path('api/search/',Api.tag_search,name='tag_search'),

] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)