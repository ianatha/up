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

```bash
$ pwd
/Users/jdoe/Developer/backend/src/main/java/com/example/service/db/
$ up example
$ pwd
/Users/jdoe/Developer/backend/src/main/java/com/example/
$ up 4
$ pwd
/Users/jdoe/Developer/backend/src/
$ cd -
$ pwd
/Users/jdoe/Developer/backend/src/main/java/com/example/
$ up
 0. example
 1. com
 2. java
 3. main
 4. src
 5. backend
 6. Developer
 7. jdoe
 8. Users
? 4
$ pwd
/Users/jdoe/Developer/backend/src/
$ up ~
$ pwd
/Users/jdoe/
```