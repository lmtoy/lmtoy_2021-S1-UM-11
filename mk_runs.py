#! /usr/bin/env python
#
#   script generator for project="2021-S1-UM-11"
#

import os
import sys

from lmtoy import runs
    
project="2021-S1-UM-11"

#        obsnums per source (make it negative if not added to the final combination)
#  initial test cases are J113833 and J132227 (where the J was accidentally dropped from the name)
on = {}
on['J113833.13+004950.2'] = [98188, 98189, 98190, 98193, 98194, 98195,-98311,-98312,-98313, 98426, 98427,
                             99974,99975,99976]

on['J115059.63-262558.4'] = [98199, 98200, 98201, 98204, 98205, 98206 ,98431, 98432,
                             99951,99952,99953,99955,99956,99957,99959,99960]

on['132227.28+300717.0']  = [98224, 98225, 98226, 98229, 98230, 98231, 98333, 98334,
                             100313, 100314, 100315, 100317, 100318, 100319, 100321, 100322, 100323]    # 25-may

on['J144219.65+672230.0'] = [98236, 98237, 98238, 98241, 98242, 98243, 98338, 98339]

on['J174209.16+490457.3'] = [-98265,-98266,-98267,-98270,-98271,-98272, 98359, 98360, 98361, 98364, 98365, 98366, 98369, 98370,
                             100084, 100085, 100086, 100088, 100089, 100090, 100092, 100093]

on['J164421.60+600011.4'] = [98343, 98344, 98345, 98348, 98349, 98352, 98353, 98354]

on['J150054.67+092038.0'] = [98390, 98391, 98392, 98395, 98396,-98397, 98495, 98496,
                             100327, 100328, 100329, 100331, 100332, 100333]              # 25-may

on['J155428.27-025618.1'] = [98501, 98502, 98503, 98504, 98505, 98506, 98512, 98513, 98514]

on['J132217.52+092326.4'] = [98561, 98562, 98563, 98598, 98599, 98600, 98602, 98603, 98604]

on['J215021.40+023605.4'] = [98653, 98654, 98655]

on['J165845.46+360543.8'] = [ 100008, 100009, 100010, 100012, 100013, 100014,
                             -100075,-100076, 100077, 100079, 100080, 100081]

on['J211704.27-191850.4'] = [100018, 100019, 100020]

#        common parameters per source on the first dryrun (run1, run2)
#        1/1,3,3 are bad for all the series
#        3/5 was bad until Gopal reseated : on 5-may-2022 ?
pars1 = {}
common1="admit=0 restart=1 badcb=1/1,3/3"
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
pars1['J165845.46+360543.8'] = ""
pars1['J211704.27-191850.4'] = ""

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
pars2['J165845.46+360543.8'] = ""
pars2['J211704.27-191850.4'] = ""


if __name__ == "__main__":
    runs.mk_runs(project, on, pars1, pars2, None, sys.argv)
