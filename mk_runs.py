#! /usr/bin/env python
#
#   script generator for project="2021-S1-UM-11"
#
#

import os
import sys

project="2021-S1-UM-11"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on['J113833.13+004950.2'] = [98188, 98189, 98190, 98193, 98194, 98195, 98311, 98312, 98313, 98426, 98427]

on['J115059.63-262558.4'] = [98199, 98200, 98201, 98204, 98205, 98206 ,98431, 98432]

on['132227.28+300717.0']  = [98224, 98225, 98226, 98229, 98230, 98231, 98333, 98334]

on['J144219.65+672230.0'] = [98236, 98237, 98238, 98241, 98242, 98243, 98338, 98339]

on['J174209.16+490457.3'] = [98265, 98266, 98267, 98270, 98271, 98272, 98359, 98360, 98361, 98364, 98365, 98366, 98369, 98370]

on['J164421.60+600011.4'] = [98343, 98344, 98345, 98348, 98349, 98352, 98353, 98354]

on['J150054.67+092038.0'] = [98390, 98391, 98392, 98395, 98396, 98397, 98495, 98496]

on['J155428.27-025618.1'] = [98501, 98502, 98503, 98504, 98505, 98506, 98512, 98513, 98514]

on['J132217.52+092326.4'] = [98561, 98562, 98563, 98598, 98599, 98600, 98602, 98603, 98604]

on['J215021.40+023605.4'] = [98653, 98654, 98655]


#        common parameters per source on the first dryrun (run1, run2)
pars1 = {}
common1="admit=0 restart=1 badcb=2/1,2/4"
pars1['J113833.13+004950.2'] = ""
pars1['J115059.63-262558.4'] = ""
pars1['132227.28+300717.0']  = ""
pars1['J144219.65+672230.0'] = ""
pars1['J174209.16+490457.3'] = ""
pars1['J164421.60+600011.4'] = ""
pars1['J150054.67+092038.0'] = ""
pars1['J155428.27-025618.1'] = ""
pars1['J132217.52+092326.4'] = ""
pars1['J215021.40+023605.4'] = ""



#        common parameters per source on subsequent runs (run1a, run2a)
pars2 = {}
common2="admit=0 restart=1 srdp=1"
pars2['J113833.13+004950.2'] = ""
pars2['J115059.63-262558.4'] = ""
pars2['132227.28+300717.0']  = ""
pars2['J144219.65+672230.0'] = ""
pars2['J174209.16+490457.3'] = ""
pars2['J164421.60+600011.4'] = ""
pars2['J150054.67+092038.0'] = ""
pars2['J155428.27-025618.1'] = ""
pars2['J132217.52+092326.4'] = ""
pars2['J215021.40+023605.4'] = ""




# below here no need to change code
# ========================================================================

#        helper function for populating obsnum dependant argument
def getargs(obsnum, flags=True):
    """ search for <obsnum>.args
        and in lmtoy.flags
    """
    args = ""    
    if flags:
        f = 'lmtoy.flags'
        if os.path.exists(f):
            lines = open(f).readlines()
            for line in lines:
                if line[0] == '#': continue
                args = args + line.strip() + " "
        
    f = "%d.args" % obsnum
    if os.path.exists(f):
        lines = open(f).readlines()
        for line in lines:
            if line[0] == '#': continue
            args = args + line.strip() + " "
    return args

#        specific parameters per obsnum will be in files <obsnum>.args
pars3 = {}
for s in on.keys():
    for o1 in on[s]:
        o = abs(o1)
        pars3[o] = getargs(o)


run1  = '%s.run1'  % project
run1a = '%s.run1a' % project
run2  = '%s.run2' % project
run2a = '%s.run2a' % project

fp1 = open(run1,  "w")
fp2 = open(run1a, "w")
fp3 = open(run2,  "w")
fp4 = open(run2a, "w")

#                           single obsnum
n1 = 0
for s in on.keys():
    for o1 in on[s]:
        o = abs(o1)
        cmd1 = "SLpipeline.sh obsnum=%d _s=%s %s admit=0 restart=1 " % (o,s,pars1[s])
        cmd2 = "SLpipeline.sh obsnum=%d _s=%s %s admit=0 %s" % (o,s,pars2[s], pars3[o])
        fp1.write("%s\n" % cmd1)
        fp2.write("%s\n" % cmd2)
        n1 = n1 + 1

#                           combination obsnums
n2 = 0        
for s in on.keys():
    obsnums = ""
    n3 = 0
    for o1 in on[s]:
        o = abs(o1)
        if o1 < 0: continue
        n3 = n3 + 1
        if obsnums == "":
            obsnums = "%d" % o
        else:
            obsnums = obsnums + ",%d" % o
    print('%s[%d/%d] :' % (s,n3,len(on[s])), obsnums)
    cmd3 = "SLpipeline.sh _s=%s admit=0 restart=1 obsnums=%s" % (s, obsnums)
    cmd4 = "SLpipeline.sh _s=%s admit=1 srdp=1  obsnums=%s" % (s, obsnums)
    fp3.write("%s\n" % cmd3)
    fp4.write("%s\n" % cmd4)
    n2 = n2 + 1

print("A proper re-run of %s should be in the following order:" % project)
print(run1)
print(run2)
print(run1a)
print(run2a)
print("Where there are %d single obsnum runs, and %d combination obsnums" % (n1,n2))
