import logging
import requests
import json

from .serializers import (
    TranslateApiSerializer
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from translate.models import Translate

logger = logging.getLogger(__file__)


class FilmTranslateView(APIView):
    permission_classes = ()
    authentication_classes = ()
    serializer_class = TranslateApiSerializer

    def post(self, request, *args, **kwargs):
        logger.info('Team close hook recieved!')
        response = Response(status=status.HTTP_400_BAD_REQUEST, )
        serializer = self.serializer_class(data=self.request.data)
        if not serializer.is_valid():
            logger.warning('Not a valid data.')
            return response

        data = serializer.validated_data
        film_name = data['name']

        req = requests.get(url='https://ghibliapi.herokuapp.com/films')
        content = req.json()

        needed_film = None
        for film in content:
            if film_name in film['title']:
                needed_film = film

        if not needed_film:
            return Response(status=status.HTTP_200_OK,
                            data={'data': f'film name {film_name} not found in ghibli catalog'})

        translate = Translate.objects.filter(name=data['name']).first()
        if not translate:
            logger.info(f'Film with name {film_name} not found')
            return Response(status=status.HTTP_200_OK, data={'data': f'film name {film_name} not found in database'})

        needed_film_description = needed_film['description']
        needed_film_director = needed_film['director']
        needed_film_producer = needed_film['producer']
        needed_film_release_date = needed_film['release_date']
        needed_film_rt_score = needed_film['rt_score']
        return Response(status=status.HTTP_200_OK, data={'data': f'Film {film_name}, '
                                                                 f'translate: {translate.translate}, '
                                                                 f'description: {needed_film_description}, '
                                                                 f'director: {needed_film_director}, '
                                                                 f'producer: {needed_film_producer}, '
                                                                 f'release_date: {needed_film_release_date}, '
                                                                 f'rt_score: {needed_film_rt_score}'})
