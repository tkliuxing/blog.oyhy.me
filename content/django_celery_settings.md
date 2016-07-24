Date: 2015-07-14
Title: Django Celery 配置
Published: true
Type: post
Category: Coding
Tags: django, python, celery
Slug: django-celery-settings

下面这个例子：

* 使用 `Redis` 作为 broker 和 result backend 。
* 配置了任务日志。
* 添加了一个5分钟的周期性任务。

Django settings:

~~~~.python
BROKER_URL = 'redis://localhost/1'
CELERY_RESULT_BACKEND = 'redis://localhost/2'
CELERYD_NODES = 'w1 w2 w3'
CELERYD_MULTI = 'celery multi'
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_ACCEPT_CONTENT = ['pickle', 'json']
CELERYD_LOG_FILE="/var/log/celery/%N.log"
CELERYD_PID_FILE="/var/run/celery/%N.pid"
from datetime import timedelta
CELERYBEAT_SCHEDULE = {
    'update-access-token-every-5-min': {
        'task': 'myproject.tasks.workerfunc',
        'schedule': timedelta(minutes=5),
        'args': [],
    },
}
~~~~

*开发环境的命令行*

`celery -A wxtest worker -l info -B`

*发布环境的命令行*

`celery -A wxtest beat -s celery_beat_file`
