from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='menyou',
    version='1.0',
    packages=['menyou'],
    install_requires=['pyfiglet'],
    url='https://gitlab.com/ricoflow/menyou',
    license='License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    author='Randall Speake',
    author_email='ranspeake@gmail.com',
    description='A easy-to-use console-based menu.',
    long_description_content_type='text/markdown',
    long_description=long_description,
    python_requires='>=3.6',
)
