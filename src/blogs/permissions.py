from rest_framework.permissions import BasePermission

from blogs.models import Commentary, Post


class BlogPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Define si un usuario puede usar o no el endpoint que quiere utilizar
        :param request: HttpRequest
        :param view: UsersAPI/UserDetailAPI
        :return: True si puede, False si no puede
        """

        # cualquiera autenticado puede acceder al detalle para ver, actualizar o borrar
        if request.user.is_authenticated() and request.method in ("POST", "PATCH", "PUT", "DELETE"):
            return True

        # si quiere acceder al listado
        if request.method == "GET":
            return True

        return False

    def has_object_permission(self, request, view, obj):
        """
        Define si el usuario puede realizar la acción sobre el objeto que quiere realizarla
        :param request: HttpRequest
        :param view: UsersAPI/UserDetailAPI
        :param obj: User
        :return: True si puede, False si no puede
        """

        post = Post.objects.get(title=obj)

        # si es admin o si es él mismo, le dejamos
        if request.user.is_superuser or request.user == post.owner and request.method in ("POST", "PUT", "DELETE"):
            return True

        if request.user.is_authenticated() and request.method == "PATCH":
            return True

        if request.method == "GET":
            return True

        return False


class CommentPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Define si un usuario puede usar o no el endpoint que quiere utilizar
        :param request: HttpRequest
        :param view: UsersAPI/UserDetailAPI
        :return: True si puede, False si no puede
        """

        # cualquiera autenticado puede acceder al detalle para ver, actualizar o borrar
        if request.method in ("GET", "POST", "PATCH", "PUT", "DELETE"):
            return True

        return False

    def has_object_permission(self, request, view, obj):
        """
        Define si el usuario puede realizar la acción sobre el objeto que quiere realizarla
        :param request: HttpRequest
        :param view: UsersAPI/UserDetailAPI
        :param obj: User
        :return: True si puede, False si no puede
        """

        comment = Commentary.objects.get(content=obj)

        # si es admin o si es él mismo, le dejamos
        if (request.user.is_superuser or request.user == comment.owner) and request.method in ("PATCH", "PUT", "DELETE"):
            return True

        if request.method in ("GET", "POST"):
            return True

        return False
