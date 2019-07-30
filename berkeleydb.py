import bsddb3
import time


for k, v in bsddb3.btopen("C:\Actimize\Instances\AIS_instance_cdd\data\flist_AML_EWLF_orgMatcher_exactMatchName.db","r").iteritems():
    print (k,v)