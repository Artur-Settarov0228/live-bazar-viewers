from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Product
from livebazar.models import Costumer   

def add_product(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        email = request.session.get("email")
        seller = Costumer.objects.filter(email=email).first()


        if not seller:
            return HttpResponse("Xatolik: Seller topilmadi. Iltimos, qaytadan tizimga kiring.", status=400)

        new_product = Product(
            seller=seller,
            name=request.POST.get("name"),
            description=request.POST.get("description"),
            category=request.POST.get("category"),
            price=request.POST.get("price"),
            discount=request.POST.get("discount"),
            quantity=request.POST.get("quantity"),
            image=request.FILES.get("image"),
            location=request.POST.get("location"),
            is_available=request.POST.get("is_available") == "on",
        )
        new_product.save()
        return redirect("seller_dashboard")
    

    return render(request, "add_product.html")
