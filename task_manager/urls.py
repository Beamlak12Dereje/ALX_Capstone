from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def root_view(request):
    if request.user.is_authenticated:
        return redirect('task_list')  # Redirect to /tasks/
    return redirect('login')  # Redirect to /login/

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', root_view, name='root'),
    path('', include('users.urls')),
    path('', include('tasks.urls')),
]