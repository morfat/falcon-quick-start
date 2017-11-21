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

  
   
    def __get_results(self,cursor,as_tuple=False):
        #returns results, after running db query.
        if as_tuple:
            return map(namedtuple('Result',[f[0] for f in cursor.description]))

        #we return as dictionary list
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]



    def fetch(self,sql,fields=None,as_tuple=False,many=True):
        """Default is to return results as dict. If many is given, we return a list of results else just one results."""
        cursor=self.cursor()
        cursor.execute(sql)
        if many:
            results=self.get_results(cursor,fields,as_tuple=as_tuple)
        else:
            r=cursor.fetchone()
            if cursor.rowcount:
                results=dict(zip([col[0] for col in cursor.description], r))
            else:
                results={}
        
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
        cursor=self.cursor()
        cursor.execute(self._query)
        results=self.__get_results(cursor)
        cursor.close()
        return results






        
    