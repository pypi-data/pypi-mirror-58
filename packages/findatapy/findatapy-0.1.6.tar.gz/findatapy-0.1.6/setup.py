from setuptools import setup, find_packages

long_description = """findatapy creates an easy to use Python API to download market data from many sources including 
Quandl, Bloomberg, Yahoo, Google etc. using a unified high level interface. Users can also define their own custom 
tickers, using configuration files. There is also functionality which is particularly useful for those downloading FX market data."""

setup(name='findatapy',
      version='0.1.6',
      description='Market data library',
      author='Saeed Amen',
      author_email='saeed@cuemacro.com',
      license='Apache 2.0',
      long_description=long_description,
      keywords=['pandas', 'data', 'Bloomberg', 'tick', 'stocks', 'equities'],
      url='https://github.com/cuemacro/findatapy',
      packages=find_packages(),
      include_package_data=True,
      install_requires=['pandas',
                        'twython',
                        'pytz',
                        'requests',
                        'numpy',
                        'pandas_datareader',
                        'fxcmpy',
                        'alpha_vantage',
                        'yfinance',
                        'quandl',
                        'statsmodels',
                        'multiprocess',
                        'multiprocessing_on_dill',
                        'pathos',
                        'redis',
                        'numba',
                        'pyarrow',
                        'keyring',
                        'openpyxl'],
      zip_safe=False)
