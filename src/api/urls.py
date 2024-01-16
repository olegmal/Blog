from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from api.views import PostViewSet

# from api.views import PostDetailView, PostListView

app_name = "api"
router = routers.DefaultRouter()
router.register("posts", PostViewSet)

# posts/ - all
# posts/1 - one
# posts/1 method delete - delete one post
# posts/1 method put - edit one post
# posts/ method post - create one post
# posts/1 method patch - edit one post

schema_view = get_schema_view(
    openapi.Info(
        title="Post API",
        default_version="v1.0",
        description="API for posts added",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@admin.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("", include(router.urls)),
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger_docs"),
    # path("posts/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    # path("posts/", PostListView.as_view(), name="post_list"),
]
