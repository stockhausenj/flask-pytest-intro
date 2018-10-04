import io

from setuptools import find_packages, setup

setup(
    name='flask_pytest_intro',
    version='1.0.0',
    url='http://flask.pocoo.org/docs/',
    license='BSD',
    maintainer='anybody',
    maintainer_email='email@domain.com',
    description='Python CI practice.',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
    extras_require={
        'test': [
            'pytest',
        ],
    },
)
