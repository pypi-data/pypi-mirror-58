import os

from setuptools import find_packages, setup, Extension, Command
import distutils.util as dutil


class BenchmarkCommand(Command):
    user_options = []
    description = "Benchmark this package"

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        from subprocess import call
        call(['python', '-m', 'fastecdsa.benchmark'])


lib_dirs = []
include_dirs = ['src/', 'include/'] if os.name in ('nt', 'dos') else ['src/']
platform = dutil.get_platform()

if platform == 'win32':
    lib_dirs = ['libs/win32/']
elif platform == 'win-amd64':
    lib_dirs = ['libs/amd64/']

curvemath = Extension(
    'fastecdsa.curvemath',
    include_dirs=include_dirs,
    library_dirs=lib_dirs,
    libraries=['mpir'],
    sources=['src/curveMath.c', 'src/curve.c', 'src/point.c'],
    extra_compile_args=['-O2'],
    extra_link_args=["/NODEFAULTLIB:MSVCRT"]
)

_ecdsa = Extension(
    'fastecdsa._ecdsa',
    include_dirs=include_dirs,
    library_dirs=lib_dirs,
    libraries=['mpir'],
    sources=['src/_ecdsa.c', 'src/curveMath.c', 'src/curve.c', 'src/point.c'],
    extra_compile_args=['-O2'],
    extra_link_args=["/NODEFAULTLIB:MSVCRT"]
)

setup(
    author='Anton Kueltz',
    author_email='kueltz.anton@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Security :: Cryptography',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
    ],
    cmdclass={'benchmark': BenchmarkCommand},
    description='Fast elliptic curve digital signatures - built windows wheels',
    ext_modules=[curvemath, _ecdsa],
    install_requires=['six'],
    setup_requires=['wheel'],
    keywords='elliptic curve cryptography ecdsa ecc',
    license='CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
    #long_description=''.join(open('README.rst', 'r').readlines()),
    name='fastecdsa-any',
    packages=find_packages(),
    tests_require=['pytest'],
    url='https://github.com/ShadowJonathan/fastecdsa-any',
    version='1.7.5',
)
