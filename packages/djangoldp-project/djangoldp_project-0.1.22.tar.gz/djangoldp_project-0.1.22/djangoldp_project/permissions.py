from djangoldp.permissions import LDPPermissions


# auxiliary function tests user is an admin for specified project
def is_user_admin_of_project(user, project):
    from .models import Member

    try:
        project_member = Member.objects.get(user=user, project=project)
        return project_member.is_admin

    except:
        return False


class ProjectPermissions(LDPPermissions):
    def has_permission(self, request, view):
        # anonymous users have no rights
        if request.user.is_anonymous and not request.method == 'OPTIONS':
            return False

        # request on an existing resource - this will be reviewed by has_object_permission
        if request.method == 'PATCH' or request.method == 'DELETE' or request.method == 'PUT':
            return True

        return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        from .models import Member

        # anonymous users have no rights
        if request.user.is_anonymous and not request.method == 'OPTIONS':
            return False

        # admins have full permissions
        if is_user_admin_of_project(request.user, obj):
            return True

        # other members can perform GET only
        if request.method != 'GET':
            return False

        if not Member.objects.filter(user=request.user, project=obj).exists():
            return False

        return super().has_object_permission(request, view, obj)


class ProjectMemberPermissions(LDPPermissions):
    def has_permission(self, request, view):
        from djangoldp.models import Model

        # anonymous users have no rights
        if request.user.is_anonymous and not request.method == 'OPTIONS':
            return False

        # request on an existing resource - this will be reviewed by has_object_permission
        if request.method == 'PATCH' or request.method == 'DELETE' or request.method == 'PUT':
            return True

        # only admins can add new members to a project
        if request.method == 'POST':
            obj = Model.resolve_id(request._request.path)
            return is_user_admin_of_project(request.user, obj.project)

        return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        # anonymous users have no rights
        if request.user.is_anonymous and not request.method == 'OPTIONS':
            return False

        # admins have full permissions
        if is_user_admin_of_project(request.user, obj.project):
            if request.method == 'DELETE':
                # I cannot remove myself if I am the last admin
                if obj.pk == request.user.pk:
                    if obj.project.get_admins().count() == 1:
                        return False

                # I cannot remove another admin
                elif obj.is_admin:
                    return False

            return True

        # I can remove myself
        if obj.user.pk == request.user.pk:
            return True

        return super().has_object_permission(request, view, obj)
