#CONFIG PARSER (Parsing info (id, passw.) from configuration file, e.g. .ini and
#export data to a new files
import configparser

config = configparser.ConfigParser()
config.read('mess.ini')


prod_config = {}
dev_config = {}


for s in config.sections():
    tmp = {}
    for i in config[s]:
        tmp.update({i:config[s][i]}) 
    if tmp['env'] == 'prod':
        tmp.pop('env')
        prod_config.update({s:tmp})
    else:
        tmp.pop('env')
        dev_config.update({s:tmp})

#----------------------
#Create and check the first file (prod)
config = configparser.ConfigParser()
config.read_dict(prod_config)
with open('prod_config.ini', mode = 'w') as p_c:
    config.write(p_c)

print('--Production')
config.read('prod_config.ini')
for s in config.sections():
    print("["+s+"]")
    for i in config[s]:
        print(i,":",config[s][i])
        
print()

#Create and check second file (prod)
config = configparser.ConfigParser()
config.read_dict(dev_config)

with open('dev_config.ini','w') as d_c:
    config.write(d_c)

print('--Development')    
config.read('dev_config.ini')
for s in config.sections():
    print("["+s+"]")
    for i in config[s]:
        print(i,":",config[s][i])
