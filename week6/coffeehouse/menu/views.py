from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import UpdateView, DeleteView

from menu.models import Special, Profile
from django.urls import reverse_lazy

class IndexView(ListView):
    template_name = "index.html"
    model = Special


# THE FOLLOWING IS IMPORTANT FOR A USER PROFILE
class ProfileUpdateView(UpdateView):
    template_name = "profile.html"
    fields = ('access_level',)
    success_url = reverse_lazy('profile_view')

    def get_object(self):
        return   Profile.objects.get(user=self.request.user)
    # this will bypass the need for a pk or slug

# with get_object, we no longer need get_queryset b/c get_object is as specific as it can get
    # def get_queryset(self):
    #     return Profile.objects.filter(user=self.request.user)

class SpecialUpdateView(UpdateView):
    model = Special
    success_url = "/"
    fields = ('title', 'description', 'cost')

    def get_queryset(self):
        # if  self.request.user.profile.access_level == 'o':
            # this code can be better, with the below
        if  self.request.user.profile.is_owner:
            return Special.objects.all()
        return Special.objects.filter(created_by=self.request.user)
        # this will prevent a user from editing pages they did not created

class SpecialDeleteView(DeleteView):
    model = Special
    success_url = "/"

    def get_queryset(self):
        if self.request.user.profile.is_owner:
            return Special.objects.all()
        return []
