import math

class Model(object):
    db_table=''
    schema_description='Model table description'
    schema_title=db_table
    schema_properties={}
    
    pk='id'
    
    def __init__(self,db):
        self.db=db
        self.sql=''

        self.page_size=2
        self.page=None



    @classmethod
    def schema(cls):
        #more here http://json-schema.org/
        #and  https://falcon.readthedocs.io/en/stable/api/media.html#media
        # #http://json-schema.org/example1.html
        #return schema for the specific model
        json_schema={"description":cls.schema_description,"title":cls.schema_title,"type":"object"}
        json_schema.update({"properties":cls.schema_properties,"required":[k for k,v in cls.schema_properties.items() if  v.get('required_field')]})
        
        return json_schema

    def all(self):
        #return all objects
        self.sql='SELECT * FROM %s'%(self.db_table)
        return self

  
    def get(self):
        #run query and retrieve results
        print (self.sql)
        return self.db.fetch(sql=self.sql,many=True)

    def filter(self,f_string):
        """ with custom filter string from user """

        self.sql='SELECT * FROM %s WHERE '%(self.db_table)
        self.sql+=" %s "%(f_string)
        return self

    def raw(self,sql):
        self.sql=sql
        return self

    def count(self):
        count_sql="SELECT count(*) "+self.sql[self.sql.upper().find('FROM'):]
        return self.db.fetch(sql=count_sql,many=False)

    def create(self,data,ignore=False):
        #insert into db
        keys=''
        values=''
        for k,v in data.items():
            v=self.normalize_variable(v)
            values+='%s,'%(v)
            keys+='%s,'%(k)
        if ignore:
            #we ignore inserting if duplicate key exists
            self.sql="INSERT IGNORE INTO %s (%s) VALUES (%s) "%(self.db_table,keys[:-1],values[:-1])
        else:
            self.sql="INSERT INTO %s (%s) VALUES (%s) "%(self.db_table,keys[:-1],values[:-1])
        

        insert_id=self.db.save(sql=self.sql)
        if insert_id:
            data.update({self.pk:insert_id})
        return data


    def update(self,pk,data):
        sql='UPDATE %s  SET '%(self.db_table)

        for k,v in data.items():
            v=self.normalize_variable(v)
            sql+=" %s=%s,"%(k,v)
        sql=sql[:-1]
        sql+=" WHERE %s=%s"%(self.pk,pk)
        self.sql=sql
        self.db.save(sql=self.sql)

    def delete(self,pk):
        sql='DELETE FROM %s WHERE %s=%s  '%(self.db_table,self.pk,pk)
        self.sql=sql
        self.db.save(sql=self.sql)



    def normalize_variable(self,v):
        if not isinstance(v,int):
            v="'%s'"%(str(v))
        return v


        












