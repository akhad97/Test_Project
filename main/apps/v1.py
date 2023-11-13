from django.urls import include, path



urlpatterns = [
    path(
        "client/",
        include(
            ("main.apps.client.urls", "main.apps.client.urls"),
            namespace="client",
        ),
    ),
    path(
        "employee/",
        include(
            ("main.apps.employee.urls", "main.apps.employee.urls"),
            namespace="employee",
        ),
    ),
    # path(
    #     "order/",
    #     include(
    #         ("main.apps.order.urls", "main.apps.order.urls"),
    #         namespace="order",
    #     ),
    # ),
    # path(
    #     "product/",
    #     include(
    #         ("main.apps.product.urls", "main.apps.product.urls"),
    #         namespace="product",
    #     ),
    # ),
]

