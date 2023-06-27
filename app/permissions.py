from rest_framework import permissions

# To add a custom permission.
class IsAdminOrReadonly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        # admin_permission = bool(request.user and request.user.is_staff)     # gets true if it's user & is_staff
        # return request.method == 'GET' or admin_permission

        #          Another method for above one

        # if request is get then it's OKAY else we are testing the user is abmin or not.
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_staff)
    
# SAFE_METHOD == GET
# UNSAFE_METHOD == POST, DELETE, PUT

class IsReviewUserOrReadOnly(permissions.BasePermission):

    # has_object_permission is used when we want permission for object only.
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.review_user == request.user or request.user.is_staff
                                    # if the user is same who as writen the review return TRUE or editing id done by admin/staff
            # obj = object(review), review_user = review writen user == current loged-in user.

            