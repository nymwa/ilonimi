import setuptools

setuptools.setup(
        name = 'ilonimi',
        version = '0.1.0',
        packages = setuptools.find_packages(),
        entry_points = {
            'console_scripts':[
                'tunimi = ilonimi.tunimi:main',
                'wannimi = ilonimi.wannimi:main',
                ]},)
