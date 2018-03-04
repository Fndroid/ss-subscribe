import base64
import json
import re
import requests
from urllib.parse import unquote_plus, quote_plus

def print_dict(d):
	res = ''
	for key in d:
		res += '{}:{}\n'.format(key, d[key])
	return res[:-1]

def save(servers):
	ss_client_config = json.load(open('gui-config.json', 'r', encoding='utf-8'))

	# print(ss_client_config)
	configs = ss_client_config['configs']
	# print(configs)
	new_addrs = list(map(lambda x: x['server'], servers))
	configs = list(filter(lambda x: x['server'] not in new_addrs, configs))

	print('\n清除旧线路(地址与新线路相同)成功!\n')

	configs.extend(servers)
	ss_client_config['configs'] = configs
	json.dump(ss_client_config, open('gui-config.json', 'w', encoding='utf-8'), indent=2)

	print('保存成功,请重启ss客户端!')

def read_config():
	subscribe_config = json.load(open("ss-subscribe.json", 'r'))
	servers = subscribe_config.get('servers', [])
	res = []
	for s in servers:
		url = s.get('url')
		resp = requests.get(url).text
		links = base64.b64decode(resp).decode('utf-8').split('\n')
		# print(links)
		print('解析链接({})成功,此URL包含{}条ss://链接:'.format(url, len(links)))
		for l in links:
			server = {}
			tag = unquote_plus(re.findall(r'#(.*?)$', l)[0])
			server['remarks'] = '{}'.format(tag)
			server['timeout'] = 5
			if '/?' in l:
				plugin = re.findall(r'/\?(.*?)#', l)[0][7:]
				server['plugin'], server['plugin_opts'] = unquote_plus(plugin).split(';')
				password = re.findall(r'ss://(.*?)@', l)[0]
				server['method'], server['password'] = base64.b64decode(password).decode('utf-8').split(':')
				address = re.findall(r'@(.*?)/\?', l)[0]
				server['server'] = address.split(':')[0]
				server['server_port'] = int(address.split(':')[1])
				# print(server)
			else:
				address = re.findall(r'ss://(.*?)#', l)[0]
				address_c = base64.b64decode(address).decode('utf-8')
				params = re.split(':|@', address_c)
				server['method'], server['password'], server['server'] = params[:-1]
				server['server_port'] = int(params[-1])
				server['plugin'] = server['plugin_opts'] = ''
				# print(server)
			print('\n链接({})信息如下:\n{}'.format(l, print_dict(server)))
			res.append(server)
	return res


if __name__ == '__main__':
	# print(read_config())
	save(read_config())
