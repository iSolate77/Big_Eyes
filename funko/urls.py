from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('funkos', views.funkos_index, name='index'),
    path('funkos/create/', views.FunkoCreate.as_view(), name='funko_create'),
    path('funkos/<int:pk>', views.FunkoDetail.as_view(), name='funko_detail'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/profile/update/', views.update_profile, name='profile_update'),
    # path('order/', views.order, name='order'),
    path('orders/', views.OrderDetail.as_view(), name='order_detail'),

    path('funkos/create', views.FunkoCreate.as_view(), name='funko_create'),
    # path('funkos/<int:pk>/', views.FunkoDetail.as_view(), name='funko_details'),
    path('funkos/<int:pk>/update', views.FunkoUpdate.as_view(), name='funko_update'),
    path('funkos/<int:pk>/delete', views.FunkoDelete.as_view(), name='funko_delete'),

    # for Many to Many relations items in cart(manual):
    path('funkos/<int:funko_id>/add_to_cart/',
         views.add_to_cart, name='add_to_cart'),
    path('funkos/<int:funko_id>/remove_from_cart/',
         views.remove_from_cart, name='remove_from_cart'),
]
