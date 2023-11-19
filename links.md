---
permalink: LINKS/
---

# links
OS related:<br>
1. [My personal notes](https://riorio805.github.io/os232/NOTES)

I do work here.


2. [Vi cheatsheet](https://www.atmos.albany.edu/daes/atmclasses/atm350/vi_cheat_sheet.pdf)

Vi commands. :thumbs:


3. [Bash cheatsheet](https://devhints.io/bash#conditionals)

Contains most of the syntax in bash, which is good enough.



---
Git related:<br>

4. [Stackoverflow: How do I clone a subdirectory only of a Git repository?](https://stackoverflow.com/questions/600079/how-do-i-clone-a-subdirectory-only-of-a-git-repository/)

Example: you want to clone only the TXT folder from https://github.com/cbkadal/os232/
```
git clone -n --depth=1 --filter=tree:0 https://github.com/cbkadal/os232/
cd os232
git sparse-checkout set --no-cone TXT
git checkout
```
or if you want to init an empty folder first<br>
(inside the empty folder)
```
git init
git remote add -f origin https://github.com/cbkadal/os232/
git sparse-checkout init
git sparse-checkout set --no-cone TXT
git pull origin master
```
Note that `git sparse-checkout` is currently experimental, and may behave unexpectedly with other git commands.


---
Etc:

5. [List of emojis supported by Github's markdown](https://gist.github.com/rxaviers/7360908)

See title. :palm_tree: