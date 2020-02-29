from setuptools import setup, find_packages


setup(name="protosearch",
      packages=find_packages(),
      install_requires=["ase>=3.20",
                        "numpy>=1.14"],
      )
