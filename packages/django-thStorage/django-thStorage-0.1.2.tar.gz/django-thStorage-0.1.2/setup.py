import os
from setuptools import find_packages,setup

with open(os.path.join(os.path.dirname(__file__),'README.rst')) as readme:
    README = readme.read()

#allow setup.py to be run  from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__),os.pardir)))

setup(
    name='django-thStorage',
    version='0.1.2',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',
    description='A simple django app to connect to thStroage,',
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://www.nscc-tj.cn',
    author='Lichangsong&TianYang',
    author_email='lics@nscc-tj.cn',
    classifiers=[
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
