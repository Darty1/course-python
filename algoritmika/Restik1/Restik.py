from Rest_classes import *
from Rest_func import *




p = -1
while p != 0:
    p = int(input("""
                     1 - Host
                     2 - Client
                     0 - Exit
                     
                        """))
    if p == 1:
        run_host_interface()
    elif p == 2:
        run_client_interface()
    else:
        print("Bad, input again!")
