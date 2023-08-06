from __future__ import print_function
from setuptools import setup, find_packages
from setuptools import Command
import sys
import os

class InstallCommand(Command):
    user_options = [
        ('qcp=',None,'what')
    ]
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        print("running InstallCommnad::run")
        cmd = 'rm -rf zqcp'
        os.system(cmd)
        cmd = 'git clone https://gitee.com/zzqq2199/qcp zqcp'
        os.system(cmd)
        cmd = 'cd zqcp && sudo make install'
        os.system(cmd)
        cmd = 'rm -rf zqcp'
        os.system(cmd)

setup(
    name = 'qcp',
    version = '0.9.1',
    author = 'togo',
    author_email = "zhouquanjs@qq.com",
    description = "quick scp in isomorphic enviroments",
    license = "MIT",
    url = "https://gitee.com/zzqq2199/qcp",
    packages=['qcp'],
    install_requires=[],
    cmdclass={
        'install':InstallCommand
    },
    classifiers=[]
)