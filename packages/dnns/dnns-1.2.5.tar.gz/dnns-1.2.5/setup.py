
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='dnns',  
     version='1.2.5',
     scripts=['worker.py'] ,
     author="Kevin Ryczko",
     author_email="kryczko@uottawa.ca",
     description="A deep learning package for using HDF5 and Pytorch (Distributed Data Parallel with NVIDIA mixed-precision) with ease.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/CLEANit/dnns.git",
     packages=setuptools.find_packages(),
     install_requires=[
        'torch',
        'apex==1.0.0'
     ],
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
     ],
     dependency_links=['https://github.com/NVIDIA/apex/tarball/master#egg/=apex-1.0.0']
 )
