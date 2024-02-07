from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path("home", views.home, name='home'),
    path("signin", views.signin, name='signin'),
    path("signup", views.signup, name ='signup'),
    path("accounts", views.accounts, name='accounts'),
    path("logout", views.logout_view, name = 'logout'),
    path("entries", views.entries, name='entries'),
    path("list", views.list, name='list'),
    path("post", views.post, name='post'),
    path("delete/<int:entry_id>", views.delete, name="delete"),
    path("entry/<int:entry_id>", views.entry, name="entry"),
    path("checklist/", views.checklist, name='checklist'),
    path("add_checklist", views.add_checklist, name="add_checklist"),
    path("delete_checklist/<int:checklist_id>", views.delete_checklist, name="delete_checklist"),
    path('add_item', views.add_item, name='add_item'),
    path('toggle/<int:item_id>/', views.toggle_item, name='toggle_item'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
]
