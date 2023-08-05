from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="right-triangle",
    version="0.1.0",
    packages=[],
    py_modules=["right_triangle"],
    url="https://github.com/lautnerb/right-triangle",
    license="MIT",
    author="Balazs Lautner",
    author_email="lautner.balazs@gmail.com",
    description="Simple Python package that can be used to do calculations with right-angled triangles",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[],
    python_requires='~=3.7',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Typing :: Typed",
    ],
)
