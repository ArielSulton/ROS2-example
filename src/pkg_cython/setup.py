from setuptools import setup
from Cython.Build import cythonize

package_name = 'pkg_cython'
files = package_name + "/*.py"

setup(
    ext_modules=cythonize(files,compiler_directives={'language_level' : "3"},force=True,quiet=True),
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'wheel',  'Cython'],
    zip_safe=True,
    maintainer='arielsulton',
    maintainer_email='arielsulton26@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    entry_points={
        'console_scripts': [
            'subs_cy = pkg_cython.subs_cy:main',
            'pubs_cy = pkg_cython.pubs_cy:main'
        ],
    },
)
