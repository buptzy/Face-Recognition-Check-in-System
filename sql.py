#数据库操作模块
import pyodbc
#连接到本地数据库
def con_sql():
    try:
        #服务器名称，数据库名称，用户，密码
        cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=服务器名称 ;DATABASE=数据库名称;UID=用户;PWD=密码')
        if cnxn:
            return cnxn
    except:
        print("Error:数据库连接错误!")
        return None

#获得表中全部数据
def get_feature(cnxn):
    try:
        cursor = cnxn.cursor()
        cursor.execute("Select *  from st_information")
        row = cursor.fetchall()
        if row:
            return row
    except:
        print("获得数据错误")
        return None

#获得表中全部学号
def get_sno(cnxn):
    try:
        cursor = cnxn.cursor()
        cursor.execute("Select Sno  from st_information")
        row = cursor.fetchall()
        if row:
            return row
    except:
        print("获得数据错误")
        return None

#向表中插入数据
def insert_info(cnxn, name, sno, Sclass, Sfeature, Sphoto, Srec):
    cursor = cnxn.cursor()
    cursor.execute(
        """
        insert into st_information(Sname,Sno,Sclass,Sfeature,Sphoto,Srec) values (?,?,?,?,?,?)
        """, name, sno, Sclass, Sfeature, Sphoto, Srec)
    cnxn.commit()

#更新表中数据，将签到的人的Srec标记为1
def update_time(st_Sno, time):
    cnxn = con_sql()
    cursor = cnxn.cursor()
    cursor.execute(
        """
        UPDATE st_information
        Set Srec = 1,Stime=?
         where Sno = ?
        """, time, st_Sno)
    cnxn.commit()

#选择已签到的人
def record(cnxn):
    try:
        cursor = cnxn.cursor()
        cursor.execute(
            """
            select * from st_information
            where Srec=1
            """)
        row = cursor.fetchall()
        if row:
            return row
    except:
        print("获得数据错误")
        return None


#重置签到数据
def reset_info():
    cnxn = con_sql()
    cursor = cnxn.cursor()
    cursor.execute(
        """
        UPDATE st_information
        Set Srec = 0
        """)
    cnxn.commit()
