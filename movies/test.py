import os
print('===== sys.path / PYTHONPATH =====')
for k in sorted(os.environ.keys()):
    v = os.environ[k]
    print ('%-30s %s' % (k,v[:70]))