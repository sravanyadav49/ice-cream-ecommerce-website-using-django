from django.shortcuts import render, redirect
from app1.models import Contact, Home, Order, Userslogin,Cart
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password

def index(request):
    if 'user_id' not in request.session:
        return redirect('login')  # Use the URL name instead of the path
    homes = Home.objects.all()
    return render(request, "index.html", {'homes': homes})

def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method == "POST":
        email = request.POST.get('email')
        feedback = request.POST.get('feedback')
        contact = Contact(email=email, feedback=feedback)
        contact.save()
        messages.success(request, "Feedback submitted successfully!")
    return render(request, "contact.html")

def menu(request):
    if request.method=='POST':
        print(request.POST)
        username=request.session['user_id']
    orders = Order.objects.all()
    return render(request, "menu.html", {'orders': orders})

def search(request):
    query = request.GET.get('query', '')
    orders = Order.objects.filter(name__icontains=query)
    return render(request, "search.html", {'orders': orders})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = Userslogin.objects.get(name=username)
            print(f"User found: {user.name}, Password entered: {password}")

            if check_password(password, user.password):
                print("Password is correct")
                request.session['user_id'] = user.name
                return redirect('index')
            else:
                print("Password is incorrect")
                messages.error(request, "Invalid credentials")
        except Userslogin.DoesNotExist:
            print("User does not exist")
            messages.error(request, "Invalid credentials")

    return render(request, 'login.html')


def logout_view(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('login')  


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            euser = Userslogin.objects.get(email=email)
            if euser != None:
                messages.error(request, "User with email already exists")
                
        except Userslogin.DoesNotExist:
             hashed_password = make_password(password)
             user = Userslogin(name=name, email=email, password=hashed_password)
             user.save()
             messages.success(request, "User created successfully!")
             return redirect('login')  
    return render(request, 'create.html')

def cart(request):
    user_name=request.session.get('user_id')
    items = Cart.objects.filter(username=user_name)
    # print(request.session)
    return render(request,'cart.html',{'items':items})


def save_order(request):
    item_name=request.POST.get('product_name')
    item_img=request.POST.get('img')
    item_price=request.POST.get('price')
    user_name=request.session.get('user_id')
    items=Cart(img=item_img,price=item_price,item_name=item_name,username=user_name )
    items.save()
    return cart(request)



def cart_view(request):
    if not request.user.is_authenticated:
        print("User is not authenticated")  # Check if the user is logged in
        return redirect('login')  # Redirect to login if user is not logged in
    
    cart_items = Cart.objects.filter(user=request.user)  # Get the user's cart items
    
    # Debugging: Check if cart items are retrieved
    print(f"Cart items: {cart_items}")
    
    total_price = sum(item.price for item in cart_items)  # Sum of prices
    
    # Debugging: Print each item's price and the total price
    for item in cart_items:
        print(f"Item price: {item.price}")
    print(f"Total price: {total_price}")
    
    context = {
        'cart_items': cart_items,
        'total_price': total_price,  # Pass the total price to the template
    }

    return render(request, 'cart.html', context)





