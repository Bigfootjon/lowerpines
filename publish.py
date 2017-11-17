import os

import lowerpines

if os.popen('git tag -l ' + lowerpines.VERSION).read() == '':
    os.system('git tag -a ' + lowerpines.VERSION + ' -m "Version '+lowerpines.VERSION + '"')
    os.system('git push --tags')
    os.system('twine upload dist/*')
else:
    print('There is already a tag for version ' + lowerpines.VERSION)
    exit(1)
