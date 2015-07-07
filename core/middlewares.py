from django.utils import translation
from django.conf import settings
from django.middleware.locale import LocaleMiddleware


def get_language_from_request(request, check_path=False):
    return settings.LANGUAGE_CODE


class FixedLocaleMiddleware(LocaleMiddleware):
    def process_request(self, request):
        language = get_language_from_request(request)
        translation.activate(language)


class SubdomainLanguageMiddleware(object):
    """
    Set the language for the site based on the subdomain the request
    is being served on. For example, serving on 'fr.domain.com' would
    make the language French (fr).
    """
    LANGUAGES = ['en', 'es']

    def process_request(self, request):
        host = request.get_host().split('.')
        if host and host[0] in self.LANGUAGES:
            lang = host[0]
            translation.activate(lang)
            request.LANGUAGE_CODE = lang


class SubdomainMiddleware(object):
    def process_request(self, request):
        """Parse out the subdomain from the request"""
        request.subdomain = None
        host = request.META.get('HTTP_HOST', '')
        host_s = host.replace('www.', '').split('.')
        if len(host_s) > 2:
            request.subdomain = ''.join(host_s[:-2])
