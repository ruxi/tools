__author__ = "github.com/ruxi"
__copyright__ = "Copyright 2016, ruxitools"
__email__ = "ruxi.github@gmail.com"
__license__ = "MIT"
__status__ = "Development"
__version__ = "0.1"

import unittest 
import collections
from ruxitools.xydb import XyDB

class TestXydb(unittest.TestCase):
    """test if unittest works"""   
    ############
    #  set-up  #
    ############
    def dummycase(self):
        # dummy record 
        key = 'dummy0'
        desc = 'test case'
        X = [1,2,3,4]
        y = ['a','b','c','d']
        return dict(key=key, desc=desc, X=X, y=y)       
    
    def badcase_nokey(self):
        desc = 'test case'
        X = [1,2,3,4]
        return dict(desc=desc, X=X) 
 
    def badcase_KeyNotStr(self):
        key = [1,2,3,4]
        X = "x is a str"
        return dict(jey=key, X=X) 
    
    def mockschema(self):
        input_validation = collections.namedtuple("Xy", ['key','desc', 'X', 'y'])
        return input_validation
    
    def push_record_noschema(self, record):
        xy = XyDB(verbose=False)
        xy.push(**record)
        return xy
    
    def push_record_w_schema(self, record, schema):
        xy = XyDB(schema=schema, verbose=False)
        xy.push(**record)
        return xy
    
    ###########
    #  TESTS  #
    ###########
    
    def test_positive_control(self):
        self.assertTrue(True)
        
    def test_init_args(self):
        xy = XyDB()
        xy = XyDB(verbose=False)
        xy = XyDB(verbose=True)

    def test_PushRecord_NoSchema(self):
        record = self.dummycase()
        self.push_record_noschema(record)
   
    def test_PushRecord_WithSchema(self):
        record = self.dummycase()
        schema = self.mockschema()
        self.push_record_w_schema(record=record, schema=schema)
         
    def test_PushRecord_NoKey(self):
        """negative test"""
        record = self.badcase_nokey()
        with self.assertRaises(TypeError):
             self.push_record_noschema(record)
                
    def test_PushRecord_KeyNotStr(self):
        """negative test"""
        record = self.badcase_KeyNotStr()
        with self.assertRaises(TypeError):
             self.push_record_noschema(record)
                
    def test_ShowRecord(self):
        record = self.dummycase()
        xy = self.push_record_noschema(record)
        getattr(xy.show, record['key'])
                
    def test_ShowRecord_NonExistKey(self):
        """negative test"""
        record = self.dummycase()
        key = record['key'] + "spike"
        xy = self.push_record_noschema(record)
        with self.assertRaises(KeyError):
            getattr(xy.show, record[key])
            
    def test_PullRecord(self):
        record = self.dummycase()
        xy = self.push_record_noschema(record)
        getattr(xy.pull, record['key'])
                
    def test_PullRecord_NonExistKey(self):
        """negative test"""
        record = self.dummycase()
        key = record['key'] + "spike"
        xy = self.push_record_noschema(record)
        with self.assertRaises(KeyError):
            getattr(xy.pull, record[key])   
    
    def test_keys_NoRecords(self):
        """is dict_keys returned"""
        xy = XyDB()
        xy.keys
        self.assertTrue(type(xy.keys)==type({}.keys())
                        , "Expecting dict_keys, instead got {}".format(type(xy.keys))
                       )

    def test_keys_WithRecords(self):
        record = self.dummycase()
        xy = XyDB()
        xy.push(**record)
        xy.keys
        
    def test_db_IsDict(self):
        record = self.dummycase()
        xy = self.push_record_noschema(record) 
        self.assertTrue(type(xy.db)==dict)
        
    def test_otherattributes(self):
        record = self.dummycase()
        schema = self.mockschema()
        xy = self.push_record_w_schema(record, schema) 
        xy._update
if __name__ == '__main__':
    unittest.main()       