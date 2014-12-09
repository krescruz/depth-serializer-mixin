DepthSerializerMixin
====================

Defined the depth serializer based on query parameter in the url

# Install

	from rest_framework import viewsets
	from django.contrib.auth.models import User
	from .mixins import DepthSerializerMixin
	from .serializers import UserSerializer

    class UserViewSet(DepthSerializerMixin, viewsets.ViewSet):
    	"""
		A simple ViewSet
		"""
		serializer_class = UserSerializer
		queryset = User.objects.all()

# Use
	http://example.com/api/users?__depth=2