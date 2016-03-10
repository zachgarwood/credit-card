from setuptools import setup

setup(
    name='credit-card',
    description='A code challenge from Cloudspotter',
    author='Zach Garwood',
    author_email='zachgarwood@gmail.com',
    license='MIT',
    packages=['credit_card'],
    install_requires=['luhn==0.2.0'],
    entry_points={
        'console_scripts': ['credit-card=credit_card:main'],
    },
)
