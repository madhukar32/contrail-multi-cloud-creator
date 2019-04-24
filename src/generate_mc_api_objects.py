import yaml
import argparse
import logging
import pdb
import os

from jinja2 import Environment
from jinja2 import FileSystemLoader

def load_input_file(inputYamlFile):

    if os.path.exists(inputYamlFile):
        fh = open(inputYamlFile)
        input = yaml.safe_load(fh)
        fh.close()
        return input
    else:
        raise FileNotFoundError('path does not exist for input file {}'.format(inputYamlFile))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate contrail go API schema objects needed to deploy CEM')
    parser.add_argument('--input', help="path to the input file where config is stored",
        default="input_config.yaml", type=str)

    logging.basicConfig(level = logging.INFO,
        format = '%(asctime)s  %(levelname)-10s %(processName)s  %(name)s %(message)s')

    args = parser.parse_args()
    # load input file
    try:
        input_config_dict = load_input_file(args.input)
    except FileNotFoundError as e:
        logging.error("{}".format(e))
        sys.exit(1)


    j2_env = Environment(loader=FileSystemLoader('templates'),
        trim_blocks=True, lstrip_blocks=True)
    template = j2_env.get_template("contrail_public_cloud_tmpl.j2")
    rendered_out = template.render(input_config_dict)

    with open("cloud_out.yaml", "w") as fh:
        fh.write(rendered_out)
        fh.close()
