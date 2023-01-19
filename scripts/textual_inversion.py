#!/usr/bin/env python

# Copyright 2023, Lincoln Stein @lstein
from ldm.invoke.globals import Globals, set_root
from ldm.invoke.textual_inversion_training import parse_args, do_textual_inversion_training

if __name__ == "__main__":
    args = parse_args()
    set_root(args.root_dir or Globals.root)
    kwargs = vars(args)
    do_textual_inversion_training(**kwargs)
