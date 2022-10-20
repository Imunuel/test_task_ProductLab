from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import ParseSerializer
from .services import parse_item


class ParseView(viewsets.GenericViewSet):

    def get_serializer_class(self):
        return ParseSerializer

    def get_queryset(self):
        pass

    @action(methods=["POST", ], detail=False)
    def get_parse_data(self, request):
        url = request.data
        data = parse_item(url=url["url"])
        return Response(data=data, status=status.HTTP_200_OK)
