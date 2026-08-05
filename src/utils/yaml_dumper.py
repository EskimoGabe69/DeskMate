import yaml
from core.constants import YAML_LOC


def yaml_dumper():
    with open(YAML_LOC, "r") as stream:
        data = yaml.safe_load(stream)
        walk_anim = data.get("walk_animation")
    return walk_anim
