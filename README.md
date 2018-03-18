# Social Auth Template

Django project template to start a demo project.

## Install

```sh
$ django-admin.py startproject \
  --template=https://github.com/ice-creams/graphql-social-auth-template/archive/master.zip \
  social_auth

$ pipenv install
```

## Environment variables

Set the environment variables of any of these providers.

```
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=...
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=...

SOCIAL_AUTH_FACEBOOK_KEY=...
SOCIAL_AUTH_FACEBOOK_SECRET=...

SOCIAL_AUTH_TWITTER_KEY=...
SOCIAL_AUTH_TWITTER_SECRET=...
```
