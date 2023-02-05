from io import BytesIO
from xhtml2pdf import pisa
from django.views import View
from django.template.loader import get_template
from django.shortcuts import render, redirect, HttpResponse

def html2pdf(template_source, context_dict={}):
     template = get_template(template_source)
     html = template.render(context_dict)
     result = BytesIO()
     pf = pisa.pisaDocument(BytesIO(html.encode("cp1252")), result)
     if not pdf.err:
          return HttpResponse(result.getvalue(), content_type="application/pdf")
     return None