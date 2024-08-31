from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django import forms
from .forms import SignUpForm,UpdateUserForm,UpdatePasswordForm, UserInfoForm
from . models import Profile

# Create your views here.

def home(request):
    return render(request, 'home.html',{})

def log_in(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user= authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have logged in successfully!")
            return redirect('home')
        else:
            messages.success(request,"Error try again")
            return redirect('log-in')
    else:
         return render(request, 'login.html',{})


def log_out(request):
    logout(request)
    messages.success(request,"You have been logged out")
    return redirect('home')

def register_user(request):
	form = SignUpForm()
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			# log in user
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ("You have successufly signed up, Please Enter your Personal details below"))
			return redirect('update_info')
		else:
			messages.success(request, ("Whoops! There was a problem Registering, please try again..."))
			return redirect('register')
	else:
		return render(request, 'register.html', {'form':form})
      
def update_user(request):
        if request.user.is_authenticated:
            current_user=User.objects.get(id=request.user.id)
            user_form = UpdateUserForm(request.POST or None,instance=current_user)
            if user_form.is_valid():
                  user_form.save()
                  login(request,current_user)
                  messages.success(request,"Profile Updated successfully")
                  return redirect('home')
            else:
                  return render(request, 'update_profile.html', {'user_form':user_form})
        else:
              messages.success(request,"You must be logged in to view this page")
                
  
# def update_password(request):
#     if not request.user.is_authenticated:
#         messages.error(request, "You must be logged in to view this page")
#         return redirect('log-in')

#     if request.method == 'POST':
#         form = UpdatePasswordForm(request.user, request.POST)  # Pass both user and POST data to the form
#         if form.is_valid():
#             user = form.save()
#             # update_session_auth_hash(request, user)  # Keep the user logged in after password change
#             messages.success(request, "Password updated successfully. Please log in again.")
#             return redirect('log-in')
#         else:
#             for error in list(form.errors.values()):
#                 messages.error(request, error)
#     else:
#         form = UpdatePasswordForm(request.user)  # Pass only the user to initialize the form

#     return render(request, "update_password.html", {'form': form})



def update_password(request):
	if request.user.is_authenticated:
		current_user = request.user
		# Did they fill out the form
		if request.method  == 'POST':
			form = UpdatePasswordForm(current_user, request.POST)
			# Is the form valid
			if form.is_valid():
				form.save()
				messages.success(request, "Your Password Has Been Updated...")
				login(request, current_user)
				return redirect('update_user')
			else:
				for error in list(form.errors.values()):
					messages.error(request, error)
					return redirect('update_password')
		else:
			form = UpdatePasswordForm(current_user)
			return render(request, "update_password.html", {'form':form})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')
	
# def update_info(request):
#         if request.user.is_authenticated:
#             current_user=Profile.objects.get(user__id=request.user.id)
#             form = UserInfoForm(request.POST or None,instance=current_user)
#             if form.is_valid():
#                   form.save()
#                   login(request,current_user)
#                   messages.success(request,"User Info Updated successfully")
#                   return redirect('home')
#             else:
#                   return render(request, 'update_info.html', {'form':form})
#         else:
#               messages.success(request,"You must be logged in to view this page")
      
def update_info(request):
	if request.user.is_authenticated:
		# Get Current User
		current_user = Profile.objects.get(user__id=request.user.id)
		
		# Get original User Form
		form = UserInfoForm(request.POST or None, instance=current_user)
			
		if form.is_valid() :
			# Save original form
			form.save()

			messages.success(request, "Your Info Has Been Updated!!")
			return redirect('home')
		return render(request, "update_info.html", {'form':form})
	else:
		messages.success(request, "You Must Be Logged In To Access That Page!!")
		return redirect('home')
 