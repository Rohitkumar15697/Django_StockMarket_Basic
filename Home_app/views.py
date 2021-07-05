from django.shortcuts import render, HttpResponse,redirect

from .forms import signup_form, login_form
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic import DetailView
from .models import StockModel

#This module is used for sending message to template
from django.contrib import messages  



#====View for home page====

def index(request):

    #Here both the sign_up and log_in are the black forms for showing to the template
    sign_up=signup_form()
    log_in=login_form()



    #======This is the code for signup from======

    #if signup button is clicked then this 'if' condition will run
    if request.method=='POST' and 'signup' in request.POST:
    
        try:
            sign_up=signup_form(request.POST)
            if sign_up.is_valid():
                #Saving the validated new user data to the database
                sign_up.save()  
                messages.success(request,'Account created successfully !')
                return reverse('index')

        except:
            return redirect('index')


    #=========This is the code for login form========
    
    #if login button clicked then this 'elif' condition will execute
    elif request.method=='POST' and 'login' in request.POST:
        log_in=login_form(request.POST)
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
   
        
    
    #====Here we will check if user is authenticated, only then the data of database will be visible in template=====
    
    elif request.user.is_authenticated:
        
        #This 'if' condition is for when you click on 'load more' button on the home page
        if request.POST.get('load'):
            

            #This line extracting all data elements from database and then sending them to template
            data=StockModel.objects.all()
            return render(request,'Home_app/index.html',{'signup':sign_up,'login':log_in,'data':data}) 
        

        #This line is fetching first 5 data from database and store them into data variable and then sending them to template
        data=StockModel.objects.all()[0:5]
        return render(request,'Home_app/index.html',{'signup':sign_up,'login':log_in,'data':data}) 
    
    else:    
        return render(request,'Home_app/index.html',{'signup':sign_up,'login':log_in})
    
    return render(request,'Home_app/index.html',{'signup':sign_up,'login':log_in})






#====When user clicked logout button this function will run===
@login_required(login_url='index')
def logout_user(request):
    logout(request)
    return redirect('index')






#Here is a decorator used which says if you are logged-in only then you can search for any item====

@login_required(login_url='index')
def search(request):
    #Getting the element(text) which is searched
    search_element=request.GET.get('search')
    
    #If the search field is empty then it will redirect to current page (home page)
    if search_element=="":
        return redirect('index')
    else:
        #We are taking only those records from database which are matching with search_element single character
        # can also be matched after that order_by function will order them according to the Starting character 
        # then show it to the 'search_result.html' template

        search_result=StockModel.objects.all().filter(stockname__icontains=search_element).order_by('stockname')

        # if the value of count is <=5 then only load button will show after clicking on load button it will desapear.
        count=len(search_result)
        context={'search_result':search_result,'count':count, 'search_element':search_element}
        return render(request, 'Home_app/search_result.html',context)





# This is a class for showing the detail when we click on any stockname

class detail(DetailView):
    model=StockModel
    template_name='Home_app/detail_view.html'
    context_object_name='data'
    