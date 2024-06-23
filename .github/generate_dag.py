import sys
from jinja2 import Environment, FileSystemLoader
import os

def generate_file(template_name, filename):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(template_name)
    
    output = template.render(filename=filename)
    
    os.makedirs('generated_files', exist_ok=True)
    with open(f'generated_files/{filename}.py', 'w') as f:
        f.write(output)

if __name__ == "__main__":
    template_name = sys.argv[1]
    filename = sys.argv[2]
    generate_file(template_name, filename)
