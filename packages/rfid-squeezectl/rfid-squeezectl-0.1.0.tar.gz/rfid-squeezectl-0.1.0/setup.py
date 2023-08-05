import setuptools
from distutils.core import setup

setup(
  name = 'rfid-squeezectl',
  py_modules=['rfid_squeezectl'],
  version = '0.1.0',
  license='Apache',
  description = 'Control Logitech Squeezebox using RFID tags',
  author = 'Bastian Bowe',
  author_email = 'bastian.dev@gmail.com',
  url = 'https://github.com/baztian/frid-squeezectl',
  keywords = ['rfid', 'raspi', 'raspberry', 'lms', 'squeeze'],
  install_requires = [
          'pi-rc522',
      ],
  entry_points = {
      'console_scripts': [
        'rfid-squeezectl = rfid_squeezectl:main',
      ],
  },
  classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: End Users/Desktop',
    'Topic :: Multimedia :: Sound/Audio',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)