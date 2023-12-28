from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from core.models import User
from .models import Customer,Address

# Create your views here.

def register(request):
    if request.method == "POST":
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        
        if password == confirm_password:
            if User.objects.filter(username = username).exists():
                messages.info(request,'Username is Alrady Exist')
                return redirect('/appuser/register')
            if User.objects.filter(email = email).exists():
                messages.info(request,'Email is Alrady Exist')
                return redirect('/appuser/register')
            else:
                user = User.objects.create_user(
                    username = username,
                    password = password,
                    email = email
                    )
                user.set_password(password)
                user.save()
                return redirect('/appuser/log-in')
        else:
            messages.info(request,'Password Do not Match')
            return redirect('/appuser/register')
    return render(request,'appuser/register.html')
            

def log_in(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('/appuser/user-info')
        else:
            messages.info(request,"Invalid Username And Password")
            return redirect('/appuser/log-in')
    return render(request,'appuser/login.html')



def log_out(request):
    auth.logout(request)
    return redirect('/')



@login_required(login_url='/appuser/log-in')
def user_info(request):
    user = request.user
    customer = Customer.objects.filter(user_id=user.id).first()
    address = Address.objects.filter(customer=customer).first()
    context = {'user': user, 'customer': customer, 'address': address}
    return render(request, 'appuser/test/userinfo.html',context)

@login_required(login_url='/appuser/log-in')
def update_user_info(request):
    user = request.user
    customer = Customer.objects.filter(user_id=user.id).first()
    address = Address.objects.filter(customer=customer).first()
    context = {'user': user, 'customer': customer, 'address': address}

    if request.method == 'POST':
        phone = request.POST['phone']
        date_of_birth = request.POST['date_of_birth']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        street = request.POST['street']
        city = request.POST['city']
        country = request.POST['country']

        # Update the User instance for the current user
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        # Update the Customer instance for the current user
        if customer:
            customer.phone = phone
            customer.date_of_birth = date_of_birth
            customer.save()
        else:
            Customer.objects.create(phone = phone,date_of_birth = date_of_birth,user_id=user.id)
            

        # Update the Address instance for the current user
        if address:
            address.street = street
            address.city = city
            address.country = country
            address.save()
        else:
            Address.objects.create(street=street, city=city, country=country, customer=customer)

        return redirect('/appuser/user-info')

    return render(request, 'appuser/test/update_user_info.html', context)






def registration_error(request):
    return  render(request,'appuser/registration_error.html')