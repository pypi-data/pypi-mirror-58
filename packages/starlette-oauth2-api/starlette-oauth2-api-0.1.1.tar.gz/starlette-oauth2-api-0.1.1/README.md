[![pipeline status](https://gitlab.com/jorgecarleitao/Starlette-oauth2-api/badges/master/pipeline.svg)](https://gitlab.com/jorgecarleitao/Starlette-oauth2-api/commits/master)
[![coverage report](https://gitlab.com/jorgecarleitao/Starlette-oauth2-api/badges/master/coverage.svg)](https://gitlab.com/jorgecarleitao/Starlette-oauth2-api/commits/master)

# Starlette OAuth2

A Starlette middleware for authentication and authorization through JWT.

This middleware is intended to add authentication and authorization to an API (e.g. FastAPI) through an external auth provider (e.g. Microsoft AD, Auth0).

This middleware depends only on `python-jose`, which it uses to decode and validate JWT.

## How to install

```
pip install starlette-oauth2-api
```

## How to use

```
from starlette.applications import Starlette
from starlette_oauth2_api import AuthenticateMiddleware

app = Starlette()
app.add_middleware(AuthenticateMiddleware,
    {
        'example': {
            'uri': f'https://example.com/tenant-id/v2.0/.well-known/openid-configuration',
            'issuer': settings.EXAMPLE_ISSUER,
            'audience': settings.EXAMPLE_AUDIENCE,
        }
    },
    public_paths={'/'},
)
```

At this point, every route except `/` requires an `authorization: Bearer {token}` where `token` must:

* be a JWT
* be issued by `issuer` to the audience `audience`
* be signed by one of the keys declared in `jwks` of the response of `https://example.com/tenant-id/v2.0/.well-known/openid-configuration`
*  not have expired

Failing any of the conditions above returns a 401 response, failing to contain the header with `Bearer ` returns a 400 response.

When the request is valid, the Middlware adds all claims in the JWT to `oauth2-claims`, which can be accessed using

```
...
def home(request):
    ...
    request.scope['oauth2-claims']
    ...
```

In particular, if your auth provider provides custom claims, you can use these for authorization.
