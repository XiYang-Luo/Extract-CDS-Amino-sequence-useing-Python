# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 22:58:14 2018

@author: luo xi yang
"""
import re
from cds_begin_end import Return1
from cds_combine_class import Combine
class Get_All_CDS_Class():
    def __init__(self,pa):
        #self.pa="E:\\2017year-study\\2017_study_下学期\\pythonGUI\\practice\\auto_cds_App1_2\\4\\sequence.gb"
        self.pa=pa
    def getCDS(self):
        with open(self.pa) as f:
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
        with open(self.pa) as f1:
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
        
        combine1=Combine(total_way1,self.pa)
        re_combine11=combine1.cdscombine()
        #print('test1:\n',str(re_combine11))
        length=re_combine11[1]
        print('number of CDS\n',str(length))
        re_combine12=re_combine11[0]
        re_combine1=str(re_combine12)
        str11='该基因一共有CDS序列：\n'
        str12=str11+str(length)
        print('AAAAAAAA\nAAAAAAA\n',str(re_combine1))
        return re_combine11[0]