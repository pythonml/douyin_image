import setuptools
from distutils.core import setup
setup(
    name='douyin_image',
    version='0.1',
    description='add douyin effect to text or image',
    author='Zhongqiang Shen',
    author_email='shenzhongqiang@msn.com',
    url='https://github.com/pythonml/douyin',
    packages=setuptools.find_packages(),
    install_requires=['Pillow>=5.1.0', 'numpy==1.22.0'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    entry_points={
        'console_scripts': [
            'douyin_image=douyin_image:main'
        ],
    },
)
