#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='jenkins-job-builder-multibranch-pipeline',
    version='0.2.9',
    description="Multibranch pipeline support for jenkins-job-builder",
    author="https://github.com/kennypt",
    url='https://github.com/kennypt/jenkins-job-builder-multibranch-pipeline',
    packages=['jjb_multibranch_pipeline'],
    include_package_data=True,
    install_requires=['jenkins-job-builder'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ],
    entry_points={
        'jenkins_jobs.projects': [
            'multibranch-pipeline=jjb_multibranch_pipeline.project_multibranch_pipeline:MultibranchPipeline',
        ],
        'jenkins_jobs.modules': [
            'multibranch-pipeline=jjb_multibranch_pipeline.sources:MultibranchPipeline',
        ],
    },
)
