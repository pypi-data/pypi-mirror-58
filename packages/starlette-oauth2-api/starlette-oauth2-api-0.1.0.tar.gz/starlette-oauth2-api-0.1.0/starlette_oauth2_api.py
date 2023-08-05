import urllib.request, json

import jose.jwt
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.types import ASGIApp, Receive, Scope, Send


def _get_json(url):
    with urllib.request.urlopen(url) as f:
        data = json.loads(f.read().decode())
    return data


class InvalidToken(Exception):
    """When a token is invalid for all identity providers"""
    def __init__(self, errors):
        self.errors = errors


def _validate_provider(provider_name, provider):
    mandatory_keys = {'issuer', 'uri', 'audience'}
    if not mandatory_keys.issubset(set(provider)):
        raise ValueError(f'Each provider must contain the following keys: {mandatory_keys}. Provider "{provider_name}" is missing {mandatory_keys - set(provider)}.')


class AuthenticateMiddleware:
    """
    A starlette middleware to authenticate and authorize requests through OAuth2 JWT tokens.

    Use ``public_paths`` to add paths that do not require authentication, e.g. `/public-endpoint`.
    Every route that is not a public path returns 401 if it does not have an authorization header with `Bearer {token}` where token is a valid jwt.

    ``providers`` must be a dictionary with the following keys:
        * ``uri``: a uri of the openid-configuration
        * ``issuer``: issuer or the tokens
        * ``audience``: audience or the tokens

    If multiple providers are passed, the request is valid if any of the providers authenticates the request.
    """
    def __init__(self, app: ASGIApp, providers, public_paths=None, get_json=None) -> None:
        self._app = app
        for provider in providers:
            _validate_provider(provider, providers[provider])
        self._providers = providers
        self._get_json = get_json or _get_json
        self._public_paths = public_paths or set()

        # cached attributes, as they are retrieved from the internet
        self._jwks = {}
        self._metadata = {}

    def provider_claims(self, provider, token):
        """
        Validates the token and returns its respective claims against a specific provider.
        """
        return jose.jwt.decode(
            token, self.jwk(provider),
            issuer=self._providers[provider]['issuer'],
            audience=self._providers[provider]['audience'],
        )

    def claims(self, token: str):
        """
        Validates the token and returns its respective claims. The token can be any of the valid providers declared 
        for this middleware.
        """
        errors = {}
        for provider in self._providers:
            try:
                return self.provider_claims(provider, token)
            except jose.exceptions.ExpiredSignatureError as e:
                # if the token has expired, it is at least from this provider.
                errors = str(e)
                break
            except jose.exceptions.JOSEError as e:  # the catch-all of Jose
                errors[provider] = str(e)
        raise InvalidToken(errors)

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        request = Request(scope)

        if request.url.path in self._public_paths:
            return await self._app(scope, receive, send)

        # check for authorization header and token on it.
        if 'authorization' in request.headers and request.headers['authorization'].startswith('Bearer '):
            token = request.headers['authorization'][len('Bearer '):]
            try:
                scope['oauth2-claims'] = self.claims(token)
            except InvalidToken as e:
                response = JSONResponse({'message': e.errors}, status_code=401)
                return await response(scope, receive, send)
        elif 'authorization' in request.headers:
            response = JSONResponse({'message': 'The "authorization" header must start with "Bearer "'}, status_code=400)
            return await response(scope, receive, send)
        else:
            response = JSONResponse({'message': 'The request does not contain an "authorization" header'}, status_code=400)
            return await response(scope, receive, send)

        return await self._app(scope, receive, send)

    def metadata(self, provider: str):
        """
        Returns the metadata of the provider. This is retrieved from the internet and cached at the first retrieval.
        """
        if self._metadata.get(provider, None) is None:
            self._metadata[provider] = self._get_json(self._providers[provider]['uri'])
        return self._metadata[provider]

    def jwk(self, provider: str):
        """
        Returns the jw keys of the provider. This is retrieved from the internet and cached at the first retrieval.
        """
        if self._jwks.get(provider, None) is None:
            self._jwks[provider] = self._get_json(self.metadata(provider)['jwks_uri'])
        return self._jwks[provider]
