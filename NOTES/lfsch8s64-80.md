again I don't have any funny things to show here so just go to the scripts



## 8.0 Chapter 8 Setup

### 8.0.S Entering chroot environment
#### Run as `root`
Check mounted or not
```bash
findmnt | grep $LFS
```
Output if LFS **IS MOUNTED**:
```
├─/mnt/lfs                                              /dev/sdb2   ext4        rw,relatime
│ ├─/mnt/lfs/dev                                        udev        devtmpfs    rw,nosuid,relatime,size=1981744k,nr_inodes=495436,mode=755,inode64
│ │ ├─/mnt/lfs/dev/pts                                  devpts      devpts      rw,nosuid,noexec,relatime,gid=5,mode=620,ptmxmode=000
│ │ └─/mnt/lfs/dev/shm                                  tmpfs       tmpfs       rw,nosuid,nodev,relatime,inode64
│ ├─/mnt/lfs/proc                                       proc        proc        rw,relatime
│ ├─/mnt/lfs/sys                                        sysfs       sysfs       rw,relatime
│ └─/mnt/lfs/run                                        tmpfs       tmpfs       rw,relatime,inode64
```
Output if LFS **IS NOT MOUNTED**:
```
├─/mnt/lfs                                              /dev/sdb2   ext4        rw,relatime
```
Mount virtual filesystem if not mounted
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
```
Enter chroot environment
```bash
chroot "$LFS" /usr/bin/env -i   \
    HOME=/root                  \
    TERM="$TERM"                \
    PS1='(lfs chroot) \u:\w\$ ' \
    PATH=/usr/bin:/usr/sbin     \
    /bin/bash --login
```


### 8.0.E Exiting chroot environment
When you want to exit just do this
```bash
exit
```

### 8.0.X Pre-flight Checks
Make sure you are in
`(lfs chroot) root:/# |`\
Create `version-check.sh` (See [Section 7.12T](./lfsch7.md#712t-test-installations) on creating `version-check.sh`)

Run `version-check.sh` to see version requirements(Make sure all is OK)
```bash
bash version-check.sh
```

Check your “NPROC”, and “MAKEFLAGS” environment variables
```bash
echo "NPROC=$(nproc) MAKEFLAGS=$MAKEFLAGS"
```
Set `MAKEFLAGS` variable
```bash
export MAKEFLAGS='-j4'
```

### 8.0.B Backup
See [Section 7.13.2](./lfsch7.md#7132-backup) on backing up the LFS system.



---
## 8.64 IPRoute2 install
Approximate time required: 0.16 SBU
```bash
cd /sources/

time {
tar xf iproute2*.tar.*
cd iproute2*/

sed -i /ARPD/d Makefile
rm -fv man/man8/arpd.8
make NETNS_RUN_DIR=/run/netns

make SBINDIR=/usr/sbin install
mkdir -pv             /usr/share/doc/iproute2-6.4.0
cp -v COPYING README* /usr/share/doc/iproute2-6.4.0
}
cd /sources/
rm -rf iproute2*/
```

---
## 8.65 Kbd install
Approximate time required: 0.26 SBU
### 8.65.1 Compile and run tests
```bash
cd /sources/

time {
tar xf kbd*.tar.*
cd kbd*/

patch -Np1 -i ../kbd-2.6.1-backspace-1.patch
sed -i '/RESIZECONS_PROGS=/s/yes/no/' configure
sed -i 's/resizecons.8 //' docs/man/man8/Makefile.in
./configure --prefix=/usr --disable-vlock
make

make check
}
```
Expected summary of `make check`
```
## ------------- ##
## Test results. ##
## ------------- ##

36 tests were successful.
4 tests were skipped.
```


### 8.65.2 Install
```bash
time {
make install
cp -R -v docs/doc -T /usr/share/doc/kbd-2.6.1
}
cd /sources/
rm -rf kbd*/
```

---
## 8.66 Libpipeline install
Approximate time required: 0.29 SBU
### 8.66.1 Compile and run tests
```bash
cd /sources/

time {
tar xf libpipeline*.tar.*
cd libpipeline*/

./configure --prefix=/usr
make

make check
}
```
Expected summary of `make check`
```
============================================================================
Testsuite summary for libpipeline 1.5.7
============================================================================
# TOTAL: 7
# PASS:  7
# SKIP:  0
# XFAIL: 0
# FAIL:  0
# XPASS: 0
# ERROR: 0
============================================================================
```

### 8.66.2 Install
```bash
time {
make install
}
cd /sources/
rm -rf libpipeline*/
```

---
## 8.67 Make install
Approximate time required: 1.02 SBU
### 8.67.1 Compile and run tests
```bash
cd /sources/

time {
tar xf make*.tar.*
cd make*/

./configure --prefix=/usr
make

chown -Rv tester .
su tester -c "PATH=$PATH make check"
}
```
Expected summary of `make check`
```
1444 Tests in 134 Categories Complete ... No Failures :-)


========================================================================
 Regression PASSED: GNU Make 4.4.1 (x86_64-pc-linux-gnu) built with gcc 
========================================================================
```

### 8.67.2 Install
```bash
time {
make install
}
cd /sources/
rm -rf make*/
```

---
## 8.68 Patch install
Approximate time required: 0.47 SBU
### 8.68.1 Compile and run tests
```bash
cd /sources/

time {
tar xf patch*.tar.*
cd patch*/

./configure --prefix=/usr
make

make check
}
```
Expected summary of `make check`
```
============================================================================
Testsuite summary for GNU patch 2.7.6
============================================================================
# TOTAL: 44
# PASS:  41
# SKIP:  1
# XFAIL: 2
# FAIL:  0
# XPASS: 0
# ERROR: 0
============================================================================
```

### 8.68.2 Install
```bash
time {
make install
}
cd /sources/
rm -rf patch*/
```

---
## 8.69 Tar install (very funny guys)
Approximate time required: 3.64 SBU
### 8.69.1 Compile and run tests
```bash
cd /sources/

time {
tar xf tar*.tar.*
cd tar*/

FORCE_UNSAFE_CONFIGURE=1  \
./configure --prefix=/usr
make

make check
}
```
Expected summary of `make check`
```
## ------------- ##
## Test results. ##
## ------------- ##

ERROR: 224 tests were run,
1 failed unexpectedly.
20 tests were skipped.
```

### 8.69.2 Install
```bash
time {
make install
make -C doc install-html docdir=/usr/share/doc/tar-1.35
}
cd /sources/
rm -rf tar*/
```

---
## 8.70 Texinfo install
Approximate time required: 0.92 SBU
### 8.70.1 Compile and run tests
```bash
cd /sources/

time {
tar xf texinfo*.tar.*
cd texinfo*/

./configure --prefix=/usr
make

make check
}
```
Make sure all test passed, check all summaries (FAIL: 0, XPASS: 0, ERROR: 0).

### 8.70.2 Install
```bash
time {
make install
make TEXMF=/usr/share/texmf install-tex
pushd /usr/share/info
  rm -v dir
  for f in *
    do install-info $f dir 2>/dev/null
  done
popd
}
cd /sources/
rm -rf texinfo*/
```

---
## 8.71 Vim install
Approximate time required: 4.36 SBU
### 8.71.1 Compile and run tests
```bash
cd /sources/

time {
tar xf vim*.tar.*
cd vim*/

echo '#define SYS_VIMRC_FILE "/etc/vimrc"' >> src/feature.h
./configure --prefix=/usr
make

chown -Rv tester .
su tester -c "LANG=en_US.UTF-8 make -j1 test" &> vim-test.log
}
```
Expected summary of `make check`
```
-------------------------------
Executed:  5574 Tests
 Skipped:   121 Tests
  FAILED:    14 Tests
```

### 8.71.2 Install
```bash
time {
make install
ln -sv vim /usr/bin/vi
for L in  /usr/share/man/{,*/}man1/vim.1; do
    ln -sv vim.1 $(dirname $L)/vi.1
done
ln -sv ../vim/vim90/doc /usr/share/doc/vim-9.0.1677

cat > /etc/vimrc << "EOF"
" Begin /etc/vimrc

" Ensure defaults are set before customizing settings, not after
source $VIMRUNTIME/defaults.vim
let skip_defaults_vim=1

set nocompatible
set backspace=2
set mouse=
syntax on
if (&term == "xterm") || (&term == "putty")
  set background=dark
endif

" End /etc/vimrc
EOF
}
cd /sources/
rm -rf vim*/
```

---
## 8.72 MarkupSafe install
Approximate time required: 0.03 SBU
```bash
cd /sources/

time {
tar xf MarkupSafe*.tar.*
cd MarkupSafe*/

pip3 wheel -w dist --no-build-isolation --no-deps $PWD
pip3 install --no-index --no-user --find-links dist Markupsafe
}
cd /sources/
rm -rf MarkupSafe*/
```

---
## 8.73 Jinja2 install
Approximate time required: 0.02 SBU
```bash
cd /sources/

time {
tar xf Jinja2*.tar.*
cd Jinja2*/

pip3 wheel -w dist --no-build-isolation --no-deps $PWD
pip3 install --no-index --no-user --find-links dist Jinja2
}
cd /sources/
rm -rf Jinja2*/
```

---
## 8.74 Udev from Systemd install
Approximate time required: 0.54 SBU
```bash
cd /sources/

time {
tar xf systemd-254.tar.gz
cd systemd-254/

sed -i -e 's/GROUP="render"/GROUP="video"/' \
       -e 's/GROUP="sgx", //' rules.d/50-udev-default.rules.in
sed '/systemd-sysctl/s/^/#/' -i rules.d/99-systemd.rules.in
mkdir -p build
cd       build
meson setup \
      --prefix=/usr                 \
      --buildtype=release           \
      -Dmode=release                \
      -Ddev-kvm-mode=0660           \
      -Dlink-udev-shared=false      \
      ..

ninja udevadm systemd-hwdb \
      $(grep -o -E "^build (src/libudev|src/udev|rules.d|hwdb.d)[^:]*" \
        build.ninja | awk '{ print $2 }')                              \
      $(realpath libudev.so --relative-to .)
rm rules.d/90-vconsole.rules
install -vm755 -d {/usr/lib,/etc}/udev/{hwdb,rules}.d
install -vm755 -d /usr/{lib,share}/pkgconfig
install -vm755 udevadm                     /usr/bin/
install -vm755 systemd-hwdb                /usr/bin/udev-hwdb
ln      -svfn  ../bin/udevadm              /usr/sbin/udevd
cp      -av    libudev.so{,*[0-9]}         /usr/lib/
install -vm644 ../src/libudev/libudev.h    /usr/include/
install -vm644 src/libudev/*.pc            /usr/lib/pkgconfig/
install -vm644 src/udev/*.pc               /usr/share/pkgconfig/
install -vm644 ../src/udev/udev.conf       /etc/udev/
install -vm644 rules.d/* ../rules.d/{*.rules,README} /usr/lib/udev/rules.d/
install -vm644 hwdb.d/*  ../hwdb.d/{*.hwdb,README}   /usr/lib/udev/hwdb.d/
install -vm755 $(find src/udev -type f | grep -F -v ".") /usr/lib/udev
tar -xvf ../../udev-lfs-20230818.tar.xz
make -f udev-lfs-20230818/Makefile.lfs install
tar -xf ../../systemd-man-pages-254.tar.xz                            \
    --no-same-owner --strip-components=1                              \
    -C /usr/share/man --wildcards '*/udev*' '*/libudev*'              \
                                  '*/systemd-'{hwdb,udevd.service}.8
sed 's/systemd\(\\\?-\)/udev\1/' /usr/share/man/man8/systemd-hwdb.8   \
                               > /usr/share/man/man8/udev-hwdb.8
sed 's|lib.*udevd|sbin/udevd|'                                        \
    /usr/share/man/man8/systemd-udevd.service.8                       \
  > /usr/share/man/man8/udevd.8
rm  /usr/share/man/man8/systemd-*.8
udev-hwdb update
}
cd /sources/
rm -rf systemd*/
```

---
## 8.75 Man-DB install
Approximate time required: 0.69 SBU
### 8.75.1 Compile and run tests
```bash
cd /sources/

time {
tar xf man-db*.tar.*
cd man-db*/

./configure --prefix=/usr                         \
            --docdir=/usr/share/doc/man-db-2.11.2 \
            --sysconfdir=/etc                     \
            --disable-setuid                      \
            --enable-cache-owner=bin              \
            --with-browser=/usr/bin/lynx          \
            --with-vgrind=/usr/bin/vgrind         \
            --with-grap=/usr/bin/grap             \
            --with-systemdtmpfilesdir=            \
            --with-systemdsystemunitdir=
make

make -k check
}
```
Expected summary of `make check`
```
============================================================================
Testsuite summary for man-db 2.11.2
============================================================================
# TOTAL: 12
# PASS:  11
# SKIP:  0
# XFAIL: 0
# FAIL:  1
# XPASS: 0
# ERROR: 0
============================================================================
```

### 8.75.2 Install
```bash
time {
make install
}
cd /sources/
rm -rf man-db*/
```

---
## 8.76 Procps-ng install
Approximate time required: 0.28 SBU
### 8.76.1 Compile and run tests
```bash
cd /sources/

time {
tar xf procps-ng*.tar.*
cd procps-ng*/

./configure --prefix=/usr                           \
            --docdir=/usr/share/doc/procps-ng-4.0.3 \
            --disable-static                        \
            --disable-kill
make

make check
}
```
Expected summary of `make check`
```
============================================================================
Testsuite summary for procps-ng 4.0.3
============================================================================
# TOTAL: 7
# PASS:  7
# SKIP:  0
# XFAIL: 0
# FAIL:  0
# XPASS: 0
# ERROR: 0
============================================================================
```

### 8.76.2 Install
```bash
time {
make install
}
cd /sources/
rm -rf procps-ng*/
```

---
## 8.77 Util-linux install
Approximate time required: 1.42 SBU
### 8.77.1 Compile and run tests
```bash
cd /sources/

time {
tar xf util-linux*.tar.*
cd util-linux*/

sed -i '/test_mkfds/s/^/#/' tests/helpers/Makemodule.am
./configure ADJTIME_PATH=/var/lib/hwclock/adjtime \
            --bindir=/usr/bin    \
            --libdir=/usr/lib    \
            --runstatedir=/run   \
            --sbindir=/usr/sbin  \
            --disable-chfn-chsh  \
            --disable-login      \
            --disable-nologin    \
            --disable-su         \
            --disable-setpriv    \
            --disable-runuser    \
            --disable-pylibmount \
            --disable-static     \
            --without-python     \
            --without-systemd    \
            --without-systemdsystemunitdir \
            --docdir=/usr/share/doc/util-linux-2.39.1
make
chown -Rv tester .
su tester -c "make -k check"
}
```
Expected summary of `make check`
```
---------------------------------------------------------------------
  All 261 tests PASSED
---------------------------------------------------------------------
```

### 8.77.2 Install
```bash
time {
make install
}
cd /sources/
rm -rf util-linux*/
```

---
## 8.78 E2fsprogs install
Approximate time required: 0.99 SBU
### 8.78.1 Compile and run tests
```bash
cd /sources/

time {
tar xf e2fsprogs*.tar.*
cd e2fsprogs*/

mkdir -v build
cd       build
../configure --prefix=/usr           \
             --sysconfdir=/etc       \
             --enable-elf-shlibs     \
             --disable-libblkid      \
             --disable-libuuid       \
             --disable-uuidd         \
             --disable-fsck
make

make check
}
```
Expected summary of `make check`
```
374 tests succeeded	1 tests failed
Tests failed: m_assume_storage_prezeroed 
```

### 8.78.2 Install
```bash
time {
make install
rm -fv /usr/lib/{libcom_err,libe2p,libext2fs,libss}.a
gunzip -v /usr/share/info/libext2fs.info.gz
install-info --dir-file=/usr/share/info/dir /usr/share/info/libext2fs.info
makeinfo -o      doc/com_err.info ../lib/et/com_err.texinfo
install -v -m644 doc/com_err.info /usr/share/info
install-info --dir-file=/usr/share/info/dir /usr/share/info/com_err.info
sed 's/metadata_csum_seed,//' -i /etc/mke2fs.conf
}
cd /sources/
rm -rf e2fsprogs*/
```

---
## 8.79 Sysklogd install
Approximate time required: 0.01 SBU
```bash
cd /sources/

time {
tar xf sysklogd-1.5.1.tar.gz
cd sysklogd-1.5.1/

sed -i '/Error loading kernel symbols/{n;n;d}' ksym_mod.c
sed -i 's/union wait/int/' syslogd.c
make
make BINDIR=/sbin install

cat > /etc/syslog.conf << "EOF"
# Begin /etc/syslog.conf

auth,authpriv.* -/var/log/auth.log
*.*;auth,authpriv.none -/var/log/sys.log
daemon.* -/var/log/daemon.log
kern.* -/var/log/kern.log
mail.* -/var/log/mail.log
user.* -/var/log/user.log
*.emerg *

# End /etc/syslog.conf
EOF

}
cd /sources/
rm -rf sysklogd-1.5.1/
```

---
## 8.80 Sysvinit install
Approximate time required: 0.02 SBU
```bash
cd /sources/

time {
tar xf sysvinit*.tar.*
cd sysvinit*/

patch -Np1 -i ../sysvinit-3.07-consolidated-1.patch
make
make install
}
cd /sources/
rm -rf sysvinit*/
```







## Continue to next section
Next section: [8.81 - 8.83](lfsch8s81-83.md)