#!/usr/bin/env python3
#coding=utf-8

from fabric.api import put,sudo
from os.path import dirname,basename


class FabricCommon():
    '''
    Fabric开发过程中常用的方法
    '''
    _PythonVersion = 3
    _FabricVersion = 3
    def __CreateSalt(self):
        ''' 假装生成了一个唯一字符串 '''
        from random import sample
        from string import ascii_letters,digits
        salt = ''.join(sample(ascii_letters + digits,20))
        return salt

    def __changeModeOwner(self,dest,mode,owner,group):
        ''' 修改文件owner、group、mode '''
        sudo('chown %s:%s %s && chmod %s %s' % owner,group,dest,mode,dest)

    def files(self,src,dest,**kwargs):
        ''' 封装一个 fabric.api.put 并修改文件属性'''
        owner = kwargs['owner'] if kwargs['owner'] != None else 'root'
        group = kwargs['group'] if kwargs['group'] != None else 'root'
        mode = kwargs['mode'] if kwargs['mode'] != None else 0o644
        put(local_path=src,remote_path=dest,mode=mode, use_sudo=True)
        self.__changeModeOwner(dest,mode,owner,group)

    def readConfigFiles(self,ConfigFilePath):
        ''' 读取.conf或.ini文件,返回一个字典 '''
        from configparser import ConfigParser
        conf = ConfigParser()
        conf.read(ConfigFilePath)
        VarsDict = {}
        for section in conf.sections():
            for option in conf.options(section):
                Vars[option.upper()] = conf.get(section,option)
        return VarsDict
    def readYamlFile(self,YamlFilePath):
        ''' 读取Yaml文件,返回一个字典 '''
        from yaml import load,FullLoader
        with open(YamlFilePath,'r') as conf:
            return load(conf, Loader=FullLoader)

    def templates(self,Vars,src,dest,**kwargs):
        '''
        使用模版创建新文件并发送到远程主机,需要一个字典替换变量
        '''
        owner = kwargs['owner'] if kwargs['owner'] != None else 'root'
        group = kwargs['group'] if kwargs['group'] != None else 'root'
        mode = kwargs['mode'] if kwargs['mode'] != None else 0o644
        from jinja2 import Environment, FileSystemLoader
        environment = Environment(loader=FileSystemLoader(dirname(src)))
        content = environment.get_template(basename(src)).render(Vars)
        salt = self.__CreateSalt()
        with open('/tmp/%s' % salt,'w') as temp:
            temp.write(content)
        put(local_path='/tmp/%s' % salt, remote_path=dest,use_sudo=True)
        self.__changeModeOwner(dest,mode,owner,group)


