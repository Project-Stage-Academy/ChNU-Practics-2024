from functools import wraps

from django.core.cache import cache
from rest_framework import serializers


def check_token_usage(func):
    @wraps(func)
    def wrapper(self, *args, **kwrags):
        token = self.request.query_params.get("token")

        if cache.get(token):
            raise serializers.ValidationError("Token has already been used.")

        result = func(self, *args, **kwrags)

        self.blacklist_access(token)

        return result

    return wrapper
