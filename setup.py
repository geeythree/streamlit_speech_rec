"""St_Audiorec's setup.py.

This file was autogenerated by pypackage. To make changes, you
should edit the pypackage.meta rather than this setup.py.
"""


from setuptools import setup
from setuptools import find_packages


setup(
    name='st_audiorec',
    py_modules=['__init__'],
    include_package_data=True,
    package_data={
        'st_audiorec': ['frontend\\.env',
        'frontend\\.prettierrc',
        'frontend\\package-lock.json',
        'frontend\\package.json',
        'frontend\\tsconfig.json',
        'frontend\\public\\bootstrap.min.css',
        'frontend\\public\\index.html',
        'frontend\\public\\styles.css',
        'frontend\\src\\index.tsx',
        'frontend\\src\\react-app-env.d.ts',
        'frontend\\src\\StreamlitAudioRecorder.tsx']
    },
    packages=find_packages(exclude=['test', 'tests']),
)
