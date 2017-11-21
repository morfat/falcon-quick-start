import MySQLdb
from collections import namedtuple

from project.settings import DATABASE


class MySQL:
    """ Creates a MySQL connection when the class is instantiated"""

    """SAmple query usagge :
       #users=self.db.table('users').select()
        #users=self.db.table('users','id,email').select()
        #users=self.db.table('users').get(1)
        #users=self.db.table('users').search("first_name like '%mosoti%' ")

        #users=self.db.table('users').update(terms="first_name='ogega' ",condition="id=3")
        #users=self.db.table('users').search("first_name like '%o%' ")

        #users=self.db.table('users').insert("6,'mosoti@me.com','mogaka','F','L'")
        #users=self.db.table('users','id,email,password').insert("7,'mosoti@me.com','mogaka'")
        users=self.db.table('users').select()
        #users=self.db.table('users').delete("id=6")
    """
    


    def __init__(self,):
        self._connection=MySQLdb.connect(user=DATABASE.get('USER'),passwd=DATABASE.get('PASSWORD'),
                                db=DATABASE.get('NAME'),host=DATABASE.get('HOST'),port=DATABASE.get('PORT')
                            )
        self._query=None
        self._table_name=None
        self._fields=None #fields for table query on select or search. or insert
       
    def cursor(self): #create cursor on each call
        return self._connection.cursor()

    def commit(self):
        return self._connection.commit()

    def rollback(self):
        return self._connection.rollback()

    def close(self):
        return self._connection.close()

    def __get_results(self,fetch_one=False):
        cursor=self.cursor()
        cursor.execute(self._query)
        #returns results, after running db query.
        #if as_tuple:
        #    return map(namedtuple('Result',[f[0] for f in cursor.description]))

        #we return as dictionary list
        columns = [col[0] for col in cursor.description]
        if fetch_one:
            results=dict(zip(columns, cursor.fetchone()))
        else:
            results=[dict(zip(columns, row)) for row in cursor.fetchall()]
        cursor.close()
        self._fields=None
        return results


    def __run(self,commit=True,data_list=None):
        #saves and commits updates or inserts. must return True if done so.
        last_id=None
        cursor=self.cursor()
        if data_list:
            #if we are doing many separated queries.
            """ example :  #saved=mysql.save_many(sql="UPDATE sms_outgoing SET status=%s WHERE id=%s",data_list=[(STATUS_IN_QUEUE,m.id) for m in messages]) """
            cursor.executemany(self._query,data_list)
        else:
            cursor.execute(self._query)
            last_id=cursor.lastrowid
        if commit:
            self.commit()
        cursor.close()
        self._fields=None
        return last_id


    
    def table(self,table_name,fields=None): #should be called before all non custom other query methods
        self._fields=fields if fields else '*'
        self._table_name=table_name
        return self

    ###Data Retrival

    def select(self,offset=0,limit=1000):
        #Select records from table
        self._query="SELECT %s FROM %s LIMIT %s , %s"%(self._fields,self._table_name,offset,limit)
        return self.__get_results()
        

    def get(self,pk):#get by primary key
        #Select records from table
        self._query="SELECT %s FROM %s  WHERE id=%s "%(self._fields,self._table_name,pk)
        return self.__get_results(fetch_one=True)

    def search(self,terms):#get results by filter of where clause. et.c
        self._query="SELECT %s FROM %s  WHERE %s "%(self._fields,self._table_name,terms)
        return self.__get_results()

    def select_raw(self,sql): #run any complex select or simple select  sql query.
        #run any query
        self._query=sql
        return self.__get_results()

    ###DAta manipulate
    def update(self,terms,condition,data_list=None,commit=True):
        #write an update of the db table. 
        #if datalist is give, many update with many queries  is run. 
        #e.g query ("UPDATE sms_outgoing SET status=%s WHERE id=%s",data_list=[(STATUS_IN_QUEUE,m.id) for m in messages]
        self._query="UPDATE %s SET %s WHERE %s "%(self._table_name,terms,condition)
        return self.__run(commit=commit,data_list=data_list)

    def insert(self,values,commit=True):
        if self._fields=='*':
            self._query="INSERT INTO %s  VALUES (%s)"%(self._table_name,values)
        else:
            self._query="INSERT INTO %s (%s) VALUES (%s)"%(self._table_name,self._fields,values)
        return self.__run(commit=commit)

    def delete(self,condition,commit=True):
        self._query="DELETE FROM %s WHERE %s"%(self._table_name,condition)
        return self.__run(commit=commit)




        













        
    