import os
from setuptools import setup


def _read(file_name):
    with open(os.path.join(os.path.dirname(__file__), file_name)) as file:
        return file.read()


setup(
    setup_requires=['nose2'],
    test_suite='nose2.collector.collector',
    name="jmodules",
    version=0.1,
    author="sp",
    author_email="info@sp.com",
    description="sp",
    keywords="sp ",
    packages=[
        "kube_helper",
              ],
    long_description=_read('README.md'),
    zip_safe=True,
    license="2021 sp",
    classifiers=[
        "Development Status :: Release",
        "Topic :: Adapter",
    ],
    install_requires=[
    ]
)
