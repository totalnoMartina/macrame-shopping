from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('macrames/', views.all_macrames, name='macrame_items'),
    path('<int:item_id>/', views.macrame_detail, name='macrame-detail'),
    # path(r'^like/$', views.macrame_likes, name='like_macs'),
    # path('like/<item_id>', views.MacrameLike.as_view(), name='macrame_like'),
    path('<int:pk>/like', views.MacrameLike.as_view(), name='like'),



]
