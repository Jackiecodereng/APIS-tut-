"""
URL configuration for students_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from apis import views

urlpatterns = [
    path('api/v1/live', views.students_list),
    path('api/v1/live/<int:student_id>', views.single_student),
    path('api/v1/live/update/<int:student_id>', views.update_student),
    path('api/v1/live/delete/<int:student_id>', views.delete_student),
    path('api/v1/live/create', views.create_student),
    path('admin/', admin.site.urls),
]
