from setuptools import setup

setup(name='pyviz3d',
      version='0.1.1',
      description='PyViz3D is a Python package to visualize 3D point clouds.',
      url='https://github.com/francisengelmann/pyviz3d',
      download_url='https://github.com/francisengelmann/pyviz3d/archive/0.1.tar.gz',
      author='Francis Engelmann',
      author_email='francis.engelmann@gmail.com',
      license='MIT',
      packages=['pyviz3d'],
      install_requires=[
          'numpy',
          'vtk',
      ],
      zip_safe=False)
