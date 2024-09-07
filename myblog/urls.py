from django.urls import path
from .views import homepage,registration,sign_in,log_out,detail,update_post,delete_post
urlpatterns = [
    path('',homepage,name='home'),
    path('reg/',registration,name='reg'),
    path('login/',sign_in,name='login'),
    path('logout/',log_out,name='logout'),
    path('detail/<int:id>',detail,name='detail'),
    path('update/<int:id>',update_post,name='update'),
    path('delete/<int:if>',delete_post,name='delete'),
]
