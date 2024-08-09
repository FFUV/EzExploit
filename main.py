import os
import colorama
import sys
import socket
import mcstatus
import requests
import json
import urllib.request, urllib.error, urllib.parse, urllib
import time
import webbrowser

from colorama import *
from mcstatus import *

init()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(0.2)

dedis = ["jouer","proxy","play","server","mc","dedi","bedwars","skywars","skyblock","creative","join","jogar","onya","buildteam","build","staff","dev","developer","serv11", "serv0", "serv10", "serv9", "serv8", "serv7", "serv6", "serv5", "serv4", "serv3", "serv2", "serv1", "serv",]
subdomains = ["www", "serieyt", "shop", "report", "apply", "youtube", "twitter", "st", "lost", "sg", "srvc1", "torneo", "serv11", "serv0", "serv10", "serv9", "serv8", "serv7", "serv6", "serv5", "serv4", "serv3", "serv2", "serv1", "serv", "mcp", "paysafe", "mu", "radio", "donate", "vps03", "vps02", "vps01", "xenon", "radio", "bans", "ns2", "ns1", "donar", "radio", "new", "appeals", "reports", "translations", "marketing", "staff", "bugs", "help", "render", "foro", "ts3", "git", "analytics", "coins", "votos", "docker-main", "main", "server3", "cdn", "server2", "creativo", "yt2", "yt", "factions", "solder", "test1", "test001", "testpene", "test", "panel", "apolo", "sv3", "sv2", "sv1", "backups", "zeus", "thor", "vps", "build", "web", "dev", "staff", "mc", "play", "sys", "node1", "node2", "node3", "node4", "node5", "node6", "node7", "node8", "node9", "node10", "node11", "node12", "node13", "node14", "node15", "node16", "node17", "node18", "node19", "node20", "node001", "node002", "node01", "node02", "node003", "sys001", "sys002", "go", "admin", "eggwars", "bedwars", "lobby1", "hub", "builder", "developer", "test", "test1", "forum", "baneos", "ts", "ts3", "sys1", "sys2", "mods", "bungee", "bungeecord", "array", "spawn", "server", "help", "client", "api", "smtp", "s1", "s2", "s3", "s4", "server1", "server2", "jugar", "login", "mysql", "phpmyadmin", "demo", "na", "eu", "us", "es", "fr", "it", "ru", "support", "developing", "discord", "backup", "buy", "buycraft", "go", "dedicado1", "dedi", "dedi1", "dedi2", "dedi3", "minecraft", "prueba", "pruebas", "ping", "register", "cdn", "stats", "store", "serie", "buildteam", "info", "host", "jogar", "proxy", "vps", "ovh", "partner", "partners", "appeals", "appeal", "store-assets", "builds", "testing", "server", "pvp", "skywars", "survival", "skyblock", "lobby", "hg", "games", "sys001", "sys002", "games001", "games002", "game001", "game002", "game003", "sys001", "us72", "us1", "us2", "us3", "us4", "us5", "goliathdev", "staticassets", "rewards", "rpsrv", "ftp", "ssh", "web", "jobs", "render", "hcf", "grafana", "vote2", "file", "sentry", "enjin", "webserver", "xen", "mco", "monitor", "servidor2", "sadre", "gamehitodrh"]

def pause():
	pause = input (" Press - Enter - to continue...")

class SConnect:
	def __init__(self, ip, port=None):
		self.ip = ip
		self.port = port
		self.address = (self.ip, self.port)
		self.s_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s_connection.settimeout(0.3)
	def portscan(self):
		return self.s_connection.connect_ex(self.address)

while True:
	os.system("cls")
	print (Fore.WHITE+Style.NORMAL+"-" * 110)
	print ()
	print(Fore.RED+'''
    ▓█████ ▒██   ██▒ ██▓███   ██▓     ▒█████   ██▓▄▄▄█████▓    ▄████▄   ██░ ██ ▓█████  ▄████▄   ██ ▄█▀
    ▓█   ▀ ▒▒ █ █ ▒░▓██░  ██▒▓██▒    ▒██▒  ██▒▓██▒▓  ██▒ ▓▒   ▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▒██▀ ▀█   ██▄█▒ 
    ▒███   ░░  █   ░▓██░ ██▓▒▒██░    ▒██░  ██▒▒██▒▒ ▓██░ ▒░   ▒▓█    ▄ ▒██▀▀██░▒███   ▒▓█    ▄ ▓███▄░ 
    ▒▓█  ▄  ░ █ █ ▒ ▒██▄█▓▒ ▒▒██░    ▒██   ██░░██░░ ▓██▓ ░    ▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒▓▓▄ ▄██▒▓██ █▄ 
    ░▒████▒▒██▒ ▒██▒▒██▒ ░  ░░██████▒░ ████▓▒░░██░  ▒██▒ ░    ▒ ▓███▀ ░░▓█▒░██▓░▒████▒▒ ▓███▀ ░▒██▒ █▄
    ░░ ▒░ ░▒▒ ░ ░▓ ░▒▓▒░ ░  ░░ ▒░▓  ░░ ▒░▒░▒░ ░▓    ▒ ░░      ░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ░▒ ▒  ░▒ ▒▒ ▓▒
     ░ ░  ░░░   ░▒ ░░▒ ░     ░ ░ ▒  ░  ░ ▒ ▒░  ▒ ░    ░         ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░  ▒   ░ ░▒ ▒░
       ░    ░    ░  ░░         ░ ░   ░ ░ ░ ▒   ▒ ░  ░         ░         ░  ░░ ░   ░   ░        ░ ░░ ░ 
       ░  ░ ░    ░               ░  ░    ░ ░   ░              ░ ░       ░  ░  ░   ░  ░░ ░      ░  ░   
                                                              ░                       ░               ''')
	print ()
	print (Fore.WHITE+"-" * 110)
	print ()
	print (Fore.MAGENTA + " (Exploit Check v6.9)")
	print ()
	print (Fore.GREEN + " (0) EXIT")
	print (Fore.CYAN + " (1) Griefing HELP")
	print (Fore.RED + " (2) IP Lookup")
	print (Fore.YELLOW + " (3) Grief & Crash Clients")
	print (Fore.BLUE + " (4) Server Lookup")
	print (Fore.WHITE + " (5) BungeeCord")
	print (Fore.MAGENTA + " (6) Plugin Exploit")
	print ()
	print (Fore.GREEN+" Choice: "+Fore.WHITE, end='')
	x = input()

	if x == "0":
		sys.exit(1)

	# GRIEFING HELP
	elif x == "1":
		os.system("cls")
		print (Fore.RED+'''
		╔═════════════════════════════════════════════════════════════════════════════╗
		║    █▀▀█  █▀▀█ ▀█▀  █▀▀▀  █▀▀▀ ▀█▀  █▄  █  █▀▀█     █  █  █▀▀▀  █     █▀▀█   ║
		║    █ ▄▄  █▄▄▀  █   █▀▀▀  █▀▀▀  █   █ █ █  █ ▄▄     █▀▀█  █▀▀▀  █     █▄▄█   ║
		║    █▄▄█  █  █ ▄█▄  █▄▄▄  █    ▄█▄  █  ▀█  █▄▄█     █  █  █▄▄▄  █▄▄█  █      ║
		╚═════════════════════════════════════════════════════════════════════════════╝
    	''')
		print(Fore.MAGENTA+" (0) EXIT")
		print(Fore.MAGENTA+" (1) GROUPMANAGER")
		print(Fore.MAGENTA+" (2) ULTRAPERMISSION")
		print(Fore.MAGENTA+" (3) ZPERMISSIONS")
		print(Fore.MAGENTA+" (4) POWERFULPERMS")
		print(Fore.MAGENTA+" (5) LUCKPERMS")
		print(Fore.MAGENTA+" (6) PERMISSIONSEX")
		print(Fore.MAGENTA+" (7) NETWORKMANAGER")
		print (Fore.MAGENTA+" Choice: "+Fore.WHITE, end='')
		gh = input()

		if gh == "0":
			print (Fore.RED+"Exiting...")
			time.sleep (3)

		elif gh == "1":
			os.system("cls")
			print(Fore.MAGENTA+'''
			╔═════════════════════════════════╗
			║  ======= GROUPMANAGER =======   ║
			║  /manuadd <player> <rank>       ║
			║  /manudel <player>              ║
			║  /manwhois <player>             ║
			╚═════════════════════════════════╝
			''')
			pause()

		elif gh == "2":
			os.system("cls")
			print(Fore.MAGENTA+'''
			╔═════════════════════════════════════════════╗
			║      ======= ULTRAPERMISSIONS =======       ║
			║       /upc addgroup <player> <rank>         ║
			║   /upc addplayerpermission <player> <rank>  ║
			║        /upc addSuperadmin <player>          ║
			║               /uperms (Menu)                ║
			╚═════════════════════════════════════════════╝
			''')
			pause()

		elif gh == "3":
			os.system("cls")
			print(Fore.MAGENTA+'''
			╔══════════════════════════════════════════════════╗
			║           ======= zPermissions ========          ║
			║                   /permissions                   ║
			║                      /perm                       ║
			║                      /perms                      ║
			║                   /zpermissions                  ║
			║                      /zperm                      ║
			║                      /zperms                     ║
			║                     /setrank                     ║
			║                    /zsetrank                     ║
			║                     /promote                     ║
			║                      /rankup                     ║
			║                     /zpromote                    ║
			║       /zpermissions player <player> set *        ║
			║  /zpermissions player <player> setgroup <group>  ║
			║              /setrank <player> <rank>            ║
			║                   /promote player                ║
			╚══════════════════════════════════════════════════╝
			''')
			pause()

		elif gh == "4":
			os.system("cls")
			print(Fore.MAGENTA+'''
			╔══════════════════════════════════════════════════╗
			║            ======= PowerFulPerms ========        ║
			║                    /powerfulperms                ║
			║                        /pp                       ║
			║                        /pop                      ║
			║                        /pow                      ║
			║         /pp user <player> add <permission>       ║
			║         /pp user <player> setgroup <rank>        ║
			╚══════════════════════════════════════════════════╝
			''')
			pause()

		elif gh == "5":
			os.system("cls")
			print(Fore.MAGENTA+'''
			╔═════════════════════════════════════════════════════════════════════════════╗
			║                         ======= LUCKPERMS ========                          ║
			║                                 /luckperms                                  ║
			║                                    /lp                                      ║
			║                                   /perm                                     ║
			║                                  /perms                                     ║
			║                                 /permission                                 ║
			║                                /permissions                                 ║
			║          /execute <player> 0 0 0 lp user <player> permission set *          ║
			║     /minecraft:execute <player> 0 0 0 lp user <player> permission set *     ║
			╚═════════════════════════════════════════════════════════════════════════════╝
			''')
			pause()

		elif gh == "6":
			os.system("cls")
			print(Fore.MAGENTA+'''
			╔═══════════════════════════════════════════════════════════════════╗
			║                    ====== PERMISSIONSEX ======                    ║
			║                                /pex                               ║
			║                           /permissionsex                          ║
			║                         /permissionsex:pex                        ║
			║                    /permissionsex:permissionsex                   ║
			║           /execute <player> 0 0 0 pex user <player> add *         ║
			║     /minecraft:execute <player> 0 0 0 pex user <player> add *     ║
			╚═══════════════════════════════════════════════════════════════════╝
			''')
			pause()

		elif gh == "7":
			os.system("cls")
			print(Fore.MAGENTA+'''
			╔════════════════════════════════════════╗
			║       ===== NETWORKMANAGER ====        ║
			║               /nmperms                 ║
			║         /networkmanagerperms           ║
			║       /networkmanagerpermissions       ║
			╚════════════════════════════════════════╝
			''')
			pause()

	# SERVER LOOKUP
	elif x == "2":
		os.system("cls")
		print ()
		print (Fore.GREEN+" IP:" +Fore.WHITE, end='')
		mcip = input()
		url = "http://ip-api.com/json/"
		response = urllib.request.urlopen(url + mcip)
		data = response.read()
		values = json.loads(data)

		try:
			print(Fore.RED+"----------------------------------------------")
			print((Fore.RED+" IP           :  "+Fore.MAGENTA + values['query']))
			print((Fore.RED+" City         :  "+Fore.MAGENTA + values['city']))
			print((Fore.RED+" Region       :  "+Fore.MAGENTA + values['regionName']))
			print((Fore.RED+" Country      :  "+Fore.MAGENTA + values['country']))
			print((Fore.RED+" Time Zone    :  "+Fore.MAGENTA + values['timezone']))
			print((Fore.RED+" ZIP          :  "+Fore.MAGENTA + values['zip']))
			print((Fore.RED+" Organisation :  "+Fore.MAGENTA + values['as']))
			print((Fore.RED+" ISP          :  "+Fore.MAGENTA + values['isp']))
			print(Fore.RED+"----------------------------------------------")
		except:
			print(Fore.RED+"----------------------------------------------")
			pass
		pause()

	# CRASH CLIENT
	elif x == "3":
		print ()
		os.system("cls")
		print(Fore.RED+'''
╔═════════════════════════════════════════════════════════════════════════════╗				
║   █▀▀█  █▀▀█ ▀█▀  █▀▀▀  █▀▀▀     █▀▀█  █    ▀█▀  █▀▀▀  █▄  █ ▀▀█▀▀  █▀▀▀█   ║
║   █ ▄▄  █▄▄▀  █   █▀▀▀  █▀▀▀     █     █     █   █▀▀▀  █ █ █   █    ▀▀▀▄▄   ║
║   █▄▄█  █  █ ▄█▄  █▄▄▄  █        █▄▄█  █▄▄█ ▄█▄  █▄▄▄  █  ▀█   █    █▄▄▄█   ║
╚═════════════════════════════════════════════════════════════════════════════╝
	''')

		print(Fore.MAGENTA+" (0) EXIT")
		print(Fore.MAGENTA+" (1) Neon Client v6.9")


		print (Fore.GREEN+" CLIENT: " +Fore.WHITE, end='')
		client = input()
		print ()

		#EXIT
		if client == "0":
			print (Fore.RED+"Exiting...")
			time.sleep (3)

		#Curium Crash Client v6.9
		if client == "1":
			print ()
			print (Fore.RED+"Downloading NeonClient v6.9...")
			time.sleep (3)
			webbrowser.open_new_tab("https://www.mediafire.com/file/z9k0rrizwnd8k8r/Neon.rar/file")
			print (Fore.MAGENTA+"This client is 100% clean!")
			pause()

	# SERVER LOOKUP
	elif x == "4":
		os.system("cls")
		print ()
		print (Fore.GREEN+" Server:" +Fore.WHITE, end='')
		mcip2 = input()
		url2 = "https://api.mcsrvstat.us/2/"
		response2 = urllib.request.urlopen(url2 + mcip2)
		data = response2.read()
		mcinfo = json.loads(data)
		try:
			print(Fore.RED+"----------------------------------------------")
			print(Fore.RED+"     IP:")
			print(mcinfo['ip'])
			print("----------------------")
			print(Fore.RED+"PORT:")
			print(mcinfo['port'])
			print("----------------------")
			print(Fore.RED+" VERSION:")
			print(mcinfo['version'])
			print("----------------------")
			print(Fore.RED+"PROTOCOL:")
			print(mcinfo['protocol'])
			print("----------------------")
			print(Fore.RED+" SOFTWARE:")
			print(mcinfo['software'])
			print(Fore.RED+"----------------------------------------------")
		except: KeyError
		pass
		print(Fore.RED+"----------------------------------------------")
		pause()

	elif x == "5":
		os.system("cls")
		print ()
		print(Fore.YELLOW+'''
		╔═══════════════════════════════════════════════════════════════════════════════╗
		║                         ======= BUNGEECORD ========                           ║
		║                                 1. Method                                     ║
		║                             Join on nick: md_5                                ║
		║                    Once you join you should have perms                        ║
		║                         try: /send /alert /server                             ║
		║                                 2. Method                                     ║
		║                                 UUID SPOOF                                    ║
		║                                 3. Method                                     ║
		║                                Port Checking                                  ║
		║ Only working if the bungeecord and the other servers are on the same machine! ║
		╚═══════════════════════════════════════════════════════════════════════════════╝''')
		pause()


	elif x == "6":
		os.system("cls")
		print ()
		print(Fore.GREEN+'''
		╔═══════════════════════════════════════════════════════════════════════════════╗
		║                         ======= PLUGIN EXPLOIT ========                       ║
		║                                 1. Method                                     ║
		║           Just try /pl if they are not using plugin to stop that              ║
		║                                 2. Method                                     ║
		║          Use JigsawClient and go to option exploits and PluginSteal           ║
		║                                 3. Method                                     ║
		║                  Use SkillClient and go to plugin exploit                     ║
		║                                 4. Method                                     ║
		║                              / pl [space] [tab]                               ║
		║                                / bukkit: help                                 ║
		║                                / bukkit: see                                  ║
		║                                 / bukkit :?                                   ║
		║                              / see [space] [tab]                              ║
		║                               or write / [tab]                                ║
		╚═══════════════════════════════════════════════════════════════════════════════╝''')
		pause()
