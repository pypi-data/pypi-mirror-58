"""simulation.py
"""
from pathlib import Path
import toml
from fillet.core import full_config_path, sudoedit


def run(parser, args):
    args.toml = full_config_path(args.toml)
    print(args.toml)

    with sudoedit(args.toml) as path:
        d = toml.load(path)

        if args.bulkfile is not None:
            args.bulkfile = str(Path(args.bulkfile).resolve(strict=True))
            print("Adding simulation file")
            d["custom_settings"]["simulation"] = args.bulkfile
        else:
            print("Removing simulation parameter")
            d["custom_settings"].pop("simulation", None)

        with open(path, "w") as fh:
            toml.dump(d, fh)

    print("File edited.")
    print("="*60)
    print(
        "To use the updated script you need to right click any\n"
        "sequencing position in MinKNOW and select 'Reload Scripts'."
    )
