import requests , bs4 , re , sys

if len(sys.argv) < 2:
	print('USAGE : Python scrap.py file-contains-ursl.txt output-file.txt')
	exit()

class Scrap:
	def __init__(self , url):
		self.url = url
		self.text = ''
		self.emails = []

	def get(self):
		res = requests.get(self.url)
		self.text = res.text

	def extract(self):
		emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", self.text)
		self.emails = emails

	def save(self):
		for email in self.emails:
			with open(sys.argv[2] , 'a') as f:
				f.write(email + '\n')



with open(sys.argv[1]) as f:
	lista = f.read().split('\n')

print(f'[!] running on {sys.argv[1]}')

for url in lista:
	print(f'[+] Crawling: {url}')
	scrap = Scrap(url)
	scrap.get()
	scrap.extract()
	scrap.save()
	print(f'[!] {len(scrap.emails)} Emails found : {scrap.emails}')

print(f'[X] SAVED IN : {sys.argv[2]}')


