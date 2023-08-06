import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PPINot4Py", # Replace with your own username
    version="1.0.2",
    license="GNU General Public License v3 (GPLv3)",
    author="Alejandro Gomez Caballero",
    author_email="agcaballero@us.es",
    include_package_data=True,
    install_requires=[
            'pandas',
            'datetime',
            'numpy',
            'pm4py'],
    description="Python version of PPINot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/isa-group/ppinot4py",
    download_url="https://github.com/isa-group/ppinot4py/archive/v_01.tar.gz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6.5',
)