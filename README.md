# test_api
Для собеседования

Для запуска:

1) docker-compose build
2) docker-compose -f docker-compose.yml up
3) docker exec -it api_test bash
4) В шеле: python manage.py migrate
5) В том же шеле: python manage.py createsuperuser


http://127.0.0.1:8000/admin/ ---> админка в которой нужно создать переводы чтобы апи отрабатывалось и могло найти хотя бы что то


http://127.0.0.1:8000/film_translate/ -------> ссылка на само апи при запуске локально



heroku:

https://thawing-everglades-53884.herokuapp.com/ | https://git.heroku.com/thawing-everglades-53884.git
    