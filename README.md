# up
Tiny utility to move up deep folder structures in CLI

## Manual Installation

Copy https://raw.githubusercontent.com/ianatha/up/master/up.py to a location of your choice.

Add
```
up () { cd `/Users/jdoe/Downloads/up.py $1` }
```
to your `~/.zshrc` or `~/.bashrc`.

## Example Usage

```bash
/Users/jdoe/Developer/backend/src/main/java/com/example/service/db$ up example
/Users/jdoe/Developer/backend/src/main/java/com/example$ up 4
/Users/jdoe/Developer/backend/src$ cd -
/Users/jdoe/Developer/backend/src/main/java/com/example$ up
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
/Users/jdoe/Developer/backend/src$ up ~
/Users/jdoe$ echo I love up
I love up
```