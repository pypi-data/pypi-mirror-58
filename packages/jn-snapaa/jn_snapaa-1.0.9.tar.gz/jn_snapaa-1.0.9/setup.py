from setuptools import setup

setup(
    name='jn_snapaa',
    version='1.0.9',
    author='jnddd',
    author_email='122296743@qq.com',
    url='https://zhuanlan.zhihu.com/p/26159930',
    description='a easy snap js',
    packages=['snaper'],
    install_requires=[],
    package_dir={'snaper': 'snaper'},
    package_data={'snaper': ['js/*.*']},
)