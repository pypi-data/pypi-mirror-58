from setuptools import setup, Extension
from distutils.extension import Extension
from Cython.Build import cythonize

ext_modules = [ 
    Extension('pymt64',
               libraries = ['m'],
              depends  = ['mt64mp.h'],
               sources   = ['pymt64.pyx','pymt64lib.c','mt19937-64mp.c'] )
    ]


setup(name = 'PyMT64',
      version = '1.6',
      description = 'Python version of the Mersenne Twister 64-bit pseudorandom number generator',
      author = 'R. Samadi',
      author_email = 'reza.samadi@obspm.fr',
      url =  'http://lesia.obspm.fr/',
      long_description = open('README.txt').read(),
      long_description_content_type='text/markdown',
      ext_modules =  cythonize(ext_modules)
      )

