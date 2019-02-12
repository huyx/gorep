from setuptools import setup

setup(
    name='gorep',
    version='0.1',
    description='Gor Grep Middleware.',
    author='ycyuxin',
    author_email='ycyuxin@qq.com',
    scripts=['gorep.py'],
    entry_points='''
    [console_scripts]
    gorep=gorep:cli
    '''
)
