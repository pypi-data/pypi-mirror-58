import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='pixelforest_drf',
                 version='0.0.dev2',
                 description='A compilation of the applications we often use in addition to Django Rest Framework',
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 url='https://bitbucket.org/pixelforest/pixelforest_drf/',
                 author='PixelForest Dev Team',
                 author_email="devteam@pixelforest.io",
                 packages=setuptools.find_packages(),
                 classifiers=[
                       "Development Status :: 1 - Planning",
                       "Programming Language :: Python :: 3",
                       "License :: OSI Approved :: MIT License",
                       "Operating System :: OS Independent",
                 ],
                 python_requires='>=3.6',
                 )
