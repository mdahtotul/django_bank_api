from rest_framework.permissions import (
    BasePermission,
    SAFE_METHODS,
)


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.role == "admin")


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif request.user.is_authenticated and request.user.role == "admin":
            return True
        else:
            return False


class IsManager(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user.is_authenticated and request.user.role in ("admin", "manager")
        )


class IsManagerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif request.user.is_authenticated and request.user.role in (
            "admin",
            "manager",
        ):
            return True
        else:
            return False


class IsOfficer(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user.is_authenticated
            and request.user.role in ("admin", "manager", "officer")
        )


class IsOfficerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif request.user.is_authenticated and request.user.role in (
            "admin",
            "manager",
            "officer",
        ):
            return True
        else:
            return False


class IsCashier(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user.is_authenticated
            and request.user.role in ("admin", "manager", "officer", "cashier")
        )


class IsCashierOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif request.user.is_authenticated and request.user.role in (
            "admin",
            "manager",
            "officer",
            "cashier",
        ):
            return True
        else:
            return False


class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated)


class IsAuthenticatedOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user.is_authenticated)
