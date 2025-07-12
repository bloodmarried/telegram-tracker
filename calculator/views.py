from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .currency import get_crypto_price
from .forms import NumberTon
# Create your views here.

headers = {
    "X-CMC_PRO_API_KEY": " 1af90b71-a98c-413e-85dc-4cb25f7a7f6f",
    "Accepts": "application/json"
}

def test(request: HttpRequest):
    print(request.session.keys())
    
    if request.method == "POST":
        form = NumberTon(request.POST)
        
        if form.is_valid:
            num_ton = float(request.POST["TON"])
            curr = get_crypto_price("TON")
            all_price = round(num_ton * curr, 2)
            data = {"price": f"{all_price} rub"}
            return render(request, "calculator/index.html", data)
        return HttpResponse("Данные не валидны")
    elif request.method == "GET":
        return render(request, "calculator/index.html")
        
