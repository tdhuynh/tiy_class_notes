from rest_framework import permissions


class IsCreatedByOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # we want to allow this for everyone that has a get request
        if request.method in permissions.SAFE_METHODS:
            return True
        print(obj.created_by == request.user)
        print(request.user)
        # this will only allow the record for the user that created it
        return obj.created_by == request.user
