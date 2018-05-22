from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='k9zk!&a^($5+d!b+)#zt%&2v@)lrt%)lm(!ujv7s)c)p9kyzna')

DEBUG = env.bool('DJANGO_DEBUG',True)
