from setuptools import setup

setup(
    name='protobuf-to-dict-2',
    description='A teeny Python library for creating Python dicts from '
        'protocol buffers and the reverse. Useful as an intermediate step '
        'before serialisation (e.g. to JSON).',
    version='0.1.0',
    author='Khizer Younas',
    author_email='m.khizeryounas@gmail.com',
    url='https://github.com/mkhizeryounas/protobuf-to-dict',
    license='Public Domain',
    keywords=['protobuf', 'json', 'dict'],
    install_requires=['protobuf>=2.3.0'],
    package_dir={'':'src'},
    py_modules=['protobuf_to_dict'],
    setup_requires=['protobuf>=2.3.0', 'nose>=1.0', 'coverage', 'nosexcover'],
    test_suite = 'nose.collector',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
