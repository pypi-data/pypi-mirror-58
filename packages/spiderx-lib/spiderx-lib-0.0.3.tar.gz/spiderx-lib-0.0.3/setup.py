# coding=utf-8


from distutils.core import setup

setup(
    name='spiderx-lib',
    version='0.0.3',
    packages=[
        'spiderx_lib',
        'spiderx_lib/invoke',
    ],
    url='https://github.com/geasyheart/spiderx-lib',
    license='GPL3',
    author='yu.zhang',
    author_email='geasyheart@163.com',
    description='libs',
    install_requires=[
        'grpcio==1.26.0',
        'grpcio-tools==1.26.0',
        'kombu==4.2.1'
    ]
)
