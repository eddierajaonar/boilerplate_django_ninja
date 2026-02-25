from ninja import NinjaAPI
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from .models import Product
from .schema import *
from .auth import *

api = NinjaAPI()
User = get_user_model()

# REGISTER
@api.post("/register")
def register(request, payload: UserCreateSchema):
    user = User.objects.create(
        username=payload.username,
        password=make_password(payload.password)
    )
    return {"id": user.id}

# LOGIN
@api.post("/login")
def login(request, payload: UserCreateSchema):
    user = authenticate(username=payload.username, password=payload.password)
    if not user:
        return {"error": "Invalid credentials"}

    access = create_access_token(user.id)
    refresh = create_refresh_token(user.id)

    response = JsonResponse({"access": access})
    response.set_cookie("refresh_token", refresh, httponly=True)
    return response

# REFRESH
@api.post("/refresh")
def refresh(request):
    token = request.COOKIES.get("refresh_token")
    user_id = verify_token(token, "refresh")
    if not user_id:
        return {"error": "Invalid refresh"}

    access = create_access_token(user_id)
    return {"access": access}

# PROTECTED CRUD

def get_current_user(request):
    auth = request.headers.get("Authorization")
    if not auth:
        return None
    token = auth.split(" ")[1]
    user_id = verify_token(token)
    return user_id

@api.get("/products")
def list_products(request):
    if not get_current_user(request):
        return {"error": "Unauthorized"}

    return Product.objects.all()

@api.post("/products")
def create_product(request, payload: ProductSchema):
    if not get_current_user(request):
        return {"error": "Unauthorized"}

    product = Product.objects.create(**payload.dict())
    return product

@api.put("/products/{product_id}")
def update_product(request, product_id: int, payload: ProductSchema):
    product = Product.objects.get(id=product_id)
    for attr, value in payload.dict().items():
        setattr(product, attr, value)
    product.save()
    return product

@api.delete("/products/{product_id}")
def delete_product(request, product_id: int):
    Product.objects.filter(id=product_id).delete()
    return {"deleted": True}
