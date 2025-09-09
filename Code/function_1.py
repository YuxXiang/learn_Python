

from typing import TYPE_CHECKING


def sort_num(a,b):
    ln_1 = a
    ln_2 = b
    if ln_1 > ln_2:
        ln_2 = a
        ln_1 = b
    
    print(str(ln_1)+','+str(ln_2))

    

sort_num(17,15)
