#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# AUTHOR: Mythezone
# DATE: 2019/12/23 Mon
# TIME: 00:25:18

# DESCRIPTION: A server

import socket,sys,time #,os,time,argparse,json
from multiprocessing import Process#,Manager,Lock,Queue
from utils import cprint

class server(Process):
    def __init__(self,addr,name,role='worker',links=10):
        Process.__init__(self)
        self.s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.addr=addr
        self.name=name
        self.links=links
        self.role='worker'
        self.func_route={}
        # print("self.role:",self.role)

        self.bind()

    def bind(self):
        try:
            self.s.bind(self.addr)
            print("INFO: Server %s:%s will run on - IP : %s, PORT : %s."%(cprint(self.name,'yellow',False),\
                    cprint(self.role,'sky',False),cprint(self.addr[0],'Green',False),cprint(self.addr[1],'Green',False)))
        except Exception as e:
            print("Bind Error.\n",e)
            sys.exit()

    def add(self,msg_type,func):
        pass

    def test(self,ss):
        cprint(ss,'red')

    def add_work(self,key_word,func):
        self.func_route[key_word]=func
        return

    def run(self):
        self.s.listen(self.links)
        while True:
            conn,addr=self.s.accept()


if __name__ == '__main__':
    s=server(("localhost",60001),"master")
    s.start()

    





