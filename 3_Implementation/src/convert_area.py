factors = {'sqm':1,'sqkm':1000000,'sqr':1011.7141056,'sqcm':0.0001,'sqf':0.09290304 ,
                    'sqin':0.00064516, 'sqmile':2589988.110336, 'mm':0.000001,'sqrod':25.29285264,
                    'sqyard':0.83612736, 'sqtownship':93239571.9721, 'sqacre':4046.8564224 ,'sqare': 100,
                    'sqbarn':1e-28, 'sqhectare':10000, 'sqhomestead':647497.027584}


def convert(amt, frm, to):
        if frm != 'sqm':
            amt = amt * factors[frm]
            return amt / factors[to]
        else:
            return amt / factors[to]