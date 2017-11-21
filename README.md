# falcon-quick-start
Falcon API Quick start Project

#Objectives:

1. This project aims at making it easier to quickstart an app based system. E.g USSD apps, SMS gateways e.t.c
2. It implements app folders as the main authentication and authorization method.


# @TODO
3. Implment getting token ,endpoint, with renew or autorenew
4. implement pagination
5. implement model filtering methods


#Authentication.
 1. We implemented user and app authentication. All in the utils app. For user you need Token, for app you need app-key and app-secret
 2. If you choose not to authenticate, import and use the NoAuthMiddleware


#Usage

1. gunicorn -c project/wsgi_config.py project.wsgi:application

