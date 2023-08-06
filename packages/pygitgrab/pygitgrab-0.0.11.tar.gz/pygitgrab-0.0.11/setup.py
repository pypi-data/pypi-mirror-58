import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pygitgrab", 
    version="v0.0.11",
    author="k.r. goger",
    author_email="k.r.goger+pygitgrab@gmail.com",
    description="grab only certain information from remote git repo and store them local",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kr-g/pygitgrab",
    packages=setuptools.find_packages(),
    license = 'MIT',
    keywords = 'python utility shell, git',
    install_requires=[ "requests" ],    
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: POSIX :: Linux',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)

