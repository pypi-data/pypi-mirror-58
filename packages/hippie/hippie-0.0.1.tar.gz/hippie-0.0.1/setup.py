from setuptools import setup, find_packages

# with open("README.md", "r") as fh:
#   long_description = fh.read()


long_description = f"""
# hippie - Easy Hyperparameter Management
"""


setup(
  name='hippie',
  version='0.0.1',
  description='',
  long_description=long_description,
  long_description_content_type="text/markdown",
  url='https://github.com/michalwols/hippie',
  author='Michal Wolski',
  author_email='michalwols@gmail.com',
  license='MIT',
  packages=find_packages(),
  install_requires=[],
  python_requires='>=3.7',
  zip_safe=False
)
