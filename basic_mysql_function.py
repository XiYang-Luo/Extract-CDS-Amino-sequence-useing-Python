# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 19:18:37 2018

@author: luo xi yang
"""
import pymysql.cursors
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='usrName',
    passwd='your password',
    db='your database table',
    charset='gbk'
)
# 获取游标
cursor = connect.cursor()
print('A')

class Basic_MySql_Function():
    def __init__(self,tablename):
        self.tablename=tablename
        self.base,self.path="A"," G:/test_for_cds_mysql/"

        #self.database=database
        self.select,self.My_from,self.where,self.id,self.eq="SELECT "," FROM "," WHERE "," id"," = "
        self.all=" * "
        
        self.insert,self.into,self.values,self.v="INSERT "," INTO "," VALUES","(%d,'%s','%s','%s','%s','%s')"
        
    
    def MySql_Selection(self,target,limit,value):
        M_target,M_table,M_limit=str(target),str(self.tablename),limit
        sql=self.select+M_target+self.My_from+M_table+self.where+self.id+self.eq+M_limit
        print("cds:\n",str(sql))
        data = (value,)
        cursor.execute(sql % data)
        for row in cursor.fetchall():
            print('b')
            #path=list(row)[0]
            print("picturepath:%s\t" % row)
        print('共查找出', cursor.rowcount, '条数据')
    def MySql_Select_All(self):
        return_value=[]
        M_table=str(self.tablename)
        sql=self.select+self.all+self.My_from+M_table
        print('maino\n',str(sql))
        #data = (value,)
        cursor.execute(sql)
        for row in cursor.fetchall():
            #path=list(row)[0]
            return_value.append(row)
            print("datas:\n",str(row))
        print('共查找出', cursor.rowcount, '条数据')
        return return_value
        
    def MySql_Insert(self,m_id,author,researchName,note,flag):
        '''flag==0:表示要存储的是cds序列，flag==1：表示要存储蛋白质序列'''
        if int(flag)==int(0):
            path=self.path+str(researchName)
            print(path)
            sql=self.insert+self.into+self.tablename+self.values+self.v
            print(sql)
            data=(int(m_id),str(author),str(researchName),str(self.base),str(path),str(note))
            cursor.execute(sql %data)
            connect.commit()
            print('成功插入', cursor.rowcount, '条数据')
        else:
            temppath=" G:/test_for_amino_mysql/"
            path1=temppath+str(researchName)
            print(path1)
            sql=self.insert+self.into+self.tablename+self.values+self.v
            print(sql)
            data=(int(m_id),str(author),str(researchName),str(self.base),str(path1),str(note))
            cursor.execute(sql %data)
            connect.commit()
            print('成功插入', cursor.rowcount, '条数据')
        
class GetValue():
    def __init__(self):
        pass
    def get_id(self):
        bmf=Basic_MySql_Function("cds_sequence")
        """得到当前数据库中的最后一个id"""
        temp_getid=bmf.MySql_Select_All()
        getid=list(temp_getid[-1])[0]
        print('final ID:\n',str(getid))
        return int(getid)
        
        
        
        
        
        
        
        
        
        
        
