from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = [
    'numpy==1.16.4',
    'Pillow==6.2.1',
    'pycryptodome==3.9.4'
]

setup(
    name='cryptemis',
    version='0.0.6',
    install_requires=requirements,
    author="Orçun Özdemir",
    author_email="benorcunozdemir@gmail.com",
    description="Minimalist symmetric AES image encryption module for paranoids.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/0x01h/cryptemis",
    packages=['cryptemis'],
    scripts=['bin/cryptemis'],
    license='WTFPL',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "Natural Language :: English",
        "Topic :: Security :: Cryptography",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"],
)