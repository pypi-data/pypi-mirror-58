import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="p2r", # Replace with your own username
    version="0.2.2",
    author="Tser",
    author_email="807447312@qq.com",
    description="PostmanScript to RequestsScript",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tser/p2r",
    packages=setuptools.find_packages(),
    keywords="xiaobai p2r postman requests",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
    install_requires=[
    	"requests"
    ],
    entry_points={'console_scripts': [
        'p2r = p2r.p2r:main',
    ]},
)
