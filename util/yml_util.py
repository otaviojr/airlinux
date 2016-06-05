import yaml

def load_config(file):
    try:
        with open(file, 'r') as stream:
            try:
                return yaml.load(stream)
            except yaml.YAMLError as exc:
                print(exc)
                return None
    except IOError as exc:
        return None
