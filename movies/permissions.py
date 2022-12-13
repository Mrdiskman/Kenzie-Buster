from rest_framework import permissions
import ipdb

class MyCustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if ( 
            request.method == "POST" and
            request.user.is_authenticated
            and request.user.is_employee
        ):
            return True
        elif(
            request.method == "DELETE" and
            request.user.is_authenticated
            and request.user.is_employee
          ):
            return True
        else:
            return False