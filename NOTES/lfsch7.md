[<- Back](.)

#### Preface:
chapter 6 is in it's own file [here](./lfsch6.md)

again, hopefully this works lol good luck


# CHAPTER 7: Entering Chroot and Building Additional Temporary Tools
## 7.0.S Setup
#### Run as `root`, no more `lfs`
> The commands in the remainder of this book must be performed while logged in as user root and no longer as user lfs. Also, double check that $LFS is set in root's environment.

Set `$LFS` variable
```bash
export LFS=/mnt/lfs
```
Set `MAKEFLAGS` variable
```bash
export MAKEFLAGS='-j4'
```
Check your “LFS”, “ARCH”, “NPROC”, and “MAKEFLAGS” environment variables
```bash
echo "LFS=\"$LFS $(df $LFS|tail -1|awk '{print $1,int($2/1000000)"G"}')\" ARCH $(arch) NPROC=$(nproc) MAKEFLAGS=$MAKEFLAGS"
```

---
## 7.2-7.4 All in one
7.2 Changing Ownership\
7.3 Preparing Virtual Kernel File Systems\
7.4 Entering the Chroot Environment

#### Run as `root`
```bash
echo "= (7.2) ======================================";
echo "Change \$LFS/* ownership from lfs to root"
chown -R root:root $LFS/{usr,lib,var,etc,bin,sbin,tools}
case $(uname -m) in
  x86_64) chown -R root:root $LFS/lib64 ;;
esac
echo "= (7.3) ======================================"
echo "Mount virtual filesystem"
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
echo "= (7.4) ======================================";
echo "Enter the matrix (chroot)"
chroot "$LFS" /usr/bin/env -i   \
    HOME=/root                  \
    TERM="$TERM"                \
    PS1='(lfs chroot) \u:\w\$ ' \
    PATH=/usr/bin:/usr/sbin     \
    /bin/bash --login
```
If you see this (first time `chroot`) => success!

`(lfs chroot) I have no name!:/# `


---
## 7.5 Creating Directories
```bash
mkdir -pv /{boot,home,mnt,opt,srv}
mkdir -pv /etc/{opt,sysconfig}
mkdir -pv /lib/firmware
mkdir -pv /media/{floppy,cdrom}
mkdir -pv /usr/{,local/}{include,src}
mkdir -pv /usr/local/{bin,lib,sbin}
mkdir -pv /usr/{,local/}share/{color,dict,doc,info,locale,man}
mkdir -pv /usr/{,local/}share/{misc,terminfo,zoneinfo}
mkdir -pv /usr/{,local/}share/man/man{1..8}
mkdir -pv /var/{cache,local,log,mail,opt,spool}
mkdir -pv /var/lib/{color,misc,locate}

ln -sfv /run /var/run
ln -sfv /run/lock /var/lock

install -dv -m 0750 /root
install -dv -m 1777 /tmp /var/tmp
```

Make sure `/usr/lib64` directory does not exist
to comply with [Filesystem Hierarchy Standard (FHS)](https://refspecs.linuxfoundation.org/fhs.shtml)\
```bash
rm -rf /usr/lib64/
```

---
## 7.6 Creating Essential Files and Symlinks
```bash
ln -sv /proc/self/mounts /etc/mtab

cat > /etc/hosts << EOF
127.0.0.1  localhost $(hostname)
::1        localhost
EOF

cat > /etc/passwd << "EOF"
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/dev/null:/usr/bin/false
daemon:x:6:6:Daemon User:/dev/null:/usr/bin/false
messagebus:x:18:18:D-Bus Message Daemon User:/run/dbus:/usr/bin/false
uuidd:x:80:80:UUID Generation Daemon User:/dev/null:/usr/bin/false
nobody:x:65534:65534:Unprivileged User:/dev/null:/usr/bin/false
EOF

cat > /etc/group << "EOF"
root:x:0:
bin:x:1:daemon
sys:x:2:
kmem:x:3:
tape:x:4:
tty:x:5:
daemon:x:6:
floppy:x:7:
disk:x:8:
lp:x:9:
dialout:x:10:
audio:x:11:
video:x:12:
utmp:x:13:
usb:x:14:
cdrom:x:15:
adm:x:16:
messagebus:x:18:
input:x:24:
mail:x:34:
kvm:x:61:
uuidd:x:80:
wheel:x:97:
users:x:999:
nogroup:x:65534:
EOF

echo "tester:x:101:101::/home/tester:/bin/bash" >> /etc/passwd
echo "tester:x:101:" >> /etc/group
install -o tester -d /home/tester

exec /usr/bin/bash --login

touch /var/log/{btmp,lastlog,faillog,wtmp}
chgrp -v utmp /var/log/lastlog
chmod -v 664  /var/log/lastlog
chmod -v 600  /var/log/btmp
```


## 7.7 - 7.12 All in one copy-paste (OPTIONAL, RECOMMENDED)
[Script here as a text file](lfsch7allpackage.txt)\
Just copy and paste the script.\
Then skip to [Section 7.13](#713-cleaning-up-and-saving-the-temporary-system)


---
## 7.7 Gettext install
Approximate time required: 1.55 SBU
```bash
cd /sources/

time {
tar xf gettext-*.tar.xz
cd gettext-*/

./configure --disable-shared
make
cp -v gettext-tools/src/{msgfmt,msgmerge,xgettext} /usr/bin
}

cd /sources/
rm -rf gettext-*/
```


---
## 7.8 Bison install
Approximate time required: 0.3 SBU
```bash
cd /sources/

time {
tar xf bison-*.tar.xz
cd bison-*/

./configure --prefix=/usr \
        --docdir=/usr/share/doc/bison-3.8.2
make
make install
}

cd /sources/
rm -rf bison-*/
```


---
## 7.9 Perl install
Approximate time required: 1.53 SBU
```bash
cd /sources/

time {
tar xf perl-*.tar.xz
cd perl-*/

sh Configure -des                                        \
             -Dprefix=/usr                               \
             -Dvendorprefix=/usr                         \
             -Duseshrplib                                \
             -Dprivlib=/usr/lib/perl5/5.38/core_perl     \
             -Darchlib=/usr/lib/perl5/5.38/core_perl     \
             -Dsitelib=/usr/lib/perl5/5.38/site_perl     \
             -Dsitearch=/usr/lib/perl5/5.38/site_perl    \
             -Dvendorlib=/usr/lib/perl5/5.38/vendor_perl \
             -Dvendorarch=/usr/lib/perl5/5.38/vendor_perl
make
make install
}

cd /sources/
rm -rf perl-*/
```


---
## 7.10 Python install
> Some Python 3 modules can't be built now because the dependencies are not installed yet. The compilation of some files will fail and the compiler message may seem to indicate “fatal error”. The message should be ignored. Just make sure the toplevel make command has not failed.

Approximate time required: 1.2 SBU
```bash
cd /sources/

time {
tar xf Python-*.tar.xz
cd Python-*/

./configure --prefix=/usr   \
            --enable-shared \
            --without-ensurepip
make
make install
}

cd /sources/
rm -rf Python-*/
```


---
## 7.11 Texinfo install
Approximate time required: 0.3 SBU
```bash
cd /sources/

time {
tar xf texinfo-*.tar.xz
cd texinfo-*/

./configure --prefix=/usr
make
make install
}

cd /sources/
rm -rf texinfo-*/
```


---
## 7.12 Util-linux install
Approximate time required: 0.7 SBU
```bash
cd /sources/

time {
tar xf util-linux-*.tar.xz
cd util-linux-*/

mkdir -pv /var/lib/hwclock
./configure ADJTIME_PATH=/var/lib/hwclock/adjtime    \
        --libdir=/usr/lib    \
        --runstatedir=/run   \
        --docdir=/usr/share/doc/util-linux-2.39.1 \
        --disable-chfn-chsh  \
        --disable-login      \
        --disable-nologin    \
        --disable-su         \
        --disable-setpriv    \
        --disable-runuser    \
        --disable-pylibmount \
        --disable-static     \
        --without-python
make
make install
}

cd /sources/
rm -rf util-linux-*/
```


---
## 7.13 Cleaning up and Saving the Temporary System

## 7.13.1 Cleaning
Do some cleaning to save ~1.1GB
```bash
# remove documentation (35MB)
rm -rf /usr/share/{info,man,doc}/*
find /usr/{lib,libexec} -name \*.la -delete
# remove cross toolchain (>1GB)
rm -rf /tools
```


## 7.13.2 Backup
~~(OPTIONAL BUT RECOMMENDED)~~
**NEVERMIND IT IS REQUIRED FOR ASSIGNMENT PLEASE BACKUP**

> "Real Computer Science Students Do BACKUP! Prove that you are a genuine (ORI) Computer Science student and not just an observer of Java language studies or a no-level Python zoologist."
> \-RMS 12 october 2023

Leave the chroot environment\
NOTE: you may need to exit multiple times to get to actual root
```bash
exit
```
Unmount the virtual file system
```bash
mountpoint -q $LFS/dev/shm && umount $LFS/dev/shm
umount $LFS/dev/pts
umount $LFS/{sys,proc,run,dev}
```

Create the backup\
Approximate time required: 6.1 SBU
```bash
cd $LFS
time { tar -cJpvf $HOME/lfs-temp-tools-12.0.tar.xz .; }
```

## 7.13.3 Restoring the backup
#### Run as `root`
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
> The following commands are extremely dangerous. If you run `rm -rf ./*` as the root user and you do not change to the $LFS directory or the LFS environment variable is not set for the root user, it will destroy your entire host system. YOU ARE WARNED.

Delete current files and restore backup
```bash
cd $LFS
rm -rf ./*
tar -xpf $HOME/lfs-temp-tools-12.0.tar.xz
```


## 7.13.S Reentering chroot environment
Before continuing to chapter 8

Mount virtual file systems and enter chroot environment
#### Run as `root`
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


# FINISHING: Generate report

## F.1 Move backup to /var/tmp
#### Run as `root`
```bash
mv -v $HOME/lfs-temp-tools-12.0.tar.xz /var/tmp/
du -s -h /var/tmp/lfs-temp-tools-12.0.tar.xz
```
Check `lfs-temp-tools-12.0.tar.xz` is larger than 800MB => OK
> Don’t delete the lfs-temp-tools-12.0.tar.xz file until the end of the term.
If prompted, you should be able to show that file.


## F.2 Run bash script
#### Run as `user`
```bash
cd $HOME/mywork/WEEK09/
bash 09-WEEK09.sh
cd $HOME/RESULT/W09/
ls -al
```