# from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny

from api.permissions import IsAdminOrReadOnly
from recipes.models import Recipe
from .serializers import SubscribeRecipeSerializer


class GetObjectMixin:
    queryset = Recipe.objects.all()
    serializer_class = SubscribeRecipeSerializer
    permission_classes = (AllowAny,)
    # lookup_field = 'recipe_id'
    lookup_field = 'id'

    # def get_object(self):
    #     recipe_id = self.kwargs['recipe_id']
    #     recipe = get_object_or_404(Recipe, id=recipe_id)
    #     self.check_object_permissions(self.request, recipe)
    #     return recipe


class PermissionAndPaginationMixin:
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None
