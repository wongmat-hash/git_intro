def contrived_func(val):
    if val < 150 and val > 100:                                                 # x< 150 && x > 100
        return True
    elif val * 5 < 361 and val / 2 < 24:                                        # x * 5 < 361 && x /2 < 24
        if val == 6:                                                            # x == 6
            return False
        else:
            return True
    #"elif (val > 75 or val / 8 < 10) and val**val % 5 == 0:"        
    elif (val > 75 or val / 8 < 10) and val**val % 5 == 0:                      # (x > 75 || x / 8 < 10) && x**x % 5 == 0
        return True
    else:
        return False


------

import uniitest
