# modular patchbook

## Requirements
- python 3
- [spektroaudio patchbook](https://github.com/spektroaudio/patchbook)
- [graphviz](https://graphviz.org/)

## Insatll
- install requirements
- put spektroaudios patchbook.py file in patchbook_parser

## Usage
### Create a patch
- create a new directory in the ./patches directory
- use the SemVer convention for trackig changes your files

### Build
- run `python3 build.py`
- Thats all, folks

## Git hook
When commiting a pre-commit hook is run, compiling all changes automagically.