from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import CategorySerializer, ProductSerializer, ProfileSerializer, ClientSerializer
from home.models import Product, Category, Profile, Client
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.decorators import action
from django.db.transaction import atomic
from rest_framework import status


class HomeAPIView(APIView):
    def get(self, request):
        return Response(data={'message': 'Hello World!'})

    def post(self, request):
        return Response(data={'message': 'Hello World!'})


class CategoryAPIView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'category__name')
    pagination_class = LimitOffsetPagination
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)

    @action(detail=True, methods=['GET'])
    def products(self, request, pk=None):
        products = self.get_object()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProfileAPIView(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('first_name', 'last_name')
    pagination_class = LimitOffsetPagination
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)

    @action(detail=True, methods=['GET'])
    def profile(self, request, *args, **kwargs):
        profile = self.get_queryset()
        first_name = profile.first.first_name
        last_name = profile.first.last_name
        full_name = first_name + last_name
        serializer = ClientSerializer(full_name, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def joined_date(self, request, *args, **kwargs):
        profile = self.get_queryset()
        date = profile.joined.date()
        serializer = ClientSerializer(date, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def sorted_by_last_update(self, request, *args, **kwargs):
        profile = self.get_queryset()
        last_update = profile.order_by('-last_update')
        serializer = ClientSerializer(last_update, many=True)
        return Response(serializer.data)


class ProductAPIView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', )
    pagination_class = LimitOffsetPagination
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)

    @action(detail=True, methods=['GET'])
    def taken(self, request, *args, **kwargs):
        products = self.get_object()
        with atomic():
            products.taken += 1
            products.save()
            return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET'])
    def duration(self, request, *args, **kwargs):
        products = self.get_queryset()
        duration = products.duration
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def price(self, request, *args, **kwargs):
        products = self.get_queryset()
        sorting = products.order_by("price")
        serializer = ProductSerializer(sorting, many=True)
        return Response(serializer.data)

    # @action(detail=True, methods=['GET'])
    # def left(self, request, *args, **kwargs):
    #     products = self.get_queryset()
    #     with atomic():
    #         products -= 1
    #         products.save()
    #         return Response(status=status.HTTP_200_OK)


class ClientAPIView(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('first_name', 'last_name')
    pagination_class = LimitOffsetPagination
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)

    @action(detail=True, methods=['GET'])
    def clients(self, request, *args, **kwargs):
        clients = self.get_queryset()
        first_name = clients.first.first_name
        last_name = clients.first.last_name
        full_name = first_name + last_name
        serializer = ClientSerializer(full_name, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def joined_date(self, request, *args, **kwargs):
        clients = self.get_queryset()
        date = clients.joined.date()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def sorted_by_last_update(self, request, *args, **kwargs):
        clients = self.get_queryset()
        last_update = clients.order_by('-last_update')
        serializer = ClientSerializer(last_update, many=True)
        return Response(serializer.data)













































