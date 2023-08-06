# coding=utf-8
from kombu import Exchange

# global
TASK_EXCHANGE = Exchange('ss', type='direct', durable=True)


