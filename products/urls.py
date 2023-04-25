from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path("about",views.about,name="about"),
    path("contact",views.contact,name="contact"),
    path("administrator",views.administrator, name="administrator"),
    path("admin_users",views.admin_users,name="customers"),
    path("admin_orders",views.admin_orders,name="admin-orders"),
    path("admin_pending_payment",views.admin_pending_payment, name="admin-pending-payment"),
    path("admin_paid_parcel",views.admin_paid_parcel, name="admin-paid-parcel"),
    path("admin_delivered",views.admin_delivered, name="admin-delivered"),
    path("admin_update_delivered/<order_id>",views.admin_update_delivered,name="admin-update-delivered"),
    path("admin_completed",views.admin_completed, name="admin-completed"),
    path("admin_payments",views.admin_payments, name="admin-payments"),
    path("admin_update_payment/<record_id>",views.admin_update_payment,name="update-payment"),
    path("admin_reviews", views.admin_reviews, name="admin-reviews"),
    path("add_service",views.add_service,name="add-service"),
    path("list_services",views.list_services,name="list-services"),
    path("update_service/<service_id>",views.update_service,name="update-service"),
    path("delete_service/<service_id>",views.delete_service,name="delete-service"),
    path("add_product",views.add_product,name="add-product"),
    path("list_products", views.list_products,name="list-products"),
    path("update_product/<product_id>",views.update_product,name="update-product"),
    path("delete_product/<product_id>",views.delete_product,name="delete-product"),
    path("update_team/<team_id>",views.update_team, name="update-team"),
    path("delete_team/<team_id>", views.delete_team, name="delete-team"),
    path("list_team", views.list_team, name="list-team"),
    path("add_team", views.add_team, name="add-team"),
    path("add_store",views.add_store, name="add-store"),
    path("list_stores", views.list_stores,name="list-stores"),
    path("update_store/<store_id>",views.update_store, name="update-store"),
    path("delete_store/<store_id>",views.delete_store, name="delete-store"),
    path("all_products",views.all_products,name="all-products"),
    path("men_glasses",views.men_glasses,name="men-glasses"),
    path("women_glasses",views.women_glasses,name="women-glasses"),
    path("kids_glasses",views.kids_glasses,name="kids-glasses"),
    path("computer_glasses",views.computer_glasses,name="computer-glasses"),
    path("protector_glasses",views.protector_glasses,name="protector-glasses"),
    path("sun_glasses",views.sun_glasses,name="sun-glasses"),
    path('add_to_cart/<product_id>',views.add_to_cart,name="add-to-cart"),
    path('cart',views.cart,name="cart"),
    path("update_cart_quantity/<cart_id>",views.update_cart_quantity,name="update-quantity"),
    path("remove_from_cart/<cart_id>",views.remove_from_cart,name="remove-from-cart"),
    path("place_order_from_cart",views.place_order_from_cart,name="order-from-cart"),
    path("place_order/<cart_id>",views.place_order,name="place-order"),
    path("my_orders",views.my_orders,name="my-orders"),
    path("payments",views.payments,name="payments"),
    path("payment",views.payment,name="payment"),
    path("pending_payment",views.pending_payment, name="pending-payment"),
    path("in_transit",views.in_transit,name="in-transit"),
    path("delivered",views.delivered, name="delivered"),
    path("update_delivered/<order_id>",views.update_delivered, name="update-delivered"),
    path("review_orders",views.review_orders, name="review-orders"),
    path("review_order/<order_id>",views.review_order, name="review-order"),
    path("completed", views.completed, name="completed"),
    path("search_products", views.search_products, name="search-products"),
    path("send_message",views.send_message, name="send-message"),
]
