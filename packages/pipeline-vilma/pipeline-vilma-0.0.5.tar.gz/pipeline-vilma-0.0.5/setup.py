import setuptools
from pipelinevilma import __version__

setuptools.setup(
    name="pipeline-vilma",
    version=__version__,
    description="Data pipeline",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Claudio Busatto",
    author_email="cjcbusatto@gmail.com",
    url="https://github.com/cjcbusatto/pipeline-vilma",
    license="MIT",
    install_requires=[
        "pymongo==3.4.0",
        "loguru==0.3.2",
        "pika==1.1.0"
    ],
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
