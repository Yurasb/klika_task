from setuptools import setup

setup(
    name='klika_task',
    version='1.0',
    packages=['pages', 'tests'],
    url='https://github.com/Yurasb/klika_task',
    license='',
    author='Yury Kuptsou',
    author_email='yurasb@tut.by',
    description='Test task for KlikaTech', install_requires=['pytest',
                                                             'selenium']
)
