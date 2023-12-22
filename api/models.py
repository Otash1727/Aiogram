from tastypie.resources import ModelResource
from information.models import Users,Courses,Groups
from tastypie.authorization import Authorization
from .authentication import CustomAuthentication


class UserResourse(ModelResource):
    class Meta:
        queryset=Users.objects.all()
        allowed_methods=['get','post','delete']
        authentication=CustomAuthentication()
        authorization=Authorization()
    
    #def hydrate(self, bundle):
    #    bundle.obj.user_id=bundle.data['id']
    #    return bundle
#
    #def dehydrate(self, bundle):
    #    bundle.data['id']=bundle.obj.user_id
    #
    #def dehydrate_title(self, bundle):
    #    return bundle.data['title'].upper()


class CoursesResourse(ModelResource):
    class Meta:
        queryset=Courses.objects.all()
        allowed_method=['get','post','delete']
        authentication=CustomAuthentication()
        authorization=Authorization()
    
class GroupResourse(ModelResource):
    class Meta:
        queryset=Groups.objects.all()
        allowed_method=['get','post','delete']
        authentication=CustomAuthentication()
        authorization=Authorization()   


        

