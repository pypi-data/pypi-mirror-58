from setuptools import Extension,setup,find_packages

version="0.9a24-2"

modules = [
    Extension("MatricesM.C_funcs.zerone",sources=["MatricesM/C_funcs/zerone.c"]),
    Extension("MatricesM.C_funcs.constructors",sources=["MatricesM/C_funcs/constructors.c"]),
    Extension("MatricesM.C_funcs.randgen",sources=["MatricesM/C_funcs/randgen.pyx"]),
    Extension("MatricesM.C_funcs.linalg",sources=["MatricesM/C_funcs/linalg.pyx"])
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="MatricesM",
    version=version,
    author="semihM",
    author_email="",
	license="MIT",
    description="Python>=3.6 library for creating and using matrices used in linear algebra and statistics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MathStuff/Matrices",
    packages=find_packages(),
    setup_requires=['setuptools>=18.0','cython'],
    ext_modules=modules,
    keywords=["matrix","matrices","dataframe","linear algebra","statistics","mathematics"],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
	python_requires='>=3.6',
	include_package_data=True,
)
