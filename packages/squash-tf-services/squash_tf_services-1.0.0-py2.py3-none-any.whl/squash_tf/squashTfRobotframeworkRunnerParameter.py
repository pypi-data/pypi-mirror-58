#
#     This file is part of the Squashtest platform.
#     Copyright (C) 2019 - 2019 Henix
#
#     See the NOTICE file distributed with this work for additional
#     information regarding copyright ownership.
#
#     This is free software: you can redistribute it and/or modify
#     it under the terms of the GNU Lesser General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     this software is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU Lesser General Public License for more details.
#
#     You should have received a copy of the GNU Lesser General Public License
#     along with this software.  If not, see <http://www.gnu.org/licenses />.
#

class TFParamService(object):
    """Library to get TM test parameters in robotframework code"""

    __data=None
    
    def __init__(self):
        """ noop _ for now """
        def printNoneOrStr(message,toPrint):
            if toPrint==None:
                print(message+" <None>")
            else:
                print(message+" "+str(toPrint))
        if not TFParamService.__data.has_section("global"):
            TFParamService.__data.add_section("global")
        
        if not TFParamService.__data.has_section("test"):
            TFParamService.__data.add_section("test")
        
        printNoneOrStr("TFParamService.global=",TFParamService.__data.items("global"))
        printNoneOrStr("TFParamService.test=",TFParamService.__data.items("test"))

    def getTestParam(self,key,defaultValue=None):
        """ Returns the test case parameter value if it is defined, None otherwise"""
        if TFParamService.__data.has_option("test",key):
            return TFParamService.__data.get("test",key)
        else:
            return defaultValue

    def getGlobalParam(self,key,defaultValue=None):
        """ Returns the global parameter value if it is defined, None otherwise"""
        if TFParamService.__data.has_option("global",key):
            return TFParamService.__data.get("global",key)
        else:
            return defaultValue


    def getParam(self,key,defaultValue=None):
       """ Returns the test case parameter if defined, else the global parameter if defined, None otherwise"""
       return self.getTestParam(key,self.getGlobalParam(key,defaultValue))

import os
import sys
if sys.version_info.major >= 3:
    print("Python 3")
    import configparser
    TFParamService._TFParamService__data=configparser.ConfigParser()
    def cfgOpen(path):
        print("Using python3 open with explicit encoding.")
        return open(path,encoding='utf-8')
else:
    print("Python 2")
    import ConfigParser
    TFParamService._TFParamService__data=ConfigParser.ConfigParser()
    def cfgOpen(path):
        print("Using python2 open with default platform encoding.")
        return open(path)

if "_SQUASH_TF_TESTCASE_PARAM_FILES" in os.environ:
    path=os.environ["_SQUASH_TF_TESTCASE_PARAM_FILES"]
    print("Loading data from path:"+path)
    # This is important to get a case-sensitive mapping
    TFParamService._TFParamService__data.optionxform=str
    TFParamService._TFParamService__data.readfp(cfgOpen(path))
else:
    print("No test case data pointer, falling back on default values")

if __name__ == "__main__":
    """ This main is here for TESTING purpose"""
    print("Hello World")
    tf_param_service=TFParamService()
    def printNoneOrStr(message,toPrint):
        if toPrint==None:
            print(message+" <None>")
        else:
            print(message+" "+toPrint)
    
    printNoneOrStr("Test parameter 'TC1', no default",tf_param_service.getTestParam('TC1'))
    printNoneOrStr("Test parameter 'TC2', no default",tf_param_service.getTestParam('TC2'))
    printNoneOrStr("Test parameter 'TC1', default=test_TC1",tf_param_service.getTestParam('TC1','test_TC1'))
    printNoneOrStr("Test parameter 'TC2', default=test_TC2",tf_param_service.getTestParam('TC2','test_TC2'))
    
    printNoneOrStr("Global parameter 'TC1', no default",tf_param_service.getGlobalParam("TC1"))
    printNoneOrStr("Global parameter 'TC2', no default",tf_param_service.getGlobalParam("TC2"))
    printNoneOrStr("Global parameter 'TC1', default=global_TC1",tf_param_service.getGlobalParam("TC1","global_TC1"))
    printNoneOrStr("Global parameter 'TC2', default=global_TC2",tf_param_service.getGlobalParam("TC2","global_TC2"))
    
    printNoneOrStr("Test or Global parameter 'TC1', no default",tf_param_service.getParam("TC1"))
    printNoneOrStr("Test or Global parameter 'TC2', no default",tf_param_service.getParam("TC2"))
    printNoneOrStr("Test or Global parameter 'TC3', no default",tf_param_service.getParam("TC3"))
    printNoneOrStr("Test or Global parameter 'TC4', no default",tf_param_service.getParam("TC4"))
    printNoneOrStr("Test or Global parameter 'TC1', default=test_or_global_TC1",tf_param_service.getParam("TC1","test_or_global_TC1"))
    printNoneOrStr("Test or Global parameter 'TC2', default=test_or_global_TC2",tf_param_service.getParam("TC2","test_or_global_TC2"))
    printNoneOrStr("Test or Global parameter 'TC3', default=test_or_global_TC3",tf_param_service.getParam("TC3","test_or_global_TC3"))
    printNoneOrStr("Test or Global parameter 'TC4', default=test_or_global_TC4",tf_param_service.getParam("TC4","test_or_global_TC4"))
    
