from django.conf.urls import url

import project.views


urlpatterns = [
    url(r'^user_login/', project.views.user_login_request, name='user_login'),
    url(r'^form_page/', project.views.form_page, name='form_page'),

    ]