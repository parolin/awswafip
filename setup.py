import setuptools

setuptools.setup(name='awswafip',
      version='0.1.3.3',
      description='Insert/Delete IP Address from a file in IP Address Conditions in AWS WAF',
      url='https://github.com/parolin/awswafip',
      author='Matheus L Parolin',
      author_email='mlparolin@gmail.com',
      license='GNU v3.0',
      packages=setuptools.find_packages(),
      zip_safe=False,
      #use_2to3=True,
      #long_description=open( 'README.rst' ).read(),
      install_requires=[
        'boto3',
      ],
      entry_points='''
        [console_scripts]
        awswafip=awswafip.updateips:cli
      ''',
)
