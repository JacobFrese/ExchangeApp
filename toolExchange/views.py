from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from toolExchange.models import tool
from toolExchange.forms import postForm, requestForm
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/login/')
def toolExchange(request):
    if (request.method == "GET" and "delete" in request.GET):
    	id = request.GET["delete"]
    	tool.objects.filter(id=id).delete()
    	return redirect("/toolExchange/")
    else:
    	table_data = tool.objects.filter(user=request.user)
    	context = {
    	"table_data": table_data,
    	}
    return render(request, 'toolExchange/toolExchange.html', context)

@login_required(login_url='/login/')
def post(request):
    if (request.method == "POST"):
        if ("post" in request.POST):
            post_form = postForm(request.POST)
            if (post_form.is_valid()):
                title= post_form.cleaned_data["title"]
                description = post_form.cleaned_data["description"]
                category = post_form.cleaned_data["category"]
                price = post_form.cleaned_data["price"]
                user = User.objects.get(id=request.user.id)
                tool(user=user, title=title, description=description, category=category, price=price).save()
                return redirect("/toolExchange/")
            else:
                context = {
                "form_data": post_form
                }
                return render(request, 'toolExchange/post.html', context)
        else:
            # Cancel
            return redirect("/toolExchange/")
    else:
        context = {
        "form_data": postForm()
        }
    return render(request, 'toolExchange/post.html', context)

@login_required(login_url='/login/')
def edit(request, id):
	if (request.method == "GET"):
		Tool = tool.objects.get(id=id)
		form = postForm(instance=Tool)
		context = { "form_data" : form }
		return render(request, 'toolExchange/edit.html', context)
	elif (request.method == "POST"):
		# Process form submission
		if ("edit" in request.POST):
			form = postForm(request.POST)
			if (form.is_valid()):
				Tool = form.save(commit=False)
				Tool.user = request.user
				Tool.id = id
				Tool.save()
				return redirect("/toolExchange/")
			else:
				context = {
				"form_data": form
				}
				return render(request, 'toolExchange/edit.html', context)
		else:
			#Cancel
			return redirect("/toolExchange/")

@login_required(login_url='/login/')
def request(request, id):
	if (request.method == "GET"):
		tool_data = tool.objects.get(id=id)
		request_Form = requestForm()
		context = { "form_data" : request_Form, "tool_data" : tool_data }
		return render(request, 'toolExchange/request.html', context)
	else:
		#Cancel
		return redirect("/")



@login_required(login_url='/login/')
def toggle(request, id):
    if (request.method == "GET"):
        Tool = tool.objects.get(id=id)
        Tool.live= not Tool.live
        Tool.save()
        return redirect("/toolExchange/")
    else:
        # Cancel
        return redirect("/toolExchange/")

@login_required(login_url='/login/')
def search_tool(request):
    if (request.method == "POST"):
        searched = request.POST['searched']
        table_data = tool.objects.filter(title__contains=searched)
        context = {
        "searched" : searched,
        "table_data": table_data,
        }
        return render(request, 'toolExchange/search_tool.html', context)
    else:
        return render(request, 'toolExchange/search_tool.html')

@login_required(login_url='/login/')
def search_category_button(request):
    if (request.method == "POST"):
        searched = request.POST['Category']
        table_data = tool.objects.filter(category__contains=searched)
        context = {
        "searched" : searched,
        "table_data": table_data,
        }
        return render(request, 'toolExchange/search_tool.html', context)
    else:
        return render(request, 'toolExchange/search_tool.html')
