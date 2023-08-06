import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()

setuptools.setup(
     name='cnntoolcore',
     version='0.2.17',
   #   long_description=long_description,
   # long_description_content_type="text/markdown",
   #   url="https://github.com/Hyphen133/Tool-for-CNN-Interpretation-core",
     packages=setuptools.find_packages(),
    # install_requires=[            # I get to this in a second
    #           'torch',
    #           'torchvision',
    #       ],
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
     ],
 )