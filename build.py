#!/usr/bin/env python3
import os
import jinja2

template_filename = "./templates/base.html.j2"
rendered_filename = "dist/index.html"
render_vars = {
  "greeting": "Oh hi!"
}

os.mkdir('dist')

script_path = os.path.dirname(os.path.abspath(__file__))
template_file_path = os.path.join(script_path, template_filename)
rendered_file_path = os.path.join(script_path, rendered_filename)

environment = jinja2.Environment(loader=jinja2.FileSystemLoader(script_path))
output_text = environment.get_template(template_filename).render(render_vars)

with open(rendered_file_path, "w") as result_file:
  result_file.write(output_text)
