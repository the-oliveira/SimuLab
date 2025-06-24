from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader("template"),
    autoescape=select_autoescape()
)

template = env.get_template("src\Web\template\index.html")
print(template.render(the=''))