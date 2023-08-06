from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = [
    'requests==2.21.0',
    'validators==0.14.0',
    'numpy==1.16.4',
    'matplotlib==2.2.3',
    'tqdm==4.31.1'
]

setup(
    name='pyronos',
    version='0.0.1',
    install_requires=requirements,
    author="Orçun Özdemir",
    author_email="benorcunozdemir@gmail.com",
    description="Simple and sweet load testing module.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/0x01h/pyronos",
    packages=['pyronos'],
    scripts=['bin/pyronos'],
    license='WTFPL',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "Natural Language :: English",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"],
)