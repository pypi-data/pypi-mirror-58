import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='pinform',
      version='0.9.1',
      author='Sina Rezaei',
      author_email='sinarezaei1991@gmail.com',
      long_description=long_description,
      long_description_content_type="text/markdown",
      description='Python InfluxDB ORM (OSTM)',
      url='https://github.com/sinarezaei/pinform',
      license='MIT',
      packages=setuptools.find_packages(),
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
      ],
      zip_safe=False)


# setup:
# python3 setup.py sdist bdist_wheel
# twine upload dist/*

# setup on test pypi:
# python3 setup.py sdist bdist_wheel
# twine upload --repository-url https://test.pypi.org/legacy/ dist/*
