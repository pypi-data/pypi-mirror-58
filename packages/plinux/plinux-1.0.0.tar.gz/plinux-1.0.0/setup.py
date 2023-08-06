from setuptools import setup

setup(
    name='plinux',
    version='1.0.0',
    packages=['plinux'],
    url='https://github.com/agegemon/plinux',
    license='GNU General Public License v3.0',
    author='Andrey Komissarov',
    author_email='a.komisssarov@gmail.com',
    description='The cross-platform tool to execute bash commands remotely.',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'pynacl>=1.3.0',
        'bcrypt>=3.1.3',
        'cryptography>=2.5',
        'paramiko>=2.6.0',
      ],
    python_requires='>=3.6'
)
