import sklearn as sk
import pandas as pd
import metaflow as mt

class test_module():
    '''
    
    '''

    def __init__(self):
        '''
        
        '''

        version = 'NA'


    def get_version(self):
        '''
        
        :return: 
        '''

        version = sk.__version__,pd.__version__,mt.__version__

        return version

if __name__ == '__main__':

     tm = test_module()
     print(tm.get_version())