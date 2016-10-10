# -*- coding: utf-8 -*-
from fabric.api import env, cd, run, prefix, local


env.hosts = ['root@meerim.djigitdev.com']


def deploy():
    """
    Комманда может создать файл `local.py` на удаленном сервере, если он ещё не
    создан. Если к базе данных требуется пароль, передайте параметр `db_password`.
    Пример:
        $ fab deploy
    :param db_password:
    """
    environment = prefix('source /var/www/altynbek/venv/bin/activate')

    with cd('/var/www/altynbek/vision/vision'):
        with environment:
            run('git pull')
            run('pip install -r ../requirements.txt')
            run('python ./manage.py migrate')
            run('python ./manage.py collectstatic --noinput')


def start_server():
    """
    Запуск сервера gunicorn с помощью supervisord.
    Замечание: для этого необходимо иметь root привелегии.
    """
    run('supervisorctl start discount_cloud_api_gunicorn')


def stop_server():
    """
    Остановка сервера gunicorn с помощью supervisord.
    Замечание: для этого необходимо иметь root привелегии.
    """
    run('supervisorctl stop discount_cloud_api_gunicorn')


def restart_server():
    """
    Перезапуск сервера gunicorn с помощью supervisord.
    Замечание: для этого необходимо иметь root привелегии.
    """
    run('supervisorctl restart discount_cloud_api_gunicorn')


def test():
    local('source /home/altynbek/python/coder/vision-project/vision-env/bin/activate & python manage.py test')
