from setuptools import setup


setup(
      name='%NAME%',
      version='%VERSION%',
      description='GRPC client for %NAME%',
      author='Pavel Anokhin',
      author_email='p.a.anokhin@gmail.com',
      packages=['%NAME%'],
      package_data={
          '%NAME%': ['*.pyi', 'py.typed'],
      },
      include_package_data=True,
)