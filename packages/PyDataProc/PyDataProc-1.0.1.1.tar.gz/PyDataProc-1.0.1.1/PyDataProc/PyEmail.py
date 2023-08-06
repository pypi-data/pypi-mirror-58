import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header
import mimetypes
from email.mime.base import MIMEBase
from email import encoders
# from email import settings as stt



class PyEmail():
    def __init__(self):
        """登录邮箱
        """
        self.username = ''
        self.password = ''  #授权码
        self.smtpserver =''  #smtp邮箱服务器

    def WriteEmail(self,subject):
        """写邮件，主题
        """
        self.message = MIMEMultipart()
        self.message['From'] = self.username  #发件人
        self.message['Subject'] = Header(str(subject), 'utf-8') # 邮件主题
        return self


    def attach(self,attachs):
        """添加附件
        """
        attachs=attachs.replace('，',',')  # 中文逗号替换成英文符号
        for attach in attachs.split(','):
            filename=attach.split('/')[-1]
            ctype, encoding = mimetypes.guess_type(attach)  #text/plain None
            if ctype is None or encoding is not None:
                ctype = 'application/octet-stream'
            maintype, subtype = ctype.split('/', 1)  #text plain
            if maintype == 'text':
                fp = open(attach,'rb')
                content = MIMEText(fp.read(), subtype,'utf-8')
                fp.close()
            elif maintype == 'image':
                fp = open(attach,'rb')
                content = MIMEImage(fp.read(), subtype)
                fp.close()
            else:
                fp = open(attach, 'rb')
                content = MIMEBase(maintype, subtype)
                content.set_payload(fp.read())
                fp.close()
                encoders.encode_base64(content)
            content.add_header('Content-Disposition', 'attachment',  filename=('gbk','',filename))
            self.message.attach(content)
            return  self

    def setEmailContent(self,mail_content):
        """写正文
        """
        self.message.attach(MIMEText(mail_content, 'html', 'utf-8'))
        return  self

    def to(self,*args):
        """收件人
        """
        try:
            if len(list(args)[0])!=0:
                rece_list=[]
                self.rece_list=self.senders(args,rece_list)
                self.message['To'] =','.join(self.rece_list)
        except Exception as e:
            print('必须有收件人')
        return self


    def cc(self,*args):
        """抄送
        """
        cc_list=[]
        self.cc_list=self.senders(args,cc_list)
        self.message['Cc'] =','.join(self.cc_list)

    def bcc(self,*args):
        """密送
        """
        bcc_list=[]
        self.bcc_list=self.senders(args,bcc_list)
        self.message['Bcc'] =','.join(self.bcc_list)
        return self

    def senders(self,receivers,sender_list):
        if len(receivers) != 0:
            receivers=list(receivers)[0].replace('，',',')
            if len(receivers.split(','))>1:
                for receiver in receivers.split(','):
                    sender_list.append(receiver)
            else:
                sender_list.append(receivers)
            return sender_list
        else:
            return []

    def send(self):
        """发送
        """
        try:
            smtpObj = smtplib.SMTP()
            # 设置服务器
            smtpObj.connect(self.smtpserver)
            smtpObj.login(self.username,self.password)
            smtpObj.sendmail(self.username, self.rece_list+self.cc_list+self.bcc_list, self.message.as_string())
            print("邮件发送成功")
            smtpObj.quit()
        except smtplib.SMTPException as e:
            print("Error: 无法发送邮件")
            print(e)
