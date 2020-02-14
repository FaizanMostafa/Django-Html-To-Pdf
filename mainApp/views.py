from django.views.generic.base import View
from wkhtmltopdf.views import PDFTemplateResponse
from django.shortcuts import render

class MyPDFView(View):
    template='index.html'
    def get(self, request):
        data={
            "greetings": "Hell yeah..."
        }
        response = PDFTemplateResponse(
            request=request,
            template=self.template,
            filename="report.pdf",
            context=data,
            show_content_in_browser=True,
            cmd_options={
                "margin-top": 10,
                "zoom": 1,
                "viewport-size": "1366 x 513",
                "javascript-delay": 500,
                "footer-center": "[page]/[topage]",
                "no-stop-slow-scripts": True
            }
        )
        return response

def index(request):
    return render(request, "index.html")