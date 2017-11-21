import MySQLdb
from collections import namedtuple

from project.settings import DATABASE


class MySQL:
    """ Creates a MySQL connection when the class is instantiated"""


    def __init__(self,):
        self._connection=MySQLdb.connect(user=DATABASE.get('USER'),passwd=DATABASE.get('PASSWORD'),
                                db=DATABASE.get('NAME'),host=DATABASE.get('HOST'),port=DATABASE.get('PORT')
                            )
        self._query=None
        self._table_name=None
        self._fields=None #fields for table query on select or search. or insert



        
       
    def cursor(self): #create cursor on each call
        return self._connection.cursor()

  
   
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
        return results


    def save(self,sql,commit=True,data_list=None):
        #saves and commits updates or inserts. must return True if done so.
        last_id=None
        cursor=self.cursor()
        if data_list:
            #if we are doing many separated queries.
            """ example :  #saved=mysql.save_many(sql="UPDATE sms_outgoing SET status=%s WHERE id=%s",data_list=[(STATUS_IN_QUEUE,m.id) for m in messages]) """
            cursor.executemany(sql,data_list)
        else:
            cursor.execute(sql)
            self._query=cursor._last_executed
            last_id=cursor.lastrowid

        if commit:
            self.connection().commit()
        cursor.close()
        return last_id


    
    def table(self,table_name,fields=None): #should be called before all non custom other query methods
        self._fields=fields if fields else '*'
        self._table_name=table_name
        return self

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
    







        
    