import json

from functools import wraps
from urllib.parse import urlparse

from flask import (
    Flask, 
    redirect,
    request,
    session
)

from .utils import (
    get_cas_client,
    get_service_url,
    authenticate,
    normalize_username,
    get_additional_info,
)

def login_sso_ui(force_login=True):
    def decorator(func):
        def wrapper(*args, **kwargs):
            service_url = get_service_url(request)
            client = get_cas_client(service_url)
            login_url = client.get_login_url()

            ticket = request.args.get("ticket")
            if ticket:
                sso_profile = authenticate(ticket, client)

                if sso_profile is None and force_login:
                    return redirect(login_url)

                kwargs.update({"sso_profile": sso_profile})
                return func(*args, **kwargs)
            else:
                return redirect(login_url)

        return wrapper

    return decorator

def logout_sso_ui(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        service_url = get_service_url(request)

        service_protocol = urlparse(service_url).scheme
        service_host = urlparse(service_url).hostname
        
        service_port = urlparse(service_url).port

        if service_port:
            service_address = service_protocol + "://" + service_host + ":" + str(service_port)
        else:
            service_address = service_protocol + "://" + service_host

        func(*args, **kwargs)

        client = get_cas_client(service_url)
        logout_url = client.get_logout_url(redirect_url=service_address)

        try:
            request.args.get("ticket")
            return redirect(logout_url)
        except:
            return redirect('/')

    return decorator