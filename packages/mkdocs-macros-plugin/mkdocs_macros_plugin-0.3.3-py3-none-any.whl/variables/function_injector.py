

import repackage, importlib
import os

DEFAULT_MODULE_NAME = 'mkfunctions.py'

def add_functions(template, config):
    """
    Add the template functions, via the python module
    located in the same directory as the Yaml config file.

    The python module must contain the following hook:

    declare_functions(template_function):

        @template_function:
        def bar(x):
            ....

        @template_function:
        def baz(x):
            ....
    """

    def template_function(f):
        """
        Decorator function: record the template

        @template_function
        def custom_function1(a):
            return a.replace('o', 'ay')
         https://stackoverflow.com/questions/6036082/call-a-python-function-from-jinja2
        """
        md_template.globals[f.__name__] = f
        return f


    # determine the package name, from the filename:
    python_module = config.get('python_module') or DEFAULT_MODULE_NAME
    # get the directory of the yaml file:
    config_file = config['config_file_path']
    yaml_dir = os.path.dirname(config_file)
    print("Found yaml directory: %s" % yaml_dir)

    # that's the directory of the package:
    repackage.add(yaml_dir)
    try:
        module = importlib.import_module(python_module)
        print("Found module '%s'" % python_module)
        # execute the hook, passing the template decorator function
        module.declare_functions(template_function)
    except ModuleNotFoundError:
        print("No module found.")


# -------------------
# Test
# -------------------
if __name__ == '__main__':
    from jinja2 import Template

    # simulation of the environment:
    markdown = "I say: {{foo}}. This is {{ bar(5)}}"
    extra = {'foo': 'Hello world'}
    config = {'config_file_path':'./markdown.yaml',
               'extra':extra,
               'python_module': 'test'}



    # Get the environment
    extra = config.get('extra')
    md_template = Template(markdown)

    # add the functions
    add_functions(md_template, config)


    # Execute the template and return
    result = md_template.render(**extra)
    print(result)
