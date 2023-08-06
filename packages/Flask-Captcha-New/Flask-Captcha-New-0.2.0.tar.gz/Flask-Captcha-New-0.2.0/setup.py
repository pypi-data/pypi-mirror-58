import os
import uuid
from setuptools import setup, find_packages

try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements

# parse_requirements() returns generator of pip.req.InstallRequirement objects
if os.path.exists("requirements.txt"):
    install_reqs = parse_requirements("requirements.txt", session=uuid.uuid1())
else:
    install_reqs = parse_requirements(
        "Flask_Captcha.egg-info/requires.txt", session=uuid.uuid1())

# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='Flask-Captcha-New',
    version="0.2.0",
    description='A very simple, yet powerful, Flask captcha extension',
    author='Skyler Mantysaari',
    author_email='sm+github@samip.fi',
    url='https://github.com/samip5/flask-captcha',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Topic :: Security',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=reqs
)
