import setuptools

setuptools.setup(
        name = 'ilonimi',
        version = '1.1.0',
        packages = setuptools.find_packages(),
        entry_points = {'console_scripts':['nimi = ilonimi.main:main',]})

