from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from core.forms import  JoinForm, LoginForm, editProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from toolExchange.models import tool
from core.models import Profile

# Create your views here.
@login_required(login_url='/login/')
def home(request):
    table_data = tool.objects.all()
    context = {
    "table_data": table_data,
    }
    return render(request, 'core/home.html', context)

def about(request):
    user_data = User.objects.get(id=request.user.id)
    tool_data = tool.objects.filter(user=request.user)
    tools = 0
    for row in tool_data:
        if row.live or not(row.live):
            tools = tools + 1
    context = {
    "user_data": user_data,
    "tools": tools,
    }
    return render(request, 'core/about.html', context)


def user_join(request):
    if (request.method == "POST"):
        join_form = JoinForm(request.POST)
        if (join_form.is_valid()):
            # Save form data to DB
            user = join_form.save()
            # Encrypt the password
            user.set_password(user.password)
            # Save encrypted password to DB
            user.save()
            # Success! Redirect to home page.
            return redirect("/")
        else:
            # Form invalid, print errors to console
            page_data = { "join_form": join_form }
            return render(request, 'core/join.html', page_data)
    else:
        join_form = JoinForm()
        page_data = { "join_form": join_form }
        return render(request, 'core/join.html', page_data)

def user_login(request):
    if (request.method == 'POST'):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # First get the username and password supplied
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            # Django's built-in authentication function:
            user = authenticate(username=username, password=password)
            # If we have a user
            if user:
                #Check it the account is active
                if user.is_active:
                    # Log the user in.
                    login(request,user)
                    # Send the user back to homepage
                    return redirect("/")
                else:
                    # If account is not active:
                    return HttpResponse("Your account is not active.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username,password))
                return render(request, 'core/login.html', {"login_form": LoginForm})
        else:
            #Nothing has been provided for username or password.
            return render(request, 'core/login.html', {"login_form": LoginForm})
    else:
        login_form = LoginForm()
        page_data = { "login_form": login_form }
        return render(request, 'core/login.html', page_data)

@login_required(login_url='/login/')
def user_logout(request):
 logout(request)
 return redirect("/")

@login_required(login_url='/login/')
def profile(request):
    user_data = User.objects.get(id=request.user.id)
    tool_data = tool.objects.filter(user=request.user)
    tools = 0
    for row in tool_data:
        if row.live or not(row.live):
            tools = tools + 1
    context = {
    "user_data": user_data,
    "tools": tools,
    }
    return render(request, 'core/profile.html', context)

@login_required(login_url='/login/')
def edit(request, id):
    if (request.method == "GET"):
    	userProfile = User.objects.get(id=id)
    	edit_form = editProfileForm(instance=userProfile)
    	context = {
        "form_data" : edit_form,
         }
    	return render(request, 'core/editProfile.html', context)
    elif (request.method == "POST"):
    	# Process form submission
    	if ("edit" in request.POST):
            edit_form = editProfileForm(request.POST)
            if (edit_form.is_valid()):
                user_data = User.objects.get(id=request.user.id)
                user_data.first_name = edit_form.cleaned_data["first_name"]
                user_data.last_name = edit_form.cleaned_data["last_name"]
                user_data.email = edit_form.cleaned_data["email"]
                user_data.save()
                return redirect("/profile/")
            else:
                context = {
    			"form_data": edit_form
    			}
                return render(request, 'core/editProfile.html', context)
    	else:
    		#Cancel
    		return redirect("/profile/")
