import sys
from form_designer.exceptions import HttpRedirectException
from django.template.base import TemplateSyntaxError
from django.http import HttpResponseRedirect

class RedirectMiddleware(object):

    def process_response(self, request, response):
        if hasattr(request, 'formDesingerRedirect'):
            return request.formDesingerRedirect
        return response
