# -*- coding: utf-8 -*-
from fabric.api import env, cd, run, prefix


env.hosts = ['root@104.131.74.168']


def deploy():
    """
    Комманда может создать файл `local.py` на удаленном сервере, если он ещё не
    создан. Если к базе данных требуется пароль, передайте параметр `db_password`.
    Пример:
        $ fab deploy
    :param db_password:
    """
    environment = prefix('source /home/.virtualenvs/djigitdev/bin/activate')

    with cd('/home/web/djigitdev'):
        with environment:
            run('git pull')
            run('pip install -r requirements.txt')
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
