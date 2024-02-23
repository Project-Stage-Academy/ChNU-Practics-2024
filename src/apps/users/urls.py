from django.urls import path

from .views import FounderListView, InvestorListView, SwitchRoleView, UserListView


urlpatterns = [
    path("", UserListView.as_view(), name="user-list"),
    path("investors/", InvestorListView.as_view(), name="investor-list"),
    path("founders/", FounderListView.as_view(), name="founder-list"),
    path("switch-role/", SwitchRoleView.as_view(), name="switch-role"),
]
