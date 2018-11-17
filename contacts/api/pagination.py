from rest_framework.pagination import (PageNumberPagination,
                                       LimitOffsetPagination)

class PhonebookPageNumberPagination(PageNumberPagination):
    page_size=10
