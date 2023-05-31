from rest_framework.permissions import AllowAny

from api.permissions import IsAdminOrReadOnly

from .serializers import SubscribeRecipeSerializer


class GetObjectMixin:
    serializer_class = SubscribeRecipeSerializer
    permission_classes = (AllowAny,)
    lookup_field = 'recipe_id'


class PermissionAndPaginationMixin:
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None
