from base64 import urlsafe_b64encode
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls.base import reverse
from .forms import SignUpForm
from django.template.context_processors import csrf
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from .models import addEmployee
from .tokens import account_activation_token
from django.views.generic import ListView
from django.template.loader import render_to_string

# Create your views here.

#homepage
def Homepage(request):
    return render(request,'index.html')

# def index1(request):
#     return render(request, 'index.html')
    
#signup---admin will create new account for employee---information includes username, email ID, password
def signup(request):
    form = SignUpForm()
    return render(request, 'signup.html', {
        'form': form
    })

#Dispaly dashboard after successful login
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "dashboard.html")

#login function
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html" ,{
                "message": "Invalid Credentials, please try again with correct details."
            })

    return render(request, "login.html")

#logout function
def logout_view(request):
    logout(request)
    return render(request, "login.html" ,{
        "message": "Logged Out."
    })
    
def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.first_name = form.cleaned_data.get('first_name')
        user.profile.last_name = form.cleaned_data.get('last_name')
        user.profile.email = form.cleaned_data.get('email')
        #user cannot login until link confirmed
        user.is_active = False
        user.save()
        current_site = get_current_site(request)
        subject = "Please Activate your Account."
        # loaded a template like get_template()
        # and calls its render() method immediately
        
        message = render_to_string('activation_request.html',{
            'user': user,
            'domain':current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            # this method will generate a hash value with user related data
            'token': account_activation_token.make_token(user),
        })
        user.email_user(subject, message)
        return redirect('activation_sent')
    
        # username = form.cleaned_data.get('username')
        # password = form.cleaned_data.get('password1')
        # user = authenticate(username= username, password=password)
        # login(request, user)
        # return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form' : form})
    

class ModelListView(ListView):
    model = addEmployee
    template_name = "register.html"


# def profile(request):
#     return render(request, 'profile.html')

# @method_decorator(login_required(login_url='login'), name='dispatch')
# class ProfileView(View):
#     profile = None

#     def dispatch(self, request, *args, **kwargs):
#         self.profile, __ = Profile.objects.get_or_create(user=request.user)
#         return super(ProfileView, self).dispatch(request, *args, **kwargs)

#     def get(self, request):
#         context = {'profile': self.profile, 'segment': 'profile'}
#         return render(request, 'customers/profile.html', context)

#     def post(self, request):
#         form = ProfileForm(request.POST, request.FILES, instance=self.profile)

#         if form.is_valid():
#             profile = form.save()
#             profile.user.first_name = form.cleaned_data.get('first_name')
#             profile.user.last_name = form.cleaned_data.get('last_name')
#             profile.user.email = form.cleaned_data.get('email')
#             profile.user.save()

#             messages.success(request, 'Profile saved successfully')
#         else:
#             messages.error(request, form_validation_error(form))
#         return redirect('profile')
    
