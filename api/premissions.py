from rest_framework import permissions


class IsCustomAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)


class IsCustomModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_moderator

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)


class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.author
