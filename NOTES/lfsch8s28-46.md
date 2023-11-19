Congratulations!!!!\
Hope you had a good night's sleep\
There is still a lot more packages to go\
gogogogogogogo\
:computer::no_entry_sign::clock5:


## 8.0 Chapter 8 Setup

## 8.0.S Entering chroot environment
#### Run as `root`
Set `$LFS` variable
```bash
export LFS=/mnt/lfs
```
Check `$LFS` variable (make sure OK)
```bash
echo "===== ======="
echo "Check $LFS..."
if   [ -z $LFS  ] ; then 
  echo ERROR: There is no LFS variable  === ERROR ===
elif [ -d $LFS/ ] ; then
  echo === === === === === === ===  LFS is $LFS/ === OK ===
else
  echo ERROR: There is no LFS directory === ERROR ===
fi
```
Mount virtual file systems and enter chroot environment
```bash
mkdir -pv $LFS/{dev,proc,sys,run}

mount -v --bind /dev $LFS/dev
mount -v --bind /dev/pts $LFS/dev/pts
mount -vt proc proc $LFS/proc
mount -vt sysfs sysfs $LFS/sys
mount -vt tmpfs tmpfs $LFS/run

if [ -h $LFS/dev/shm ]; then
  mkdir -pv $LFS/$(readlink $LFS/dev/shm)
else
  mount -t tmpfs -o nosuid,nodev tmpfs $LFS/dev/shm
fi

chroot "$LFS" /usr/bin/env -i   \
    HOME=/root                  \
    TERM="$TERM"                \
    PS1='(lfs chroot) \u:\w\$ ' \
    PATH=/usr/bin:/usr/sbin     \
    /bin/bash --login
```

## 8.0.E Exiting chroot environment
When you want to exit just do this
```bash
exit
```

## 8.0.X Pre-flight Checks
Make sure you are in
`(lfs chroot) root:/sources# |`



---
## 8.28 Pkgconf install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf pkgconf-*.tar.*
cd pkgconf-*/

# Installation here

}

cd /sources/
rm -rf pkgconf-*/
```

---
## 8.29 Ncurses install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf ncurses-*.tar.*
cd ncurses-*/

# Installation here

}

cd /sources/
rm -rf ncurses-*/
```

---
## 8.30 Sed install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf sed-*.tar.*
cd sed-*/

# Installation here

}

cd /sources/
rm -rf sed-*/
```

---
## 8.31 Psmisc install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf psmisc-*.tar.*
cd psmisc-*/

# Installation here

}

cd /sources/
rm -rf psmisc-*/
```

---
## 8.32 Gettext install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf gettext-*.tar.*
cd gettext-*/

# Installation here

}

cd /sources/
rm -rf gettext-*/
```

---
## 8.33 Bison install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf bison-*.tar.*
cd bison-*/

# Installation here

}

cd /sources/
rm -rf bison-*/
```

---
## 8.34 Grep install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf grep-*.tar.*
cd grep-*/

# Installation here

}

cd /sources/
rm -rf grep-*/
```

---
## 8.35 Bash install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf bash-*.tar.*
cd bash-*/

# Installation here

}

cd /sources/
rm -rf bash-*/
```

---
## 8.36 Libtool install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf libtool-*.tar.*
cd libtool-*/

# Installation here

}

cd /sources/
rm -rf libtool-*/
```

---
## 8.37 GDBM install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf gdbm-*.tar.*
cd gdbm-*/

# Installation here

}

cd /sources/
rm -rf gdbm-*/
```

---
## 8.38 Gperf install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf gperf-*.tar.*
cd gperf-*/

# Installation here

}

cd /sources/
rm -rf gperf-*/
```

---
## 8.39 Expat install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf expat-*.tar.*
cd expat-*/

# Installation here

}

cd /sources/
rm -rf expat-*/
```

---
## 8.40 Inetutils install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf inetutils-*.tar.*
cd inetutils-*/

# Installation here

}

cd /sources/
rm -rf inetutils-*/
```

---
## 8.41 Less install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf less-*.tar.*
cd less-*/

# Installation here

}

cd /sources/
rm -rf less-*/
```

---
## 8.42 Perl install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf perl-*.tar.*
cd perl-*/

# Installation here

}

cd /sources/
rm -rf perl-*/
```

---
## 8.43 XML::Parser install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf XML-Parser-*.tar.*
cd XML-Parser-*/

# Installation here

}

cd /sources/
rm -rf XML-Parser-*/
```

---
## 8.44 Intltool install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf intltool-*.tar.*
cd intltool-*/

# Installation here

}

cd /sources/
rm -rf intltool-*/
```

---
## 8.45 Autoconf install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf autoconf-*.tar.*
cd autoconf-*/

# Installation here

}

cd /sources/
rm -rf autoconf-*/
```

---
## 8.46 Automake install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf automake-*.tar.*
cd automake-*/

# Installation here

}

cd /sources/
rm -rf automake-*/
```



## Continue to next section
Next section: [8.47 - 8.80](lfsch8s47-80.md)



:trollface::trollface::trollface: