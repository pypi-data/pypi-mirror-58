from setuptools import setup
import re

version = ''
with open('asynclupa/version.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('version is not set')

readme = ''
with open('README.rst') as f:
    readme = f.read()

setup(name='AsyncLupa',
      author='SoulSen',
      url='https://github.com/SoulSen/AsyncLupa',
      project_urls={
        "Documentation": 'https://github.com/SoulSen/AsyncLupa/blob/master/README.rst',
        "Issue tracker": "https://github.com/SoulSen/AsyncLupa/issues",
      },
      version=version,
      packages=['asynclupa'],
      license='MIT',
      description='A async wrapper for Lupa',
      long_description=readme,
      long_description_content_type="text/x-rst",
      include_package_data=True,
      install_requires=['lupa'],
      python_requires='>=2',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Intended Audience :: Information Technology',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Other Scripting Engines',
          'Operating System :: OS Independent',
          'Topic :: Software Development',
      ]
)