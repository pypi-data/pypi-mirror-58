#!/usr/bin/env python
from setuptools import setup, find_packages



setup(
    name="sentry-dingding-sean",
    version='0.0.1',
    author='sean',
    author_email='ichenxiang@vip.qq.com',
    url='',
    description='sean A Sentry extension which send errors stats to DingDing',
    long_description="sean A Sentry extension which send errors stats to DingDing",
    long_description_content_type="text/markdown",
    license='MIT',
    keywords='sentry dingding',
    include_package_data=True,
    zip_safe=False,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
        'sentry>=9.0.0',
        'requests',
    ],
    entry_points={
        'sentry.plugins': [
            'sentry_dingding = sentry_dingding.plugin:DingDingPlugin'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 2.7',
        "License :: OSI Approved :: MIT License",
    ]
)
