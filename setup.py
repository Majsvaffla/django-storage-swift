from setuptools import setup

setup(
    name='django-storage-swift',
    version='1.3.0',
    description='OpenStack Swift storage backend for Django',
    long_description=open('README.rst').read(),
    url='https://github.com/dennisv/django-storage-swift',
    author='Dennis Vermeulen',
    author_email='blacktorn@gmail.com',
    license='MIT',
    packages=['swift'],
    install_requires=[
        'python-swiftclient>=2.2.0',
        'python-keystoneclient>=0.2.3',
        'six',
        'filetype>=1.2.0',
    ],
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
)
