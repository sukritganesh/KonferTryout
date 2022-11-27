def dump_redbaron(red, filepath="dump.py"):
    with open(filepath, "w") as source_code:
        source_code.write(red.dumps())