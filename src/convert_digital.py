factors = {'PB': 1000000000000000, 'TB': 1000000000000, 'GB': 1000000000, 'MB' : 1000000, 'kB' : 1000, 'bit' : 8, 'byte' : 1}

def convert(amt, frm, to):
        if frm != 'byte':
            amt = amt * factors[frm]
            return amt / factors[to]
        else:
            return amt / factors[to]