import yaml
import os

config_path = os.path.join(os.environ['USERPROFILE'], '.continue', 'config.yaml')

config = {
    'name': 'Local Ollama Config',
    'version': '1.0.0',
    'schema': 'v1',
    'models': [
        {
            'title': 'Local Ollama (8B)',
            'provider': 'ollama',
            'model': 'deepseek-r1:8b',
            'apiBase': 'http://localhost:11434'
        },
        {
            'title': 'Local Ollama (1.5B)',
            'provider': 'ollama',
            'model': 'deepseek-r1:1.5b',
            'apiBase': 'http://localhost:11434'
        }
    ]
}

with open(config_path, 'w') as f:
    yaml.dump(config, f, default_flow_style=False)

print(f'Updated YAML config at {config_path}')
print('Please restart VS Code for changes to take effect.')