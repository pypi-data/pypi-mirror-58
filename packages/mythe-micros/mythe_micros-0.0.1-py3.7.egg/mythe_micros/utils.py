#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# AUTHOR: Mythezone
# DATE: 2019/12/23 Mon
# TIME: 00:48:24

# DESCRIPTION: Utils


#----- output-----#
def cprint(s,pc=-1,show=True,end='\n'):
    if pc=='help':
        print('''
        # 显示格式: \033[显示方式;前景色;背景色m
        # ------------------------------------------------
        # 显示方式             说明
        #   0                 终端默认设置
        #   1                 高亮显示
        #   4                 使用下划线
        #   5                 闪烁
        #   7                 反白显示
        #   8                 不可见
        #   22                非粗体
        #   24                非下划线
        #   25                非闪烁
        #
        #   前景色             背景色            颜色
        #     30                40              黑色
        #     31                41              红色
        #     32                42              绿色
        #     33                43              黃色
        #     34                44              蓝色
        #     35                45              紫红色
        #     36                46              青蓝色
        #     37                47              白色
        # ------------------------------------------------
        ''')
        return
    if pc=='show':
        for i in [0,1,4,5,7,8,22,24,25,30,31,32,33,34,35,36,37,40,41,42,43,44,45,46,47]:
            cprint(s,i)
        return
    dct=dict({'default':0,'highlight':1,'underline':4,'blink':5,'reverse':7,'invisible':8,'nbold':22,
        'nunderline':24,'nblink':25,'black':30,'red':31,'green':32,'yellow':33,'blue':34,'purple':35,
        'sky':36,'white':37,'bblack':40,'bred':41,'bgreen':42,'byellow':43,'bblue':44,'bpurple':45,'bsky':46,
        'bwhite':47})
    reset='\033[0m'
    if type(pc)==int:
        style='\033[%dm'%pc
    elif type(pc)==str:
        if pc.lower() in dct:
            style='\033[%sm'%dct[pc.lower()]
        else:
            style=reset
    else:
        style=reset
    res="%s%s%s"%(style,s,reset)

    if show==True:
        print(res,end=end)
    else:
        return res

def cprints(arg):
    for s,pc in arg:
        cprint(s,pc,end=' ')

if __name__ == '__main__':
    cprint("Hello,world!",'bred')
    cprints([('a','red'),('b','yellow')])
    print("\n")
