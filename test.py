import yaml

with open('config.yml', 'r') as ymlFile:
  config = yaml.load(ymlFile)

print(config['vesta_vars']['ip'])
