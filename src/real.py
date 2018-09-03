'''
    description: python real.py 20180830
'''
import sys

import main

#sys.stderr = open("../data/logs/log_err.txt","w")
#sys.stdout = open("../data/logs/log_out.txt","w")

DEBUG = True

if DEBUG:
    main.main()
else:
    try:
        main.main()
        sys.exit(0)
    except Exception as err:
        print('Error: %s' % err, file=sys.stderr)
    sys.exit(1)
