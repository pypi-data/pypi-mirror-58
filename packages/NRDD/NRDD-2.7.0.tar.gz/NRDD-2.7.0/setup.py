from setuptools import setup, find_packages

with open ('_version.py') as f:
    exec(f.read())

setup(name='NRDD',
      version=__version__,
      author='Stefano Scopel, Gaurav Tomar, Jong Hyun Yoon, Sunghyun Kang',
      author_email='scopel@sogang.ac.kr',
      url='https://github.com/NRDD-constraints/NRDD',
      description='A python tool for calculating the direct-detection exclusion plot for the WIMP-nucleon cross section in a non-relativistic effective model',
      long_description="""The NRDD_constraints tool provides simple interpolating functions 
                          written in python that return the most constraining limit on the 
                          dark matter-nucleon scattering cross section for a list of non-relativistic 
                          effective operators that corresponds to the diagonal terms listed in Table 2 
                          of arXiv: 1810.00607 with the exception of those proportional to a meson pole. 
                          The package contains four files: The code, NRDD_constraints.py;
                          A simple driver, NRDD_constraints-example.py; Two data files, NRDD_data1.npy, 
                          NRDD_data2.npy""",
      license='MIT',
      install_requires=['numpy', 'scipy', 'setuptools']
    )
