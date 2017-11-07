#注册报名系统
#基于itchat
#请尽量使用小号登陆微信，防止被封。
BasicCommand='pip3 install itchat'
Command=''
Done=[]
import os
try:
    import itchat
    from itchat.content import *
except:
    import platform
    x=platform.platform()
    if 'Windows' in x:
        Command=''
    else:
        Command='sudo '
    print('Traceback - 导入Itchat失败，请检查权限并检查电脑中是否已安装itchat')
    print('您可以尝试手动安装itchat:')
    print(Command+BasicCommand+' 或 '+BasicCommand)
    print('您也可以选择自动安装itchat(请输入1):')
    x=input('>')
    if x=='1':
        try:
            os.system(Command+BasicCommand)
        except:
            try:
                os.system(BasicCommand)
            except:
                try:
                    os.system('pip install itchat')
                except:
                    try:
                        os.system('sudo pip install itchat')
                    except:
                        print('自动安装失败,请联系管理员.')
#Login Itchat
print('正在登陆微信...')
itchat.auto_login(hotReload=True)
#itchat.auto_login(hotReload=True)
#如果有权限或者有需要,可以选用第二个
print('微信开启成功')
print('请输入 参加/已缴/已交 参与统计')
@itchat.msg_register(TEXT,isGroupChat=True)
def main(msg):
    if '已缴' in msg['Content'] or '已交' in msg['Content'] or '参加' in msg['Content']:
        #print(msg['NickName'])
        #print(msg)
        x=msg['Content'].replace('已缴费','已交')
        x=x.replace('\n','')
        x=x.replace('已交费','已交')
        x=x.replace('已缴','已交')
        x=x.replace('已交钱','已交')
        x=x.replace('参加','已交')
        x=x.replace(' ','')
        #print(x)
        x=x.split('已交')
        #print(x)
        if len(x)>=1:
            for y in x:
                if y=='':
                    continue
                if y not in Done:
                    Done.append(y)
                    print(y+' 统计成功')
                    #itchat.send_msg(y+' 统计成功',toUserName=msg['FromUserName'])
                else:
                    print(y+' 已统计,无需重复统计')
                    #itchat.send_msg(y+' 已统计,无需重复统计',toUserName=msg['FromUserName'])
@itchat.msg_register(TEXT,isFriendChat=True)
def Output(msg):
    if msg['Content']=='导出':
        print('请稍等,正在导出')
        ReplyText=''
        if os.path.exists('Comparelist.txt'):
            print('请稍后,正在比对')
            ReplyText='未在统计列表中的有:'
            with open('Comparelist.txt') as f:
                z=f.read()
                z=list(z.split('\n'))
            for x in Done:
                if x in z:
                    z.remove(x)
            for x in z:
                ReplyText=ReplyText+'\n'+x
        ReplyText=ReplyText+'\n'+'在统计列表里的有:'
        for x in Done:
            ReplyText=ReplyText+'\n'+x
        itchat.send_msg(ReplyText,toUserName=msg['FromUserName'])
        print(ReplyText)
itchat.run()
