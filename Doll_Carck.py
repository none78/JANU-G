import os, platform
try:
    import requests
except:
    os.system('pip2 install requests')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from Doll import main1
    main1()
elif bit == '32bit':
    from Doll import main1
    main1()