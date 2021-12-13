from setuptools import setup

setup(name='jupyter_MyVala_kernel',
      version='0.0.1',
      description='Minimalistic Vala kernel for Jupyter',
      author='nufeng',
      author_email='18478162@qq.com',
      license='MIT',
      classifiers=[
          'License :: OSI Approved :: MIT License',
      ],
      url='https://github.com/nufeng1999/jupyter-MyVala-kernel/',
      download_url='https://github.com/nufeng1999/jupyter-MyVala-kernel/tarball/0.0.1',
      packages=['jupyter_MyVala_kernel'],
      scripts=['jupyter_MyVala_kernel/install_MyVala_kernel'],
      keywords=['jupyter', 'notebook', 'kernel', 'vala'],
      include_package_data=True
      )
