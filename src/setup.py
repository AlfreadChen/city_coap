from distutils.core import setup
from Cython.Build import cythonize

setup( name = 'city_coap', 
       ext_modules = cythonize(["grads.py","interface.py","main.py"]),
     )
