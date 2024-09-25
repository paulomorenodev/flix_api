from rest_framework import permissions

class GenrePermissionClass(permissions.BasePermission):
   def has_permission(self, request, view):
     #    print(request.method)
     #    print(request.content_type)
     #    print(request.META['USERDOMAIN'])
     #    print(request.headers['User-Agent'])

        if request.method in ['GET', 'HEAD', 'OPTIONS']:
             return request.user.has_perm('genres.view_genre')
        
        if request.method == 'POST':
             return request.user.has_perm('genres.add_genre')
        
        if request.method in ['PUT', 'PATCH']:
             return request.user.has_perm('genres.change_genre')
        
        if request.method == 'DELETE':
             return request.user.has_perm('genres.delete_genre')
   
        return False