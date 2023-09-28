from django.shortcuts import render
from django.http import HttpResponse
import logging


logger = logging.getLogger(__name__)


def index(request):
    logger.info('Главная страница')
    html = """
        <html>
        <head>
            <title>Главная страница</title>
        </head>
        <body>
            <h1>Главная страница</h1>
            <p>Главная страница</p>
        </body>
        </html>
    """
    return HttpResponse(html)


def about(request):
    logger.info('О себе')
    html = """
            <html>
            <head>
                <title>О себе</title>
            </head>
            <body>
                <h1>О себе</h1>
                <p>О себе</p>
            </body>
            </html>
        """
    return HttpResponse(html)
