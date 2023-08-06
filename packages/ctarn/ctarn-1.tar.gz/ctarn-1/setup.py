import setuptools

setuptools.setup(
    name='ctarn',
    version='1',
    description='Tarn Yeong Ching',
    url='http://res.ctarn.io',
    author='Tarn Yeong Ching',
    author_email='i@ctarn.io',
    license='Public Domain',
    packages=setuptools.find_packages(exclude=('test',)),
    install_requires=[
        'matplotlib',
        'networkx',
        'numpy',
        'pillow',
        'scikit-learn',
        'scipy',
    ],
    entry_points={
        'console_scripts': [
            'ctarn-data=ctarn.util.dataset:main',
            'ctarn-rc=ctarn.demo.rc:main',
        ],
    },
)
