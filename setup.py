import setuptools


with open('README.md') as f:
    long_discription = f.read()


setuptools.setup(
        name = 'ilonimi',
        version = '1.3.0',
        author = 'nymwa',
        author_email = 'nymwa0@gmail.com',
        description = 'Toki Pona Tokenizer / Detokenizer / Kanaizer',
        long_discription = long_discription,
        long_discription_content_type = 'text/markdown',
        url = 'https://github.com/nymwa/ilonimi',
        classifiers = [
            'Programming Language :: Python :: 3.8',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent'],
        packages = setuptools.find_packages(),
        entry_points = {'console_scripts':['nimi = ilonimi.main:main']})

