import os
import sys
from setuptools import setup, find_packages


# (
#    (Major, Minor, [Micros]),
#    [(releaselevel, serial)],
# )
#__version_info__ = ((1, 0, 0),())
#__version_info__ = ((1, 0, 0),(rc,))
#__version_info__ = ((1, 0, 0),(rc,1))
__version_info__ = ((0, 0, 1), ('a'))


readme = os.path.normpath(os.path.join(__file__, '..', 'README.md'))
with open(readme, 'r') as fh:
    long_description = fh.read()

def get_version():
    global __version_info__
    return (
        '.'.join(str(x) for x in __version_info__[0])
        + ''.join(str(x) for x in __version_info__[1])
    )


setup(
    name='basskick',
    version=get_version(),
    description='Blender Animation Studio System',
    long_description=long_description,
    url='https://gitlab.com/basskick/basskick',
    author='Damien "dee" Coureau',
    author_email='contact@basskick.org',
    license='LGPLv3+',
    classifiers=[
        'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',

        'Topic :: System :: Shells',

        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',

        'Operating System :: OS Independent',

        'Programming Language :: Python :: 3.7',

        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
    ],
    keywords='b3d blender vfx animation pipeline workflow',
    install_requires=[
    ],
    python_requires='>=3.7',
    packages=find_packages('python'),
    package_dir={'': 'python'},
    package_data={
        '': ['*.css', '*.png', '*.svg', '*.gif'],
    },
)
