from setuptools import setup, find_packages
import os
import django_xhtml2pdf

CLASSIFIERS = [
    'Environment :: Web Environment',
    'Framework :: Django',
    'Framework :: Django :: 1.11',
    'Framework :: Django :: 2.0',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.8',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
]

setup(
    author="Scott Sharkey",
    author_email="ssharkey@lanshark.com",
    name='lanshark-django-xhtml2pdf',
    url='https://gitlab.com/lansharkconsulting/django/lanshark-django-xhtml2pdf/',
    version=django_xhtml2pdf.__version__,
    description='A Django app to generate pdfs from templates',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    license='BSD License',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
        'Django',
        'xhtml2pdf'
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    options={"bdist_wheel": {"universal": "1"}},
)
