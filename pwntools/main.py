from pwn import remote

r = remote('localhost', 6023) # connect

r.recvline() # receive until new line (infinite loop when no new line so becareful!!)

r.recvline().decode() # receive and decode

r.sendline(b'a') # send bytes a
r.sendline(bytes('a', 'utf-8')) # send string a
r.sendline('a'.encode())

r.interactive() # like nc but inside python

r.close() # close connection
