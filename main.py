# -*- coding: utf-8 -*-
import wx
"""使用启动画面时，新版本需要先导入adv"""
from wx import adv
import time
import re
import os
"""打开浏览器""" 
import webbrowser
from cds_begin_end import Return1
from cds_combine_class import Combine
from turn_cds_amino import Turn_Cds_Amino
from get_all_cds_class import Get_All_CDS_Class as GACC

from basic_mysql_function import Basic_MySql_Function as BMF
"""
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
主框架
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
"""
class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'Bioloy Tools',size=(1800,830),pos=(0,0))
        self.splitterwindow()
        self.create_menu()#主菜单创建
        self.create_button()#按钮创建
        self.create_text()#创建文本框
        self.create_statusbar()#创建状态栏
        self.create_toolbar()#创建工具栏
        #self.create_list()#创建列表框
        self.event_bind_button()#按钮绑定
        self.event_bind_MainMenu()#主菜单绑定
        self.event_bind_text()#文本框绑定
        
    """
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    控件设置：
    分割窗口splitterwindow;设置主菜单create_menu;设置按钮：create_button；设置文本框：create_text
    设置工具栏：create_toolbar；设置状态栏：create_statusbar；
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    """
    def splitterwindow(self):
        self.sp=wx.SplitterWindow(self,style=wx.SP_LIVE_UPDATE)
        self.panel1=wx.Panel(self.sp,-1,style=wx.SUNKEN_BORDER)
        self.panel2=wx.Panel(self.sp,-1)
        """设置颜色：蓝绿色：AQUAMARINE"""
        #self.panel1.SetBackgroundColour('MEDIUM TURQUOISE')
        #self.panel2.SetBackgroundColour('AQUAMARINE')
        self.sp.SplitVertically(self.panel1,self.panel2,150)
        self.sp.SetMinimumPaneSize(150)
     
    def create_menu(self):
        self.menubar=wx.MenuBar()
        self.menu1=wx.Menu()
        self.menu2=wx.Menu()
        self.menu3=wx.Menu()
        self.menu4=wx.Menu()
        self.upload_database=wx.Menu()
        self.upload_web=wx.Menu()
        
        self.save_cds_mysql_DB=self.upload_database.Append(-1,'Save CDS Sequence To MySqlDB')
        self.save_amino_mysql_DB=self.upload_database.Append(-1,"Save Amino Sequence To MySqlDB")
        self.save_cds_web=self.upload_web.Append(-1,"Upload To Web")
        """STEP3在菜单下面，建立选项栏，使用Append（-1，“name”）"""
        #self.m1open=self.menu1.Append(-1,"Open")
        self.m1save_cds=self.menu1.Append(-1,"Save_Cds")
        self.m1save_amino=self.menu1.Append(-1,'Save_Amino')
        self.m1save_codon=self.menu1.Append(-1,'Save_Codon_Frequency')
        self.m1quit = self.menu1.Append(-1,'Quit')
        self.m2about=self.menu2.Append(-1,"About")
        
        self.m3NCBI=self.menu3.Append(-1,'NCBI')
        self.m3PDB=self.menu3.Append(-1,'PDB')
        self.m3EMBOSS=self.menu3.Append(-1,'EMBOSS Explorer')
        self.m3ibilinux=self.menu3.Append(-1,'cqupt_ibi_linux_study')
        self.m3ibiCQUPT=self.menu3.Append(-1,"IBI CQUPT")
        self.m3CQUPTjwzx=self.menu3.Append(-1,"重庆邮电大学教务在线")
        
        self.m4save_cds_mysql_DB=self.menu4.Append(-1,"Upload DataBase",self.upload_database)
        self.m4uplaod_web=self.menu4.Append(-1,"Uplaod Web",self.upload_web)
        
        """STEP4将建好的菜单添加到菜单栏下面去，使用Append(菜单，“name”)"""
        self.menubar.Append(self.menu1,"SAVE")
        self.menubar.Append(self.menu2,"HELP")
        self.menubar.Append(self.menu4,"Upload")
        self.menubar.Append(self.menu3,"Other")
        """STEP5将菜单栏设置到主窗口中，使用SetMenuBar（）"""
        self.SetMenuBar(self.menubar)
    
    def create_statusbar(self):
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetFieldsCount(3)
        self.statusbar.SetStatusWidths([-1, -2, -1])
    
    def create_toolbar(self):
        self.toolbar=self.CreateToolBar()
    """   
    def create_list(self):
        choice=['Cds Squence','','Amino Sequence','','Codon Frequency']
        self.main_list=wx.ListBox(self.panel1,-1,(10,10),(123,700),choice,style=wx.LB_ALWAYS_SB|wx.LB_HSCROLL)
        self.main_list.SetSelection(0)
        self.main_list.SetBackgroundColour('TURQUOISE')
    """ 
    def create_button(self):
        #self.button_cds_sequence=wx.Button(self.panel1,-1,u'CdsSequence',pos=(10,10),size=(120,50))
        self.button_cds_sequence=wx.Button(self.panel1, -1,"CDS", pos = (10, 10),size=(120,50))
        self.button_cds_sequence.SetBackgroundColour('WHITE')
        self.button_amino_sequence=wx.Button(self.panel1, -1,"Amino", pos = (10, 70),size=(120,50))
        #self.button_amino_sequence=wx.Button(self.panel1,-1,u'AminoSequence',pos=(10,70),size=(120,50))
        self.button_amino_sequence.SetBackgroundColour('WHITE')
        self.button_codon_frequency=wx.Button(self.panel1,-1,"Frequency",pos=(10,130),size=(120,50))
        #self.button_codon_frequency=wx.Button(self.panel1,-1,u'CodonFrequency',pos=(10,130),size=(120,50))
        self.button_codon_frequency.SetBackgroundColour('WHITE')
    
    def create_text(self):
        self.main_text=wx.TextCtrl(self.panel2,-1,pos=(10,10),size=(1350,700),style=wx.TE_MULTILINE)
        '''
        """空闲时显示logo画面"""
        self.image12=wx.Image("textlogo.png",wx.BITMAP_TYPE_PNG)
        self.temp=self.image12.ConvertToBitmap()
        self.bmp=wx.StaticBitmap(self.main_text,bitmap=self.temp)
        self.main_text.SetBackgroundColour('WHITE')
        '''
    """
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    绑定函数：
    主菜单事件绑定函数：event_bind_MainMenu;按钮绑定函数：event_bind_button；文本框绑定函数：
    event_bind_text
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    """
    def event_bind_MainMenu(self):
        #self.menu1.Bind(wx.EVT_MENU,self.OnMenuOpen,self.m1open)
        self.menu1.Bind(wx.EVT_MENU,self.OnMenuSave_Cds,self.m1save_cds)
        self.menu2.Bind(wx.EVT_MENU,self.OnMenuAbout,self.m2about)
        self.menu1.Bind(wx.EVT_MENU,self.OnMenuAminoSequenceSave,self.m1save_amino)
        self.menu1.Bind(wx.EVT_MENU,self.OnMenuCodonFrequencySave,self.m1save_codon)
        self.menu1.Bind(wx.EVT_MENU,self.OnMenuQuit,self.m1quit)
        
        self.menu3.Bind(wx.EVT_MENU,self.OnMenuNCBI,self.m3NCBI)
        self.menu3.Bind(wx.EVT_MENU,self.OnMenuPDB,self.m3PDB)
        self.menu3.Bind(wx.EVT_MENU,self.OnMenuEMBOSS,self.m3EMBOSS)
        self.menu3.Bind(wx.EVT_MENU,self.OnMenuCQUPTibiLinux,self.m3ibilinux)
        self.menu3.Bind(wx.EVT_MENU,self.OnMenuIBICQUPT,self.m3ibiCQUPT)
        self.menu3.Bind(wx.EVT_MENU,self.OnMenuCQUPT,self.m3CQUPTjwzx)
        
        self.Bind(wx.EVT_MENU,self.OnMenuCDS_SaveDB,self.save_cds_mysql_DB)
        self.Bind(wx.EVT_MENU,self.OnMenuAmino_SaveDB,self.save_amino_mysql_DB)
        self.Bind(wx.EVT_MENU,self.OnMenuUpload_Web,self.save_cds_web)
    def event_bind_button(self):
        self.button_cds_sequence.Bind(wx.EVT_BUTTON,self.OnButtonCdsSequence)
        self.button_amino_sequence.Bind(wx.EVT_BUTTON,self.OnButtonAminoSequence)
        self.button_codon_frequency.Bind(wx.EVT_BUTTON,self.OnButtonCodonFrequency)
    def event_bind_text(self):
        self.main_text.Bind(wx.EVT_TEXT,self.OnTextMainText)
           
    """
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    子窗口（关于帮助菜单的）：
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    """
    def OnMenuAbout(self,event):
        """子窗口界面创建wx.Dialog，在self.panel下面"""
        self.dialog_main_help=wx.Dialog(None,-1,title="Help",pos=(100,100),size=(800,500))
        listDatas = ['这个软件可以帮助你从sequence.gb中提取到CDS文件，并且可以计算相应的氨基酸序列和密码子使用频率','使用步骤:','1、先将下载好的sequence.gb文件点击“CdsSequence”按钮导入。',
                     '2、第二步：等待计算得到所有CDS序列','3、点击菜单“SAVE”中Save_Cds将CDS序列逐条保存（每一个cds序列是保存在单独的txt文件中的）','其他事项：',
                     '\t按钮：AminoSequence是将提取的cds转变为氨基酸序列','\t使用方法是：先点击AminoSequence导入cds.txt，显示出氨基酸序列；最后点击SAVE中Save_Amino保存',
                     '\t按钮：CodonFrequency是计算cds中密码子的使用频率','\t使用方法是先点击CodonFrequency导入cds.txt，显示出cds密码子以及使用频率；最后点击SAVE中Save_CodonFrequency保存']
        self.help_listBox = wx.ListBox(self.dialog_main_help, -1, pos=(20, 20), size=(750, 430), style=wx.LB_SINGLE)
        """设置背景颜色和字体颜色"""
        self.help_listBox.SetBackgroundColour('white'), self.help_listBox.SetForegroundColour('sky blue') 
        self.help_listBox.SetTransparent(400)#设置透明
        #self.imagelist=wx.Image("helplistlogo.jpg",wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        #self.bmplist=wx.StaticBitmap(self.dialog_main_help,bitmap=self.imagelist)
        self.help_listBox.Append(listDatas)
    
        """显示子窗口"""
        self.dialog_main_help.ShowModal()
    
    """
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    事件函数：
    主菜单保存CDS:OnMenuSave_Cds；主菜单帮助：OnMenuAbout；主文本框：OnTextMainText
    主菜单保存Amino：OnMenuAminoSequenceSave；主菜单保存密码子使用率：OnMenuCodonFrequencySave
    计算cds序列：OnButtonCdsSequence；得到氨基酸序列：OnButtonAminoSequence；得到密码子使用率：
    OnButtonCodonFrequency;NCBI链接：OnMenuNCBI
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    """   
                
    """@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@保存CDS序列@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""    
    def OnMenuSave_Cds(self,event):
        self.statusbar.SetStatusText('      Cds       Sequence     Saveing ... ... ...!',1)
        print('test\n save')
        """同样的，如同Onopen一般，使用FileDialog来保存文件"""
        #self.up_text.SetValue('Saveing... ...')
        with wx.FileDialog(self,"Save file",wildcard="Text file (*.txt)|*.txt",style=wx.FD_SAVE) as fileDialog:
            if fileDialog.ShowModal()==wx.ID_OK:
                pathname=fileDialog.GetPath()
                print(pathname)
                """这里依然使用open的方法来写文件，使用了GetNumberOfLines()来记录
                文本的行数，使用GetLineText(i)来得到每一行的文本值"""
                r1=re.findall(r'(,)',self.main_text.GetValue())
                length=len(r1)+1
                r2=re.findall(r'\'(\w*)\'',self.main_text.GetValue())
                temp_path=pathname#保证了每一条cds都是独立的文件
                a=".txt"
                for i in range(length):
                    pathname=temp_path+str(i+1)+a
                    print(pathname)
                    #print('OH shit!\n',str(r2[i]))
                    self.main_text.SetValue(r2[i])
                    fp=open(pathname,'w')
                    number1=self.main_text.GetNumberOfLines()
                    for i in range(number1):
                        v=self.main_text.GetLineText(i)
                        fp.write(v)
                        #fp.write("\n")#换行
                    fp.close()#关闭文件
        self.statusbar.SetStatusText('      Cds       Sequence     Saved!',1)
    
    """@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@提取CDS序列@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""
    def OnButtonCdsSequence(self,event):
        self.statusbar.SetStatusText('                 Geting        Cds       Sequence     ',1)
        self.statusbar.SetStatusText('        CDS  Sequence',1)
        print('test\n cdssequence')
        self.main_text.Clear()
        total_way1=[]
        with wx.FileDialog(self,"Open file",wildcard="Text files (*.gb)|*.gb",style=wx.FD_OPEN|wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal()==wx.ID_OK:
                pathname_up=fileDialog.GetPath()
        #print(pathname_up)
        temp_pathname=pathname_up
        """该部分用于得到：一个CDS中所有碱基段都在一行上的CDS序列（碱基段比较少）"""                
        filename=temp_pathname
        with open(filename) as f:
            for line in f.readlines():
                if 'CDS' in line:
                    rule1=re.findall(r'\((.+)\)',line)
                    if rule1:
                        #print('阶段性测试：碱基段少：\n',str(line))
                        Re=Return1(line)
                        temp_total_way1=Re
                        total_way1=temp_total_way1.way1()
                        #print('total_way1\n',str(total_way1))
                    else:
                        pass
        f.close()
        #print('total:\n',str(total_way1))
        """该部分用于得到：一个CDS中所有碱基段不只在一行上的CDS序列（碱基段比较多）""" 
        with open(filename) as f1:
            line2=f1.readlines()
            #print(line2)
            """得到碱基段不只一行的cds字符位置"""
            new2,position_new3=[],[]
            for s in range(len(line2)):
                rule1_1=re.findall(r'(,\n)',line2[s])
                if rule1_1 and ('CDS' in line2[s]) :
                    #print('tetetetet\n',str(line2[s]))
                    new2.append(line2[s])
                    position_new3.append(s)
                    print('阶段测试组：cds_position\n',str(position_new3))
                else:
                    pass
        """
        下面部分为：每一条CDS序列的合并
        """
        """生成新列表"""
        position_new2=position_new3
        lis2= []
        for i2 in range(int(len(position_new2))):
            lis2.append([])
        #print(lis2)
        """得到碱基段不只一行的所有碱基段位置"""
        all_line1=[]
        for m in range(len(position_new2)):
            all_line=[]
            all_line.append(line2[position_new2[m]])
            print('test\n',str(all_line))
            for m2 in range(1,100):
                if re.findall(r'(.*\))',line2[position_new2[m]+m2]):
                    all_line.append(line2[position_new2[m]+m2])
                    break
                else:
                    all_line.append(line2[position_new2[m]+m2])
            all_line1.append(all_line)#二维列表
        print('阶段测试组：all_cds\n',str(all_line1))
        tem11=[]
        for m3 in range(len(all_line1)):
            tem=all_line1[m3]
            tem1=''.join(map(str,tem))
            tem1=str(tem1)
            """去掉字符串中空格"""
            tem1=re.split(r'\s+',tem1)
            """合并成字符串"""
            tem1=''.join(map(str,tem1))
            tem11.append(tem1)
            #print('阶段测试组：CDS_SEQUENCE\n',str(tem11))
            """调用方法得到碱基段位置列表"""
            #print('hahahahha\n',str(tem1))
            Re=Return1(tem1)
            tem_total_way1=Re
            total_way1=tem_total_way1.way1()
        #print('total:\n',str(total_way1))
        
        combine1=Combine(total_way1,temp_pathname)
        re_combine11=combine1.cdscombine()
        #print('test1:\n',str(re_combine11))
        length=re_combine11[1]
        print('number of CDS\n',str(length))
        re_combine12=re_combine11[0]
        re_combine1=str(re_combine12)
        str11='该基因一共有CDS序列：\n'
        str12=str11+str(length)
        print('AAAAAAAA\nAAAAAAA\n',str(re_combine1))
        self.main_text.SetValue(re_combine1)
        self.statusbar.SetStatusText('                 Geted                   Cds           Sequence!',1)
        return re_combine1
        
    """@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@将CDS序列转化为Amino序列@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""
    def OnButtonAminoSequence(self,event):
        self.statusbar.SetStatusText('                     Aimno              Sequence   ... ... ...',1)
        print('test\naminosequence')
        self.main_text.Clear()
        with wx.FileDialog(self,"Open file",wildcard="Text files (*.txt)|*.txt",style=wx.FD_OPEN|wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal()==wx.ID_OK:
                pathname_open=fileDialog.GetPath()
                #print(pathname_open)
                """使用open读入文件，AppendText将列表中所有字符都显示出来，而SetValue是逐行显示
                最终只显示列表中的最后一个字符"""
                fp=open(pathname_open,'r')
                tempstr=fp.readlines()
                print(tempstr)
                for line in tempstr:
                    self.main_text.AppendText(line)
                fp.close()
                
        cds_sequence=self.main_text.GetValue()
        cds_sequence_list=[]
        for pp in cds_sequence:
            cds_sequence_list.append(pp)
        TA=Turn_Cds_Amino(cds_sequence_list)
        amino_sequence=TA.turn_cds_to_amino()
        print('AAAAAAAA1\nAAAAAAA1\n',str(amino_sequence))
        self.main_text.SetValue(amino_sequence)
        self.statusbar.SetStatusText('                     Aimno              Sequence            End!',1)
    """@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@保存Amino序列@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""
    def OnMenuAminoSequenceSave(self,event):
        self.statusbar.SetStatusText('              Amino              Sequence            Saveing ... ... ...!',1)
        with wx.FileDialog(self,"Save file",wildcard="Text file (*.txt)|*.txt",style=wx.FD_SAVE) as fileDialog:
            if fileDialog.ShowModal()==wx.ID_OK:
                pathname=fileDialog.GetPath()
                print(pathname)
                """这里依然使用open的方法来写文件，使用了GetNumberOfLines()来记录
                文本的行数，使用GetLineText(i)来得到每一行的文本值"""
                fp=open(pathname,'w')
                number1=self.main_text.GetNumberOfLines()
                for i in range(number1):
                    v=self.main_text.GetLineText(i)
                    fp.write(v)
                    #fp.write("\n")#换行
                fp.close()#关闭文件
        self.statusbar.SetStatusText('              Amino         Sequence           Saved!',1)
    
    """@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@计算CDS序列中密码子的出现频率@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""
    def OnButtonCodonFrequency(self,event):
        self.statusbar.SetStatusText('                         Calculate         Codon       Frequency!',1)
        print('test\n codonfrequency')
        self.main_text.Clear()
        with wx.FileDialog(self,"Open file",wildcard="Text files (*.txt)|*.txt",style=wx.FD_OPEN|wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal()==wx.ID_OK:
                pathname_open=fileDialog.GetPath()
                #print(pathname_open)
                """使用open读入文件，AppendText将列表中所有字符都显示出来，而SetValue是逐行显示
                最终只显示列表中的最后一个字符"""
                fp=open(pathname_open,'r')
                tempstr=fp.readlines()
                print(tempstr)
                for line in tempstr:
                    self.main_text.AppendText(line)
                fp.close()
                
        cds_sequence=self.main_text.GetValue()
        #print('阶段性测试组：cds_sequence\n',str(cds_sequence))
        cds_sequence_list=[]
        for pp in cds_sequence:
            cds_sequence_list.append(pp)
        #print('观测当前CDS值是否为一维列表，如是则可以导入函数中计算\n',str(cds_sequence_list))
        TA=Turn_Cds_Amino(cds_sequence_list)
        amino_sequence=TA.turn_cds_to_amino()
        print('阶段性测试组：amino\n',str(amino_sequence))
        
        """计算每一种密码子出现的次数"""
        number_coding=TA.number_coding_use()
        print("\n\n\t\t\t\tthe number that a kind of coding from CDS sequence was:\n\n\n")
        print(number_coding)

        """计算出每一种密码子出现的频率"""
        frequency=TA.frequency_coding_use()
        print("\n\n\t\t\t\tthe frequency that a kind of coding from CDS sequence was:\n\n\n")
        print(frequency)

        """将字典值列表化"""
        codon,number,frequencies=[],[],[]
        for index,value in number_coding.items():
            codon.append(index)#密码子
            number.append(value)#个数
        for value1 in frequency.values():
            frequencies.append(value1)#频率
        #print(codon)
        fk=frequency.keys()
        fk=list(fk)
        #print('键\n',str(fk))
        fv=frequency.values()
        fv=list(fv)
        #print(fv)
        fkv=['\t\t\t密码子出现频率:\n\t\t']
        for i in range(len(fv)):
            fkv.append(fk[i])
            fkv.append('  :  ')
            fkv.append(fv[i])
            fkv.append('\n\t\t')
        fkv=''.join(map(str,fkv))
        print(fkv)
        self.SetFont(wx.Font(20, wx.FONTFAMILY_SWISS, wx.NORMAL, wx.NORMAL, False,u'黑体'))
        self.main_text.SetValue(fkv)
    
    """@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@保存密码子出现频率@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""        
    def OnMenuCodonFrequencySave(self,event):
        self.statusbar.SetStatusText('     Codon      Frequency      Saveing ... ... ...',1)
        print('test\nsavecodonfrequency')
        with wx.FileDialog(self,"Save file",wildcard="Text file (*.txt)|*.txt",style=wx.FD_SAVE) as fileDialog:
            if fileDialog.ShowModal()==wx.ID_OK:
                pathname=fileDialog.GetPath()
                print(pathname)
                """这里依然使用open的方法来写文件，使用了GetNumberOfLines()来记录
                文本的行数，使用GetLineText(i)来得到每一行的文本值"""
                fp=open(pathname,'w')
                number1=self.main_text.GetNumberOfLines()
                for i in range(number1):
                    v=self.main_text.GetLineText(i)
                    fp.write(v)
                    fp.write('\n')#换行
                fp.close()#关闭文件
        self.statusbar.SetStatusText('     Codon      Frequency      Saved!',1)
        
    def OnMenuNCBI(self,event):
        webbrowser.open("https://www.ncbi.nlm.nih.gov/")
        
    def OnMenuPDB(self,event):
        webbrowser.open("http://www.rcsb.org/")
        
    def OnMenuEMBOSS(self,event):
        webbrowser.open("http://www.bioinformatics.nl/emboss-explorer/")
        
    def OnMenuCQUPTibiLinux(self,event):
        webbrowser.open('http://ibi.cqupt.edu.cn/bioinfo/course/linux/')
        
    def OnMenuIBICQUPT(self,event):
        webbrowser.open('http://ibi.cqupt.edu.cn/new/')
         
    def OnMenuCQUPT(self,event):
        webbrowser.open('http://jwzx.cqupt.edu.cn/')
            
    def OnTextMainText(self,event):
        print('test\n maintext')
        """一有事件响应便破坏位图"""
        self.bmp.Destroy()
    
    def OnMenuCDS_SaveDB(self,event):
        print('fff')
        """启用Upload_DataBase类（子窗口）"""
        win_UD=Upload_DataBase()
        win_UD.Show()
    def OnMenuAmino_SaveDB(self,event):
        """启用Upload_DataBase_Amino类（子窗口）"""
        win_UDA=Upload_DataBase_Amino()
        win_UDA.Show()
    def OnMenuUpload_Web(self,event):
        """启用Upload_DataBase类（子窗口）"""
        win_UD=Upload_DataBase()
        win_UD.Show()
        
    def OnMenuQuit(self,evt):
        os.sys.exit()
        

"""
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
UPload DataBase 类
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
"""
class Upload_DataBase(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"Upload CDS Sequence To MySqlDatabase",pos=(200,200),size=(600,460))
        self.create_UD_Button()
        self.event_UD_Button()
        self.create_UD_Text()
        self.create_UD_Gurage()
        self.create_UD_StaticText()
        self.create_UD_staticbar()
        
        self.count = 0 
        self.SetBackgroundColour('MEDIUM TURQUOISE')
         
    def create_UD_staticbar(self):
        self.UD_statusBar = self.CreateStatusBar()
        '''
        self.statusBar1.SetFieldsCount(3)
        self.statusBar1.SetStatusWidths([-1, -2, -1])
        '''
    def create_UD_StaticText(self):
        self.UD_author_statictext=wx.StaticText(self,-1,"Author",pos=(40,20),size=(50,30))
        self.UD_research_statictext=wx.StaticText(self,-1,"Douc Name",pos=(20,60),size=(70,30))
        self.UD_note_statictext=wx.StaticText(self,-1,"Note",pos=(40,100),size=(50,30))
    def create_UD_Text(self):
        self.UD_author_text=wx.TextCtrl(self,-1,"",pos=(100,20),size=(400,30))
        self.UD_researchName_text=wx.TextCtrl(self,-1,"",pos=(100,60),size=(400,30))
        self.UD_note_text=wx.TextCtrl(self,-1,"",pos=(100,100),size=(400,50),style=wx.TE_MULTILINE)
        self.UD_contents_text=wx.TextCtrl(self,-1,"",pos=(100,160),size=(400,100),style=wx.TE_MULTILINE)
    def create_UD_Gurage(self):
        self.gauge = wx.Gauge(self, -1, 100, (100, 270), (400, 20))  
        self.gauge.SetBezelFace(3)  
        self.gauge.SetShadowWidth(3)  
    def create_UD_Button(self):
        self.UD_button=wx.Button(self,-1,"UPLOAD",pos=(100,300),size=(400,50))
        self.UD_openfile_button=wx.Button(self,-1,"contents",pos=(20,160),size=(70,30))
        self.UD_openfile_button.SetBackgroundColour('MEDIUM TURQUOISE')
    def event_UD_Button(self):
        self.UD_button.Bind(wx.EVT_BUTTON,self.On_UD_Button)
        self.UD_openfile_button.Bind(wx.EVT_BUTTON,self.On_UD_Openfile_Button)
    """
    def event_UD_Gurage(self):
         self.Bind(wx.EVT_IDLE, self.OnIdle) 
    """
    def On_UD_Openfile_Button(self,event):
        researchName = self.UD_researchName_text.GetValue()
        
        print("ghhgh\n",str(researchName))
        if len(researchName)==0:
            self.UD_contents_text.SetValue("In order to better manage the database,please fill in 'author'、'docu'、'note' filrstly\n(为了方便数据库管理，请先填写author、docu、note)")
        else:
            
            with wx.FileDialog(self,"Open file",wildcard="Text files (*.gb)|*.gb",style=wx.FD_OPEN|wx.FD_FILE_MUST_EXIST) as fileDialog:
            
                if fileDialog.ShowModal()==wx.ID_OK:
                    pathname_up=fileDialog.GetPath()
            #print(pathname_up)
            temp_pathname=pathname_up
            gacc = GACC(temp_pathname)
            contents=gacc.getCDS()
            """设置到text"""
            print('klkl\n\n')
            print(contents)
            print("len:\n",str(len(contents)))
            for i in range(len(contents)):
                print("temp:\n",contents[i])
                self.UD_contents_text.SetValue(contents[i])
                content = self.UD_contents_text.GetValue()
                '''保存文本到指定目录'''
                temp_path="G:/test_for_cds_mysql/"
                number=str(i)
                temp=".txt"
                filename=temp_path+str(researchName)+number+temp
                fh = open(filename, 'w')
                fh.write(content)
                print("\n\nsd",str(content))
                #self.UD_contents_text.Clear()
                #del content
                fh.close()          
    
    def On_UD_Button(self,event):
        test_contents = self.UD_contents_text.GetValue()
        if len(test_contents)==0:
            self.UD_contents_text.SetValue("In order to better manage the database,please run the button:'contents',firstly")
        else:
            print("yes")
            '''获得组件中的文本'''
            author=self.UD_author_text.GetValue()
            researchName = self.UD_researchName_text.GetValue()
            note = self.UD_note_text.GetValue()
            print(author,researchName,note)
            '''将数据保存到数据库'''
            bmf=BMF("cds_sequence")
            """得到当前数据库中的id"""
            temp_getid=bmf.MySql_Select_All()
            getid=list(temp_getid[-1])[0]
            print(getid)
            """向数据库中上传相应的值"""
            #a=bmf.MySql_Selection("path","cds_sequence","'%s'",'1')
            all_datas=bmf.MySql_Select_All()#得到返回的所有数据列表
            bmf.MySql_Insert(int(getid+1),str(author),str(researchName),str(note),int(0))
            
            self.count = self.count + 99
            if self.count >= 100:  
                self.count = 0  
            self.gauge.SetValue(self.count) 
            
            
            self.UD_statusBar.SetStatusText("                      \t\t\t\t\t\t\t Uploaded!                ")
            
        
"""
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
UPload DataBase Amino类
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
"""
class Upload_DataBase_Amino(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"Upload Amino Sequence To MySqlDatabase",pos=(200,200),size=(600,460))
        self.create_UDA_Button()
        self.event_UDA_Button()
        self.create_UDA_Text()
        self.create_UDA_Gurage()
        self.create_UDA_StaticText()
        self.create_UDA_staticbar()
        
        self.UDA_count = 0 
        #self.SetBackgroundColour('MEDIUM TURQUOISE')
        self.SetBackgroundColour('WHITE')
         
    def create_UDA_staticbar(self):
        self.UDA_statusBar = self.CreateStatusBar()

    def create_UDA_StaticText(self):
        self.UDA_author_statictext=wx.StaticText(self,-1,"Author",pos=(40,20),size=(50,30))
        self.UDA_research_statictext=wx.StaticText(self,-1,"Douc Name",pos=(20,60),size=(70,30))
        self.UDA_note_statictext=wx.StaticText(self,-1,"Note",pos=(40,100),size=(50,30))
    def create_UDA_Text(self):
        self.UDA_author_text=wx.TextCtrl(self,-1,"",pos=(100,20),size=(400,30))
        self.UDA_researchName_text=wx.TextCtrl(self,-1,"",pos=(100,60),size=(400,30))
        self.UDA_note_text=wx.TextCtrl(self,-1,"",pos=(100,100),size=(400,50),style=wx.TE_MULTILINE)
        self.UDA_contents_text=wx.TextCtrl(self,-1,"",pos=(100,160),size=(400,100),style=wx.TE_MULTILINE)
    def create_UDA_Gurage(self):
        self.UDA_gauge = wx.Gauge(self, -1, 100, (100, 270), (400, 20))  
        self.UDA_gauge.SetBezelFace(3)  
        self.UDA_gauge.SetShadowWidth(3)  
    def create_UDA_Button(self):
        self.UDA_button=wx.Button(self,-1,"UPLOAD",pos=(100,300),size=(400,50))
        self.UDA_openfile_button=wx.Button(self,-1,"contents",pos=(20,160),size=(70,30))
        #self.UDA_openfile_button.SetBackgroundColour('MEDIUM TURQUOISE')
        self.UDA_openfile_button.SetBackgroundColour('WHITE')
        self.UDA_button.SetBackgroundColour('WHITE')
    def event_UDA_Button(self):
        self.UDA_button.Bind(wx.EVT_BUTTON,self.On_UDA_Button)
        self.UDA_openfile_button.Bind(wx.EVT_BUTTON,self.On_UDA_Openfile_Button)
    def On_UDA_Openfile_Button(self,event):
        researchName = self.UDA_researchName_text.GetValue()
        print("ghhghamino\n",str(researchName))
        if len(researchName)==0:
            self.UDA_contents_text.SetValue("In order to better manage the database,please fill in 'author'、'docu'、'note' filrstly\n(为了方便数据库管理，请先填写author、docu、note)")
        else:
            with wx.FileDialog(self,"Open file",wildcard="Text files (*.txt)|*.txt",style=wx.FD_OPEN|wx.FD_FILE_MUST_EXIST) as fileDialog:
                cds_sequence_list=[]
                if fileDialog.ShowModal()==wx.ID_OK:
                    pathname_open=fileDialog.GetPath()
                    """使用open读入文件，AppendText将列表中所有字符都显示出来，而SetValue是逐行显示
                    最终只显示列表中的最后一个字符"""
                    fp=open(pathname_open,'r')
                    tempstr=fp.read()
                    print("test\n",str(tempstr))
                    for line in tempstr:
                        #print("line\n",str(line))
                        cds_sequence_list.append(line)
                    fp.close()
            print(cds_sequence_list)
            TA=Turn_Cds_Amino(cds_sequence_list)
            amino_sequence=TA.turn_cds_to_amino()
            print('AAAAAAAA1\nAAAAAAA1\n',str(amino_sequence))
            self.UDA_contents_text.SetValue(str(amino_sequence))

            content = self.UDA_contents_text.GetValue()
            '''保存文本到指定目录'''
            temp_path="G:/test_for_amino_mysql/"
            temp=".txt"
            filename=temp_path+str(researchName)+temp
            fh = open(filename, 'w')
            fh.write(content)
            print("\n\nsd",str(content))
            fh.close()   
    
    def On_UDA_Button(self,event):
        test_contents = self.UDA_contents_text.GetValue()
        if len(test_contents)==0:
            self.UDA_contents_text.SetValue("In order to better manage the database,please run the button:'contents',firstly")
        else:
            print("yes")
            '''获得组件中的文本'''
            author=self.UDA_author_text.GetValue()
            researchName = self.UDA_researchName_text.GetValue()
            note = self.UDA_note_text.GetValue()
            print(author,researchName,note)
            '''将数据保存到数据库'''
            bmf=BMF("amino_sequence")
            """得到当前数据库中的id"""
            temp_getid=bmf.MySql_Select_All()
            getid=list(temp_getid[-1])[0]
            print(getid)
            """向数据库中上传相应的值"""
            #a=bmf.MySql_Selection("path","cds_sequence","'%s'",'1')
            all_datas=bmf.MySql_Select_All()#得到返回的所有数据列表
            print(all_datas)
            bmf.MySql_Insert(int(getid+1),str(author),str(researchName),str(note),int(1))
        
            self.UDA_count = self.UDA_count + 99
            if self.UDA_count >= 100:  
                self.UDA_count = 0  
            self.UDA_gauge.SetValue(self.UDA_count) 
            
            
            self.UDA_statusBar.SetStatusText("                      \t\t\t\t\t\t\t Uploaded!                ")
            
"""
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
启动画面函数
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
"""
'''
def splashscreen():
    P1=wx.Image('logo.png',type=wx.BITMAP_TYPE_PNG).ConvertToBitmap()
    adv.SplashScreen(P1,adv.SPLASH_CENTER_ON_SCREEN|adv.SPLASH_TIMEOUT,1000,None,-1)
'''
"""
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
主事件
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
"""
app=wx.App()
'''
#启动画面
splashscreen()
time.sleep(1)
'''
win=MainFrame()
win.Show()
app.MainLoop()
