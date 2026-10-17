# modular patchbook

## Requirements
- python 3
- [spektroaudio patchbook](https://github.com/spektroaudio/patchbook)
- [graphviz](https://graphviz.org/)

## Install
- install requirements
- put spektroaudios patchbook.py file in patchbook_parser

- the content of output directory is ignored by git. Change it if you want to track it. But it will be generated anyway.

## Usage
### Create a patch
- create a new directory in the ./patches directory
- use the SemVer convention for trackig changes your files

### Build
- run `python3 build.py`
- That's all, folks

## Git hook
When committing a pre-commit hook is run, compiling all changes automagically. 

You can skip that with the `--no-verify` flag.
But since you read the git documentation, this is nothing new to you.
