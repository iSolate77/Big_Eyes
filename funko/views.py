from django.shortcuts import render, redirect, get_object_or_404
from .models import Funko, Order, OrderFunko
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, View
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import date


class ObjectDoesNotExist(Exception):
    silent_variable_failure = True


def home(request):
    return render(request, "home.html")


def funkos_index(request):
    funkos = Funko.objects.all()
    return render(request, "funkos/index.html", {"funkos": funkos})


class FunkoCreate(LoginRequiredMixin, CreateView):
    model = Funko
    fields = ["name", "description", "image", "price", "category"]
    success_url = "/funkos"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class FunkoDetail(DetailView):
    model = Funko


class FunkoUpdate(LoginRequiredMixin, UpdateView):
    model = Funko
    fields = ["name", "description", "price", "category", 'image']
    success_url = "/funkos"


class FunkoDelete(LoginRequiredMixin, DeleteView):
    model = Funko
    success_url = "/funkos"


@login_required
def add_to_cart(request, funko_id):
    funko = get_object_or_404(Funko, id=funko_id)
    order_item, created = OrderFunko.objects.get_or_create(
        funko=funko, user=request.user, is_ordered=False)
    order_status = Order.objects.filter(user=request.user, is_ordered=False)
    if order_status.exists():
        order = order_status[0]
        if order.items.filter(funko__id=funko.id).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated")
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart")
            return redirect("order_detail")
    else:
        order_date = date.today()
        order = Order.objects.create(user=request.user, order_date=order_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart")
        return redirect("order_detail")


@login_required
def remove_from_cart(request, funko_id):
    funko = get_object_or_404(Funko, id=funko_id)
    order_status = Order.objects.filter(user=request.user, is_ordered=False)
    if order_status.exists():
        order = order_status[0]
        if order.items.filter(funko__id=funko.id).exists():
            order_item = OrderFunko.objects.filter(funko=funko)[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, "This item was removed from your cart")
            return redirect("order_detail")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("index.html")
    else:
        messages.info(request, "You do not have an active order")
        return redirect("index.html")


# @login_required
# def order(request):
    # return render(request, "funkos/orders.html", {"order": order})


class OrderList(LoginRequiredMixin, ListView):
    model = Order


class OrderDetail(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, is_ordered=False)
            context = {
                "object": order
            }
            return render(self.request, "funkos/order_detail.html", context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("/")


class OrderCreate(LoginRequiredMixin, CreateView):
    model = Order
    fields = "__all__"


class OrderDelete(LoginRequiredMixin, DeleteView):
    model = Order
    fields = "__all__"


@login_required
def assoc_items(request, funko_id, item_id):
    Funko.objects.get(id=funko_id).funkos.add(item_id)
    return redirect("detail", funko_id=funko_id)


@login_required
def unassoc_items(request, funko_id, item_id):
    Funko.objects.get(id=funko_id).funkos.remove(item_id)
    return redirect("detail", funko_id=funko_id)


def signup(request):
    error_message = "You must be logged in. Sign up if you have not"
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect("login")
        else:
            error_message = "Invalid Sign Up. Please try again"
    form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "registration/signup.html", context)


def profile(request):
    return render(request, "registration/profile.html")


# class PasswordReset(UpdateView):
#     model = User
#     fields = ["password"]
#     success_url = "/funkos"

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)


def update_profile(request):
    if request.method == "POST":
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = UserChangeForm(instance=request.user)
        context = {"form": form}
        return render(request, "registration/update_profile.html", context)
