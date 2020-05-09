from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# @login_required()
# def index(request):
#     if request.method == "POST":
#         user = User.objects.get(pk=request.user.id)
#         user.first_name = request.POST.get("first_name", None)
#         user.last_name = request.POST["last_name"]
#         # user.last_name = request.POST["last_name"]
#         user.profile.location = request.POST.get("location", None)
#         user.profile.birth_date = request.POST.get("birth_date", None)
#         user.save()
#
#         request.user = user
#
#     return render(request, 'registration/profile.html')


class ProfileView(View):
    template_name = 'registration/profile.html'

    @method_decorator(login_required)
    def get(self, request):
        return render(request, self.template_name)

    @method_decorator(login_required)
    def post(self, request):
        if request.method == "POST":
            user = User.objects.get(pk=request.user.id)
            user.first_name = request.POST.get("first_name", None)
            user.last_name = request.POST["last_name"]
            user.profile.location = request.POST.get("location", None)
            user.profile.birth_date = request.POST.get("birth_date", None)
            user.save()
            request.user = user
        return self.get(request)
