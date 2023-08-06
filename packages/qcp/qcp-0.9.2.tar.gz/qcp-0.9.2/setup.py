from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.install import install
import sys
import os

class InstallCommand(install):
    def run(self):
        install.run(self)
        print("running InstallCommnad::run")
        cmd = 'rm -rf zqcp'
        os.system(cmd)
        cmd = 'git clone https://gitee.com/zzqq2199/qcp zqcp'
        os.system(cmd)
        cmd = 'cd zqcp && sudo make install'
        os.system(cmd)
        cmd = 'rm -rf zqcp'
        os.system(cmd)
        print("InstallCommand::run over")


setup(
    name = 'qcp',
    version = '0.9.2',
    author = 'togo',
    author_email = "zhouquanjs@qq.com",
    description = "quick scp in isomorphic enviroments",
    license = "MIT",
    url = "https://gitee.com/zzqq2199/qcp",
    packages=['qcp'],
    install_requires=[],
    cmdclass={
        'install':InstallCommand
    }
)