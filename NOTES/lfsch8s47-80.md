



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
## 8.47 OpenSSL install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf openssl-*.tar.*
cd openssl-*/

# Installation here

}

cd /sources/
rm -rf openssl-*/
```

---
## 8.48 Kmod install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf kmod-*.tar.*
cd kmod-*/

# Installation here

}

cd /sources/
rm -rf kmod-*/
```

---
## 8.49 Libelf from Elfutils install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf elfutils-*.tar.*
cd elfutils-*/

# Installation here

}

cd /sources/
rm -rf elfutils-*/
```

---
## 8.50 Libffi install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf libffi-*.tar.*
cd libffi-*/

# Installation here

}

cd /sources/
rm -rf libffi-*/
```

---
## 8.51 Python install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf Python-*.tar.*
cd Python-*/

# Installation here

}

cd /sources/
rm -rf Python-*/
```

---
## 8.52 Flit-Core install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf flit_core-*.tar.*
cd flit_core-*/

# Installation here

}

cd /sources/
rm -rf flit_core-*/
```

---
## 8.53 Wheel install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf wheel-*.tar.*
cd wheel-*/

# Installation here

}

cd /sources/
rm -rf wheel-*/
```

---
## 8.54 Ninja install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf ninja-*.tar.*
cd ninja-*/

# Installation here

}

cd /sources/
rm -rf ninja-*/
```

---
## 8.55 Meson install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf meson-*.tar.*
cd meson-*/

# Installation here

}

cd /sources/
rm -rf meson-*/
```

---
## 8.56 Coreutils install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf coreutils-*.tar.*
cd coreutils-*/

# Installation here

}

cd /sources/
rm -rf coreutils-*/
```

---
## 8.57 Check install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf check-*.tar.*
cd check-*/

# Installation here

}

cd /sources/
rm -rf check-*/
```

---
## 8.58 Diffutils install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf diffutils-*.tar.*
cd diffutils-*/

# Installation here

}

cd /sources/
rm -rf diffutils-*/
```

---
## 8.59 Gawk install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf gawk-*.tar.*
cd gawk-*/

# Installation here

}

cd /sources/
rm -rf gawk-*/
```

---
## 8.60 Findutils install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf findutils-*.tar.*
cd findutils-*/

# Installation here

}

cd /sources/
rm -rf findutils-*/
```

---
## 8.61 Groff install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf groff-*.tar.*
cd groff-*/

# Installation here

}

cd /sources/
rm -rf groff-*/
```

---
## 8.62 GRUB install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf grub-*.tar.*
cd grub-*/

# Installation here

}

cd /sources/
rm -rf grub-*/
```

---
## 8.63 Gzip install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf gzip-*.tar.*
cd gzip-*/

# Installation here

}

cd /sources/
rm -rf gzip-*/
```

---
## 8.64 IPRoute2 install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf iproute2-*.tar.*
cd iproute2-*/

# Installation here

}

cd /sources/
rm -rf iproute2-*/
```

---
## 8.65 Kbd install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf kbd-*.tar.*
cd kbd-*/

# Installation here

}

cd /sources/
rm -rf kbd-*/
```

---
## 8.66 Libpipeline install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf libpipeline-*.tar.*
cd libpipeline-*/

# Installation here

}

cd /sources/
rm -rf libpipeline-*/
```

---
## 8.67 Make install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf make-*.tar.*
cd make-*/

# Installation here

}

cd /sources/
rm -rf make-*/
```

---
## 8.68 Patch install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf patch-*.tar.*
cd patch-*/

# Installation here

}

cd /sources/
rm -rf patch-*/
```

---
## 8.69 Tar install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf tar-*.tar.*
cd tar-*/

# Installation here

}

cd /sources/
rm -rf tar-*/
```

---
## 8.70 Texinfo install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf texinfo-*.tar.*
cd texinfo-*/

# Installation here

}

cd /sources/
rm -rf texinfo-*/
```

---
## 8.71 Vim install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf vim-*.tar.*
cd vim-*/

# Installation here

}

cd /sources/
rm -rf vim-*/
```

---
## 8.72 MarkupSafe install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf MarkupSafe-*.tar.*
cd MarkupSafe-*/

# Installation here

}

cd /sources/
rm -rf MarkupSafe-*/
```

---
## 8.73 Jinja2 install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf Jinja2-*.tar.*
cd Jinja2-*/

# Installation here

}

cd /sources/
rm -rf Jinja2-*/
```

---
## 8.74 Udev from Systemd install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf systemd-*.tar.*
cd systemd-*/

# Installation here

}

cd /sources/
rm -rf systemd-*/
```

---
## 8.75 Man-DB install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf man-db-*.tar.*
cd man-db-*/

# Installation here

}

cd /sources/
rm -rf man-db-*/
```

---
## 8.76 Procps-ng install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf procps-ng-*.tar.*
cd procps-ng-*/

# Installation here

}

cd /sources/
rm -rf procps-ng-*/
```

---
## 8.77 Util-linux install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf util-linux-*.tar.*
cd util-linux-*/

# Installation here

}

cd /sources/
rm -rf util-linux-*/
```

---
## 8.78 E2fsprogs install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf e2fsprogs-*.tar.*
cd e2fsprogs-*/

# Installation here

}

cd /sources/
rm -rf e2fsprogs-*/
```

---
## 8.79 Sysklogd install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf sysklogd-*.tar.*
cd sysklogd-*/

# Installation here

}

cd /sources/
rm -rf sysklogd-*/
```

---
## 8.80 Sysvinit install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf sysvinit-*.tar.*
cd sysvinit-*/

# Installation here

}

cd /sources/
rm -rf sysvinit-*/
```


## Continue to next section
Next section: [8.81 - 8.83](lfsch8s81-83.md)