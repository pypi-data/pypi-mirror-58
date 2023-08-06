import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="arturlib",
    version="0.0.1.dev1",
    author="Artur H. Lange",
    author_email="ArturLange@poczta.fm",
    description="Small utility lib for Advent of Code and stuff",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ArturLange/arturlib",
    packages=['vectors'],
    # packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        'scipy>=1.3.0,<2',
        'sympy>=1.4,<3',
        'numpy>=1.17,<2',
        'arrow>=0.15',
        'Pillow>=6,<7'
    ],
)
