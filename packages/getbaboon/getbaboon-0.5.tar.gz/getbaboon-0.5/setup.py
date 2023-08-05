import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='getbaboon',  
     version='0.5',
     scripts=['baboon'] ,
     author="Kishore",
     author_email="kishore@tealpod.com",
     description="A Simple File Copy Tool",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/prakis/baboon",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 2.7",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
