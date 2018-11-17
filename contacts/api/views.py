from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView
    )
from django.db.models import Q
from contacts.models import Phonebook
from .pagination import PhonebookPageNumberPagination
from .serializers import PhonebookSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


class PhonebookCreateAPIView(CreateAPIView):
    queryset = Phonebook.objects.all()
    serializer_class = PhonebookSerializer
    #permission_classes=[IsAuthenticated]



class PhonebookDetailAPIView(RetrieveAPIView):
    queryset = Phonebook.objects.all()
    serializer_class = PhonebookSerializer
    renderer_classes = (JSONRenderer, )

class PhonebookUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Phonebook.objects.all()
    serializer_class = PhonebookSerializer
    #permission_classes=[IsAuthenticatedOrReadOnly]

class PhonebookDeleteAPIView(DestroyAPIView):
    queryset = Phonebook.objects.all()
    serializer_class = PhonebookSerializer
    #permission_classes=[IsAuthenticated]

class PhonebookListAPIView(ListAPIView):
    serializer_class = PhonebookSerializer
    template_name = 'base.html'
    pagination_class = PhonebookPageNumberPagination
    #permission_classes = [IsAuthenticatedOrReadOnly]
    renderer_classes = (JSONRenderer, )

    def get_queryset(self, *args, **kwargs):
        queryset = Phonebook.objects.all()
        query=self.request.GET.get('q')
        if query:
            print ("in")
            queryset = Phonebook.objects.filter(Q(first_name__icontains=query)|
                                                Q(last_name__icontains=query)|
                                                Q(email__icontains=query)
                                                ).distinct()
        print (queryset, query)

        return queryset
