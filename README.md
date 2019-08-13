# up
Tiny utility to move up-and-down complex folder structures in CLI

## Manual Installation

Copy https://raw.githubusercontent.com/ianatha/up/master/up.py to a location of your choice.

Add
```
up () { cd `/Users/jdoe/Downloads/up.py $1` }
```
to your `~/.zshrc` or `~/.bashrc`.

## Example Usage

```
$ pwd
/Users/jdoe/Developer/backend/src/main/java/com/example/service/db/
$ up example
$ pwd
/Users/jdoe/Developer/backend/src/main/java/com/example/
$ up 4
$ pwd
/Users/jdoe/Developer/backend/src/
```