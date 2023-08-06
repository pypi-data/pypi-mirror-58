#from distutils.core import setup
#import os
import setuptools

#README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

with open("README.md", "r") as fh:
    long_description = fh.read()

# allow setup.py to be run from any path
#os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setuptools.setup(
    name='python3-particle',
    version='0.1',
    packages=['particle'],
    include_package_data=True,
    license='MIT License',  # example license
    description='A Python wrapper around the Particle (particle.io) Cloud API',
    long_description=long_description,
    install_requires = [
        'python-dateutil==2.8.1',
        'pytz==2019.3',
        'requests==2.7.0',
	'pexpect==3.3'
    ],
    url='https://github.com/DarkSector/python-particle',
    author='Pronoy Chopra',
    author_email='contact@pronoy.in',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        #'Framework :: Requests',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
