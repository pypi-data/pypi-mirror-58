from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

# I attempted to separate test and install dependencies but couldn't figure it out (in 10 minutes). Keeping them
# toegether for now - pytest is lightweight.
setup(name="mathx",
      description="Mathematics extensions",
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='Dane Austin',
      author_email='dane_austin@fastmail.com.au',
      url='https://github.com/draustin/mathx',
      license='MIT',
      packages=find_packages(),
      install_requires=['numpy', 'scipy'],
      python_requires='>=3.5',
      use_scm_version=True,
      setup_requires=['setuptools_scm'],
      classifiers=[
            "Programming Language :: Python",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent"])
