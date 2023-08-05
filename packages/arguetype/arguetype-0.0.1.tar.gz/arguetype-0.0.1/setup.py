
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='arguetype',
      version='0.0.1',
      description='arg typing for workflows',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/dicaso/arguetype',
      author='Christophe Van Neste',
      author_email='christophe.vanneste@kaust.edu.sa',
      license='MIT',
      packages=find_packages(),
      python_requires='>=3.6',
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: POSIX",
          "Development Status :: 1 - Planning"
      ],
      install_requires=[
      
      ],
      extras_require={
          'documentation': ['Sphinx']
      },
      package_data={},
      include_package_data=True,
      zip_safe=False,
      entry_points={},
      test_suite='nose.collector',
      tests_require=['nose']
      )

# To install with symlink, to make changes immediately available:
# pip install -e .
