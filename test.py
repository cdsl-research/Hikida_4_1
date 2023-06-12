import base64
from random import randint
account = [base64.b64encode(('%s:%s' % ('user', 'password')).encode()).decode(), 
           base64.b64encode(('%s:%s' % ('user1', 'password')).encode()).decode(), 
           base64.b64encode(('%s:%s' % ('user3', 'password')).encode()).decode()]

print(randint(0, 2))

print(account[randint(0,2)])