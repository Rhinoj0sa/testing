import stripe
from django.contrib.auth.decorators import login_required
from django.contrib.messages import success
from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView, UpdateView

from . import models, forms


class HomeView(TemplateView):
    template_name = 'birdie/home.html'


class AdminView(TemplateView):
    template_name = 'birdie/admin.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        # import ipdb;ipdb.set_trace()
        return super(AdminView, self).dispatch(request, *args, **kwargs)


class PostUpdateView(UpdateView):
    model = models.Post
    form_class = forms.PostForm
    # template_name = 'birdie/update.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        print(f"request: {request}")
        if getattr(request.user, 'first_name', None) == "Martin":
            raise Http404()
        return super(PostUpdateView, self).post(request, *args, **kwargs)


class PaymentView(View):
    def post(self, request, *args, **kwargs):
        charge = stripe.Charge.create(amount=100, currency='sgd', description='', token=request.POST)
        send_mail('Payment received', 'Charge {} succed'.format(charge['id']),
                  'server@example.com',
                  ['admin@domain.com', ], )
        return redirect('/')