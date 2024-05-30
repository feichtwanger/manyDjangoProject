from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('todo', include('todo.urls')),
]


from django.urls import path
from . import views

urlpatterns = [    
    path('', views.index, name='todo'),
    path('del/<str:item_id>', views.remove, name='del'),
]
