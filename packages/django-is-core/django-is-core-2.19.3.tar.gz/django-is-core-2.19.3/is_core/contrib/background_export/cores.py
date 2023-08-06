from is_core.auth.permissions import PermissionsSet, SelfPermission, IsSuperuser
from is_core.main import UIRESTModelISCore, UIRESTISCore

from .models import ExportedFile
from .resource import CeleryRESTModelResource, CeleryRESTResource


class BackgroundExportISCoreMixin:

    rest_resource_class = CeleryRESTModelResource
    export_permission = IsSuperuser()

    def _get_export_permission(self):
        return self.export_permission

    def _init_permission(self, permission):
        permission = super()._init_permission(permission)
        permission.set('export', self._get_export_permission())
        return permission


class BackgroundExportUIRESTModelISCore(BackgroundExportISCoreMixin, UIRESTModelISCore):

    abstract = True


class BaseExportedFileISCore(BackgroundExportUIRESTModelISCore):

    abstract = True
    model = ExportedFile

    can_create = can_update = can_delete = False

    read_own_permission = IsSuperuser()
    read_all_permission = IsSuperuser()

    all_ui_list_fields = (
        'changed_at', 'created_at', 'created_by', 'downloaded_by', 'expiration', 'download_link', 'task__get_state',
        'task__get_start', 'task__get_stop'
    )
    own_ui_list_fields = (
        'changed_at', 'created_at', 'expiration', 'download_link', 'task__get_state', 'task__get_start',
        'task__get_stop'
    )
    form_fields = (
        'changed_at', 'created_at', 'created_by', 'downloaded_by', 'content_type', 'download_link', 'expiration',
        'task', 'task__get_state', 'task__get_start', 'task__get_stop'
    )

    def _init_permission(self, permission):
        return PermissionsSet(
            read=SelfPermission('read_own') | SelfPermission('read_all'),
            read_own=self.read_own_permission,
            read_all=self.read_all_permission,
        )

    def get_ui_list_fields(self, request):
        return (
            list(self.all_ui_list_fields) if self.permission.has_permission('read_all', request, self)
            else list(self.own_ui_list_fields)
        )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if self.permission.has_permission('read_all', request, self):
            return qs
        elif self.permission.has_permission('read_own', request, self):
            return qs.filter(created_by=request.user)
        else:
            return qs.none()
