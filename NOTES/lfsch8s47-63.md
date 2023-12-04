I don't have any funny things to show here so just go to the scripts



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

---
## 8.47 OpenSSL install
Approximate time required: 6.46 SBU
### 8.47.1 Compile and run tests
```bash
cd /sources/

time {
tar xf openssl*.tar.*
cd openssl*/

./config --prefix=/usr         \
         --openssldir=/etc/ssl \
         --libdir=lib          \
         shared                \
         zlib-dynamic
make
make test
}
```
Expected summary of `make test`
```
All tests successful.
Files=252, Tests=3364, 286 wallclock secs ( 4.93 usr  0.28 sys + 234.44 cusr 43.60 csys = 283.25 CPU)
Result: PASS
```

### 8.47.2 Install
```bash
time {
sed -i '/INSTALL_LIBS/s/libcrypto.a libssl.a//' Makefile
make MANSUFFIX=ssl install
mv -v /usr/share/doc/openssl /usr/share/doc/openssl-3.1.2
cp -vfr doc/* /usr/share/doc/openssl-3.1.2
}
cd /sources/
rm -rf openssl*/
```

---
## 8.48 Kmod install
Approximate time required: 0.13 SBU
```bash
cd /sources/

time {
tar xf kmod*.tar.*
cd kmod*/

./configure --prefix=/usr          \
            --sysconfdir=/etc      \
            --with-openssl         \
            --with-xz              \
            --with-zstd            \
            --with-zlib
make

make install

for target in depmod insmod modinfo modprobe rmmod; do
  ln -sfv ../bin/kmod /usr/sbin/$target
done

ln -sfv kmod /usr/bin/lsmod
}
cd /sources/
rm -rf kmod*/
```

---
## 8.49 Libelf from Elfutils install
Approximate time required: 0.81 SBU
### 8.49.1 Compile and run tests
```bash
cd /sources/

time {
tar xf elfutils*.tar.*
cd elfutils*/

./configure --prefix=/usr                \
            --disable-debuginfod         \
            --enable-libdebuginfod=dummy
make

make check
}
```
Expected summary of `make check`
```
============================================================================
Testsuite summary for elfutils 0.189
============================================================================
# TOTAL: 238
# PASS:  233
# SKIP:  5
# XFAIL: 0
# FAIL:  0
# XPASS: 0
# ERROR: 0
============================================================================
```

### 8.49.2 Install
```bash
time {
make -C libelf install
install -vm644 config/libelf.pc /usr/lib/pkgconfig
rm /usr/lib/libelf.a
}
cd /sources/
rm -rf elfutils*/
```

---
## 8.50 Libffi install
Approximate time required: 3.22 SBU
### 8.50.1 Compile and run tests
```bash
cd /sources/

time {
tar xf libffi*.tar.*
cd libffi*/

./configure --prefix=/usr          \
            --disable-static       \
            --with-gcc-arch=native
make

make check
}
```
Expected summary of `make check`
```
		=== libffi Summary ===

# of expected passes		2366
```

### 8.50.2 Install
```bash
time {
make install
}
cd /sources/
rm -rf libffi*/
```

---
## 8.51 Python install
Approximate time required: 3.71 SBU
```bash
cd /sources/

time {
tar xf Python*.tar.*
cd Python*/

./configure --prefix=/usr        \
            --enable-shared      \
            --with-system-expat  \
            --with-system-ffi    \
            --enable-optimizations
make

make install

cat > /etc/pip.conf << EOF
[global]
root-user-action = ignore
disable-pip-version-check = true
EOF

install -v -dm755 /usr/share/doc/python-3.11.4/html
tar --strip-components=1  \
    --no-same-owner       \
    --no-same-permissions \
    -C /usr/share/doc/python-3.11.4/html \
    -xvf ../python-3.11.4-docs-html.tar.bz2
}
cd /sources/
rm -rf Python*/
```

---
## 8.52 Flit-Core install
Approximate time required: 0.01 SBU
```bash
cd /sources/

time {
tar xf flit_core*.tar.*
cd flit_core*/

pip3 wheel -w dist --no-build-isolation --no-deps $PWD
pip3 install --no-index --no-user --find-links dist flit_core
}
cd /sources/
rm -rf flit_core*/
```

---
## 8.53 Wheel install
Approximate time required: 0.01 SBU
```bash
cd /sources/

time {
tar xf wheel*.tar.*
cd wheel*/

pip3 wheel -w dist --no-build-isolation --no-deps $PWD
pip3 install --no-index --find-links=dist wheel
}
cd /sources/
rm -rf wheel*/
```

---
## 8.54 Ninja install
Approximate time required: 0.65 SBU
### 8.54.1 Compile and run tests
```bash
cd /sources/

time {
tar xf ninja*.tar.*
cd ninja*/

export NINJAJOBS=4
python3 configure.py --bootstrap
./ninja ninja_test
./ninja_test --gtest_filter=-SubprocessTest.SetWithLots
}
```
Expected summary of `ninja_test`
```
passed
```

### 8.54.2 Install
```bash
time {
install -vm755 ninja /usr/bin/
install -vDm644 misc/bash-completion /usr/share/bash-completion/completions/ninja
install -vDm644 misc/zsh-completion  /usr/share/zsh/site-functions/_ninja
}
cd /sources/
rm -rf ninja*/
```

---
## 8.55 Meson install
Approximate time required: 0.03 SBU
```bash
cd /sources/

time {
tar xf meson*.tar.*
cd meson*/

pip3 wheel -w dist --no-build-isolation --no-deps $PWD
pip3 install --no-index --find-links dist meson
install -vDm644 data/shell-completions/bash/meson /usr/share/bash-completion/completions/meson
install -vDm644 data/shell-completions/zsh/_meson /usr/share/zsh/site-functions/_meson
}
cd /sources/
rm -rf meson*/
```

---
## 8.56 Coreutils install
Approximate time required: 3.15 SBU
### 8.56.1 Compile and run tests
```bash
cd /sources/

time {
tar xf coreutils*.tar.*
cd coreutils*/

patch -Np1 -i ../coreutils-9.3-i18n-1.patch
autoreconf -fiv
FORCE_UNSAFE_CONFIGURE=1 ./configure \
            --prefix=/usr            \
            --enable-no-install-program=kill,uptime
make
make NON_ROOT_USERNAME=tester check-root
groupadd -g 102 dummy -U tester
chown -Rv tester . 
su tester -c "PATH=$PATH make RUN_EXPENSIVE_TESTS=yes check"
groupdel dummy
}
```
Expected summary of `make check`
```
============================================================================
Testsuite summary for GNU coreutils 9.3
============================================================================
# TOTAL: 397
# PASS:  373
# SKIP:  24
# XFAIL: 0
# FAIL:  0
# XPASS: 0
# ERROR: 0
============================================================================
```

### 8.56.2 Install
```bash
time {
make install
mv -v /usr/bin/chroot /usr/sbin
mv -v /usr/share/man/man1/chroot.1 /usr/share/man/man8/chroot.8
sed -i 's/"1"/"8"/' /usr/share/man/man8/chroot.8
}
cd /sources/
rm -rf coreutils*/
```

---
## 8.57 Check install
Approximate time required: 2.76 SBU
### 8.57.1 Compile and run tests
```bash
cd /sources/

time {
tar xf check*.tar.*
cd check*/

./configure --prefix=/usr --disable-static
make

make check
}
```
Expected summary of `make check`
```
============================================================================
Testsuite summary for Check 0.15.2
============================================================================
# TOTAL: 9
# PASS:  9
# SKIP:  0
# XFAIL: 0
# FAIL:  0
# XPASS: 0
# ERROR: 0
============================================================================
```

### 8.57.2 Install
```bash
time {
make docdir=/usr/share/doc/check-0.15.2 install
}
cd /sources/
rm -rf check*/
```

---
## 8.58 Diffutils install
Approximate time required: 0.76 SBU
### 8.58.1 Compile and run tests
```bash
cd /sources/

time {
tar xf diffutils*.tar.*
cd diffutils*/

./configure --prefix=/usr
make

make check
}
```
Expected summary of `make check`
```
============================================================================
Testsuite summary for GNU diffutils 3.10
============================================================================
# TOTAL: 215
# PASS:  199
# SKIP:  16
# XFAIL: 0
# FAIL:  0
# XPASS: 0
# ERROR: 0
============================================================================
```

### 8.58.2 Install
```bash
time {
make install
}
cd /sources/
rm -rf diffutils*/
```

---
## 8.59 Gawk install
Approximate time required: 0.46 SBU
### 8.59.1 Compile and run tests
```bash
cd /sources/

time {
tar xf gawk*.tar.*
cd gawk*/

sed -i 's/extras//' Makefile.in
./configure --prefix=/usr
make

chown -Rv tester .
su tester -c "PATH=$PATH make check"
}
```
Expected summary of `make check`
```
make[3]: Entering directory '/sources/gawk-5.2.2/test'
ALL TESTS PASSED
make[3]: Leaving directory '/sources/gawk-5.2.2/test'
```

### 8.59.2 Install
```bash
time {
make LN='ln -f' install
ln -sv gawk.1 /usr/share/man/man1/awk.1
mkdir -pv                                   /usr/share/doc/gawk-5.2.2
cp    -v doc/{awkforai.txt,*.{eps,pdf,jpg}} /usr/share/doc/gawk-5.2.2
}
cd /sources/
rm -rf gawk*/
```

---
## 8.60 Findutils install
Approximate time required: 1.45 SBU
### 8.60.1 Compile and run tests
```bash
cd /sources/

time {
tar xf findutils*.tar.*
cd findutils*/

./configure --prefix=/usr --localstatedir=/var/lib/locate
make

chown -Rv tester .
su tester -c "PATH=$PATH make check"
}
```
Expected summary of `make check`
```
============================================================================
Testsuite summary for GNU findutils 4.9.0
============================================================================
# TOTAL: 262
# PASS:  246
# SKIP:  16
# XFAIL: 0
# FAIL:  0
# XPASS: 0
# ERROR: 0
============================================================================
...
============================================================================
Testsuite summary for GNU findutils 4.9.0
============================================================================
# TOTAL: 17
# PASS:  15
# SKIP:  2
# XFAIL: 0
# FAIL:  0
# XPASS: 0
# ERROR: 0
============================================================================
```

### 8.60.2 Install
```bash
time {
make install
}
cd /sources/
rm -rf findutils*/
```

---
## 8.61 Groff install
Approximate time required: 0.55 SBU
### 8.61.1 Compile and run tests
```bash
cd /sources/

time {
tar xf groff*.tar.*
cd groff*/

PAGE=A4 ./configure --prefix=/usr
make

make check
}
```
Expected summary of `make check`
```
============================================================================
Testsuite summary for GNU roff 1.23.0
============================================================================
# TOTAL: 164
# PASS:  151
# SKIP:  11
# XFAIL: 2
# FAIL:  0
# XPASS: 0
# ERROR: 0
============================================================================
```

### 8.61.2 Install
```bash
time {
make install
}
cd /sources/
rm -rf groff*/
```

---
## 8.62 GRUB install
Approximate time required: 0.96 SBU
```bash
cd /sources/

time {
tar xf grub*.tar.*
cd grub*/

unset {C,CPP,CXX,LD}FLAGS
patch -Np1 -i ../grub-2.06-upstream_fixes-1.patch
./configure --prefix=/usr          \
            --sysconfdir=/etc      \
            --disable-efiemu       \
            --disable-werror
make

make install
mv -v /etc/bash_completion.d/grub /usr/share/bash-completion/completions
}
cd /sources/
rm -rf grub*/
```

---
## 8.63 Gzip install
Approximate time required: 0.61 SBU
### 8.63.1 Compile and run tests
```bash
cd /sources/

time {
tar xf gzip*.tar.*
cd gzip*/

./configure --prefix=/usr
make

make check
}
```
Expected summary of `make check`
```
============================================================================
Testsuite summary for gzip 1.12
============================================================================
# TOTAL: 26
# PASS:  26
# SKIP:  0
# XFAIL: 0
# FAIL:  0
# XPASS: 0
# ERROR: 0
============================================================================
```

### 8.63.2 Install
```bash
time {
make install
}
cd /sources/
rm -rf gzip*/
```






## Continue to next section
Next section: [8.64 - 8.80](lfsch8s64-80.md)