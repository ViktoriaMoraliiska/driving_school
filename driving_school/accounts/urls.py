from django.urls import path, include

from driving_school.accounts.views import LogInUserView, RegisterUserView, LogOutUserView, DeleteUserView, DetailUserView, EditUserView
urlpatterns = (
    path('login/', LogInUserView.as_view(), name='login user'),
    path('register/', RegisterUserView.as_view(), name='register user'),
    path('logout/', LogOutUserView.as_view(), name='logout user'),
    path('profile/<int:pk>/', include([
        path('', DetailUserView.as_view(), name='details user'),
        path('edit/', EditUserView.as_view(), name='edit user'),
        path('delete/', DeleteUserView.as_view(), name='delete user'),
    ])),
)
