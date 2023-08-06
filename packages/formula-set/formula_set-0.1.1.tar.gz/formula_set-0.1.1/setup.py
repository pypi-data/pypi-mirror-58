import setuptools
setuptools.setup(
    name='formula_set',
    version='0.1.1',
    packages=['formula_set'],
    entry_points={
        'console_scripts': [
         'formula_set = formula_set.formula_set:main'
        ]
    },
)
