from django.urls import path
from .views.users import SignUp, SignIn, SignOut, ChangePassword
from .views.jobs import JobsView, JobView

urlpatterns = [
  path('sign-up/', SignUp.as_view(), name='sign-up'),
  path('sign-in/', SignIn.as_view(), name='sign-in'),
  path('sign-out/', SignOut.as_view(), name='sign-out'),
  path('change-password/', ChangePassword.as_view(), name='change-password'),
  path('jobs/', JobsView.as_view(), name='jobs'),
  path('job/', JobView.as_view(), name='job'),
]