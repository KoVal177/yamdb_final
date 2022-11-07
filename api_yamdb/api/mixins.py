from rest_framework import mixins, viewsets


class CreateListDestroyMixinViewset(mixins.CreateModelMixin,
                                    mixins.ListModelMixin,
                                    mixins.DestroyModelMixin,
                                    viewsets.GenericViewSet):
    pass
