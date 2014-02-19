from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [
        Extension("p3mq",
                  sources=["p3mq.pyx", "q.c", "q_ik.c", "q_ik_i.c", "q_ad.c", "q_ad_i.c"],
                  include_dirs=[numpy.get_include()]
                  )
    ],
)
