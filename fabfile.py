from fabric.api import *
env.hosts=['192.168.2.116','192.168.2.140','127.0.0.1']
env.user='fabuser'
env.password='fab@123'
def deploy():
	local("ls")
def host_deploy():
	run("ls")
def uptime():
	run("uptime")
