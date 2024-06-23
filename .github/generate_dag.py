import sys
from jinja2 import Environment, FileSystemLoader
import os

def generate_file(template_name, filename):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(template_name)
    
    output = template.render(filename=filename)
    
    # Create output filename by replacing extension and adding '-dag.py'
    base_filename = os.path.splitext(filename)[0]
    output_filename = f'{base_filename}-dag.py'
    
    os.makedirs('generated_files', exist_ok=True)
    with open(f'generated_files/{output_filename}', 'w') as f:
        f.write(output)
    
    return output_filename

if __name__ == "__main__":
    template_name = sys.argv[1]
    filename = sys.argv[2]
    output_filename = generate_file(template_name, filename)
    print(output_filename)
