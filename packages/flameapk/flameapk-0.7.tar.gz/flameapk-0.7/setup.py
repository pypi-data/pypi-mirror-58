import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

     name='flameapk',  

     version='0.7',

     scripts=['flameapk.py'] ,

     author="Haroon Awan",

     author_email="mrharoonawan@gmail.com",

     description="APK Deep Data Swiss Knife",

     long_description=long_description,

   long_description_content_type="text/markdown",

     url="https://github.com/haroonawanofficial/flameapk",

     packages=setuptools.find_packages(),

     classifiers=[

         "Programming Language :: Python :: 3",

         "License :: OSI Approved :: MIT License",

         "Operating System :: OS Independent",

     ],

 )