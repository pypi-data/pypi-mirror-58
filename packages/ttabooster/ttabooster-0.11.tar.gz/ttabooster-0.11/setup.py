from setuptools import setup

setup(name='ttabooster',
      version='0.11',
      url='https://github.com/OmriKaduri/ttabooster',
      license='MIT',
      author='Seffi Cohen, Omri Kaduri',
      author_email='Kaduriomri@gmail.com',
      description='Boost pretrained models with test time augmentation selection',
      packages=['ttabooster'],
      long_description=open('README.md').read(),
      download_url='https://github.com/OmriKaduri/ttabooster/archive/0.01.tar.gz',
      zip_safe=False,
      install_requires=[  # I get to this in a second
          'numpy>=1.17.4',
          'pandas>=0.25.3',
          'tensorflow>=2.0.0',
          'scikit-learn>=0.22'],
      )
