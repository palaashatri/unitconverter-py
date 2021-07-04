factors = {'PB': 8000000000000000, 'TB': 8000000000000, 'GB': 8000000000, 'MB' : 8000000, 'kB' : 8000, 'bit' : 1, 'byte' : 0.125}

def convert(amt, frm, to):
        if frm != 'bit':
            amt = amt * factors[frm]
            return amt / factors[to]
        else:
            return amt / factors[to]