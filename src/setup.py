from setuptools import setup
 
setup(name='sample',
      version='0.0.1',
      description='Sample Twisted application',
      author='Teemu Harju',
      author_email='teemu.harju@gmail.com',
      url='http://blog.teemu.im',
      packages=['sample'],
      package_data={'twisted.plugins': ['twisted/plugins/sample.py']},
      zip_safe=False
)
