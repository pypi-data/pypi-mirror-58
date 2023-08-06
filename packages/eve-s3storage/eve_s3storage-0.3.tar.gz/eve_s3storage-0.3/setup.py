from distutils.core import setup
from setuptools import find_packages

with open('LICENSE') as f:
    LICENSE = f.read()

setup(name='eve_s3storage',
      version='0.3',
      description='python-eve S3 MediaStorage extension',
      author='Sandro Lutz',
      author_email='code@temparus.ch',
      test_suite='eve_s3storage.tests',
      tests_require=[],
      install_requires=[
          'minio',
          'eve'
      ],
      packages=find_packages(),
      include_package_data=True,
      long_description_content_type='text/markdown',
      long_description="""Please head to the repository for the details README.""",
      license=LICENSE,
      zip_safe=False,
      url='https://gitlab.ethz.ch/amiv/eve-s3storage',
    )
