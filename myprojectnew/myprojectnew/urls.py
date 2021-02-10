"""myprojectnew URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path


from accounts import views as accounts_views
from boards import views
from boards.views import ChartView

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    # url(r'^signup/$', accounts_views.signup, name='signup'),
    # url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('',views.logintstar, name='logintstar'),
    # url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^table/$',views.table, name='table'),
    url(r'^admin/', admin.site.urls),
    path('edit<int:Progress_ID>', views.edit, name='edit'),
    url(r'chart/$',ChartView.as_view(), name='chart'),
]