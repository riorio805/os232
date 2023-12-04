Congratulations!!!!\
Hope you had a good night's sleep\
There is still a lot more packages to go\
gogogogogogogo\
:computer::no_entry_sign::clock5:


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
## 8.28 Pkgconf install
Approximate time required: 0.07 SBU
```bash
cd /sources/

time {
tar xf pkgconf*.tar.*
cd pkgconf*/

./configure --prefix=/usr              \
            --disable-static           \
            --docdir=/usr/share/doc/pkgconf-2.0.1
make
make install
ln -sv pkgconf   /usr/bin/pkg-config
ln -sv pkgconf.1 /usr/share/man/man1/pkg-config.1
}
cd /sources/
rm -rf pkgconf*/
```

---
## 8.29 Ncurses install
Approximate time required: 0.58 SBU

```bash
cd /sources/

time {
tar xf ncurses*.tar.*
cd ncurses*/

./configure --prefix=/usr           \
            --mandir=/usr/share/man \
            --with-shared           \
            --without-debug         \
            --without-normal        \
            --with-cxx-shared       \
            --enable-pc-files       \
            --enable-widec          \
            --with-pkg-config-libdir=/usr/lib/pkgconfig
make
make DESTDIR=$PWD/dest install
install -vm755 dest/usr/lib/libncursesw.so.6.4 /usr/lib
rm -v  dest/usr/lib/libncursesw.so.6.4
cp -av dest/* /
for lib in ncurses form panel menu ; do
    rm -vf                    /usr/lib/lib${lib}.so
    echo "INPUT(-l${lib}w)" > /usr/lib/lib${lib}.so
    ln -sfv ${lib}w.pc        /usr/lib/pkgconfig/${lib}.pc
done
rm -vf                     /usr/lib/libcursesw.so
echo "INPUT(-lncursesw)" > /usr/lib/libcursesw.so
ln -sfv libncurses.so      /usr/lib/libcurses.so
cp -v -R doc -T /usr/share/doc/ncurses-6.4
}
cd /sources/
rm -rf ncurses*/
```

---
## 8.30 Sed install
Approximate time required: 0.71 SBU
### 8.30.1 Compile and run tests
```bash
cd /sources/

time {
tar xf sed*.tar.*
cd sed*/

./configure --prefix=/usr
make
make html

chown -Rv tester .
su tester -c "PATH=$PATH make check"
}
```
Expected summary of `make check`
```
============================================================================
Testsuite summary for GNU sed 4.9
============================================================================
# TOTAL: 192
# PASS:  171
# SKIP:  21
# XFAIL: 0
# FAIL:  0
# XPASS: 0
# ERROR: 0
============================================================================
```

### 8.30.2 Install
```bash
time {
make install
install -d -m755           /usr/share/doc/sed-4.9
install -m644 doc/sed.html /usr/share/doc/sed-4.9
}
cd /sources/
rm -rf sed*/
```

---
## 8.31 Psmisc install
Approximate time required: 0.15 SBU
### 8.31.1 Compile and run tests
```bash
cd /sources/

time {
tar xf psmisc*.tar.*
cd psmisc*/

./configure --prefix=/usr
make

make check
}
```
Make sure all test passed

### 8.31.2 Install
```bash
time {
make install
}
cd /sources/
rm -rf psmisc*/
```

---
## 8.32 Gettext install
Approximate time required: 4.61 SBU
### 8.32.1 Compile and run tests
```bash
cd /sources/

time {
tar xf gettext*.tar.*
cd gettext*/

./configure --prefix=/usr    \
            --disable-static \
            --docdir=/usr/share/doc/gettext-0.22
make

make check
}
```
Expected summary of `make check`
```
============================================================================
Testsuite summary for gettext-tools 0.22
============================================================================
# TOTAL: 314
# PASS:  300
# SKIP:  14
# XFAIL: 0
# FAIL:  0
# XPASS: 0
# ERROR: 0
============================================================================
```

### 8.32.2 Install
```bash
time {
make install
chmod -v 0755 /usr/lib/preloadable_libintl.so
}
cd /sources/
rm -rf gettext*/
```

---
## 8.33 Bison install
Approximate time required: 5.96 SBU
### 8.33.1 Compile and run tests
```bash
cd /sources/

time {
tar xf bison*.tar.*
cd bison*/

./configure --prefix=/usr --docdir=/usr/share/doc/bison-3.8.2
make

make check
}
```
Expected summary of `make check`
```
## ------------- ##
## Test results. ##
## ------------- ##

712 tests were successful.
64 tests were skipped.
```

### 8.33.2 Install
```bash
time {
make install
}
cd /sources/
rm -rf bison*/
```

---
## 8.34 Grep install
Approximate time required: 0.98 SBU
### 8.34.1 Compile and run tests
```bash
cd /sources/

time {
tar xf grep*.tar.*
cd grep*/

sed -i "s/echo/#echo/" src/egrep.sh
./configure --prefix=/usr
make

make check
}
```
Expected summary of `make check`
```
============================================================================
Testsuite summary for GNU grep 3.11
============================================================================
# TOTAL: 226
# PASS:  210
# SKIP:  16
# XFAIL: 0
# FAIL:  0
# XPASS: 0
# ERROR: 0
============================================================================
```

### 8.34.2 Install
```bash
time {
make install
}
cd /sources/
rm -rf grep*/
```

---
## 8.35 Bash install
Approximate time required: 2.23 SBU
### 8.35.1 Compile and run tests
```bash
cd /sources/

time {
tar xf bash*.tar.*
cd bash*/

./configure --prefix=/usr             \
            --without-bash-malloc     \
            --with-installed-readline \
            --docdir=/usr/share/doc/bash-5.2.15
make

chown -Rv tester .
su -s /usr/bin/expect tester << EOF
set timeout -1
spawn make tests
expect eof
lassign [wait] _ _ _ value
exit $value
EOF
}
```

### 8.35.2 Install
```bash
time {
make install
}
cd /sources/
rm -rf bash*/
exec /usr/bin/bash --login
```

---
## 8.36 Libtool install
Approximate time required: 5.44 SBU
### 8.36.1 Compile and run tests
```bash
cd /sources/

time {
tar xf libtool*.tar.*
cd libtool*/

./configure --prefix=/usr
make

make -k check
}
```
Expected summary of `make check`
```
## ------------- ##
## Test results. ##
## ------------- ##

ERROR: 137 tests were run,
65 failed (58 expected failures).
32 tests were skipped.
```
```
============================================================================
Testsuite summary for GNU Libtool 2.4.7
============================================================================
# TOTAL: 6
# PASS:  4
# SKIP:  2
# XFAIL: 0
# FAIL:  0
# XPASS: 0
# ERROR: 0
============================================================================
```

### 8.36.2 Install
```bash
time {
make install
rm -fv /usr/lib/libltdl.a
}
cd /sources/
rm -rf libtool*/
```

---
## 8.37 GDBM install
Approximate time required: 0.19 SBU
### 8.37.1 Compile and run tests
```bash
cd /sources/

time {
tar xf gdbm*.tar.*
cd gdbm*/

./configure --prefix=/usr    \
            --disable-static \
            --enable-libgdbm-compat
make

make check
}
```
Expected summary of `make check`
```
## ------------- ##
## Test results. ##
## ------------- ##

All 33 tests were successful.
```

### 8.37.2 Install
```bash
time {
make install
}
cd /sources/
rm -rf gdbm*/
```

---
## 8.38 Gperf install
Approximate time required: 0.08 SBU
### 8.38.1 Compile and run tests
```bash
cd /sources/

time {
tar xf gperf*.tar.*
cd gperf*/

./configure --prefix=/usr --docdir=/usr/share/doc/gperf-3.1
make

make -j1 check
}
```
Make sure no errors in `make check`

### 8.38.2 Install
```bash
time {
make install
}
cd /sources/
rm -rf gperf*/
```

---
## 8.39 Expat install
Approximate time required: 0.17 SBU
### 8.39.1 Compile and run tests
```bash
cd /sources/

time {
tar xf expat*.tar.*
cd expat*/

./configure --prefix=/usr    \
            --disable-static \
            --docdir=/usr/share/doc/expat-2.5.0
make

make check
}
```
Expected summary of `make check`
```
============================================================================
Testsuite summary for expat 2.5.0
============================================================================
# TOTAL: 2
# PASS:  2
# SKIP:  0
# XFAIL: 0
# FAIL:  0
# XPASS: 0
# ERROR: 0
============================================================================
```

### 8.39.2 Install
```bash
time {
make install
install -v -m644 doc/*.{html,css} /usr/share/doc/expat-2.5.0
}
cd /sources/
rm -rf expat*/
```


---
## 8.40 Inetutils install
Approximate time required: 0.67 SBU
### 8.40.1 Compile and run tests
```bash
cd /sources/

time {
tar xf inetutils*.tar.*
cd inetutils*/

./configure --prefix=/usr        \
            --bindir=/usr/bin    \
            --localstatedir=/var \
            --disable-logger     \
            --disable-whois      \
            --disable-rcp        \
            --disable-rexec      \
            --disable-rlogin     \
            --disable-rsh        \
            --disable-servers
make

make check
}
```
Expected summary of `make check`
```
============================================================================
Testsuite summary for GNU inetutils 2.4
============================================================================
# TOTAL: 12
# PASS:  11
# SKIP:  1
# XFAIL: 0
# FAIL:  0
# XPASS: 0
# ERROR: 0
============================================================================
```

### 8.40.2 Install
```bash
time {
make install
mv -v /usr/{,s}bin/ifconfig
}
cd /sources/
rm -rf inetutils*/
```


---
## 8.41 Less install
Approximate time required: 0.14 SBU
### 8.41.1 Compile and run tests
```bash
cd /sources/

time {
tar xf less*.tar.*
cd less*/

./configure --prefix=/usr --sysconfdir=/etc
make

make check
}
```
Expected summary of `make check`
```
RAN  13 tests with 0 errors
```

### 8.41.2 Install
```bash
time {
make install
}
cd /sources/
rm -rf less*/
```


---
## 8.42 Perl install
Approximate time required: 13.98 SBU
### 8.42.1 Compile and run tests
```bash
cd /sources/

time {
tar xf perl*.tar.*
cd perl*/

export BUILD_ZLIB=False
export BUILD_BZIP2=0
sh Configure -des                                         \
             -Dprefix=/usr                                \
             -Dvendorprefix=/usr                          \
             -Dprivlib=/usr/lib/perl5/5.38/core_perl      \
             -Darchlib=/usr/lib/perl5/5.38/core_perl      \
             -Dsitelib=/usr/lib/perl5/5.38/site_perl      \
             -Dsitearch=/usr/lib/perl5/5.38/site_perl     \
             -Dvendorlib=/usr/lib/perl5/5.38/vendor_perl  \
             -Dvendorarch=/usr/lib/perl5/5.38/vendor_perl \
             -Dman1dir=/usr/share/man/man1                \
             -Dman3dir=/usr/share/man/man3                \
             -Dpager="/usr/bin/less -isR"                 \
             -Duseshrplib                                 \
             -Dusethreads
make

make test
}
```
Expected summary of `make test`
```
All tests successful.
Elapsed: XYZ sec
u=5.94  s=2.06  cu=526.91  cs=45.08  scripts=2612  tests=1196071
```

### 8.42.2 Install
```bash
time {
make install
unset BUILD_ZLIB BUILD_BZIP2
}
cd /sources/
rm -rf perl*/
```

---
## 8.43 XML::Parser install
Approximate time required: 0.04 SBU
### 8.43.1 Compile and run tests
```bash
cd /sources/

time {
tar xf XML-Parser*.tar.*
cd XML-Parser*/

perl Makefile.PL
make

make test
}
```
Expected summary of `make test`
```
All tests successful.
Files=15, Tests=140,  1 wallclock secs ( 0.04 usr  0.00 sys +  0.47 cusr  0.05 csys =  0.56 CPU)
Result: PASS
```

### 8.43.2 Install
```bash
time {
make install
}
cd /sources/
rm -rf XML-Parser*/
```

---
## 8.44 Intltool install
Approximate time required: 0.04 SBU
### 8.44.1 Compile and run tests
```bash
cd /sources/

time {
tar xf intltool*.tar.*
cd intltool*/

sed -i 's:\\\${:\\\$\\{:' intltool-update.in
./configure --prefix=/usr
make

make check
}
```
Expected summary of `make check`
```
============================================================================
Testsuite summary for intltool 0.51.0
============================================================================
# TOTAL: 1
# PASS:  1
# SKIP:  0
# XFAIL: 0
# FAIL:  0
# XPASS: 0
# ERROR: 0
============================================================================
```

### 8.44.2 Install
```bash
time {
make install
install -v -Dm644 doc/I18N-HOWTO /usr/share/doc/intltool-0.51.0/I18N-HOWTO
}
cd /sources/
rm -rf intltool*/
```

---
## 8.45 Autoconf install
Approximate time required: 5.33 SBU
### 8.45.1 Compile and run tests
```bash
cd /sources/

time {
tar xf autoconf*.tar.*
cd autoconf*/

sed -e 's/SECONDS|/&SHLVL|/'               \
    -e '/BASH_ARGV=/a\        /^SHLVL=/ d' \
    -i.orig tests/local.at
./configure --prefix=/usr
make

make check TESTSUITEFLAGS=-j4
}
```
Expected summary of `make check`
```
## ------------- ##
## Test results. ##
## ------------- ##

543 tests behaved as expected.
56 tests were skipped.
```

### 8.45.2 Install
```bash
time {
make install
}
cd /sources/
rm -rf autoconf*/
```

---
## 8.46 Automake install
Approximate time required: 16.34 SBU
### 8.46.1 Compile and run tests
```bash
cd /sources/

time {
tar xf automake*.tar.*
cd automake*/

./configure --prefix=/usr --docdir=/usr/share/doc/automake-1.16.5
make

make -j4 check
}
```
Expected summary of `make check`
>The test t/subobj.sh is known to fail.
```
============================================================================
Testsuite summary for GNU Automake 1.16.5
============================================================================
# TOTAL: 2926
# PASS:  2725
# SKIP:  163
# XFAIL: 38
# FAIL:  0
# XPASS: 0
# ERROR: 0
============================================================================
```

### 8.46.2 Install
```bash
time {
make install
}
cd /sources/
rm -rf automake*/
```





## Continue to next section
Next section: [8.47 - 8.63](lfsch8s47-63.md)



:trollface::trollface::trollface: