Definitely bug free and tested under production standards :))))))

<img src="./there-are-none.png" width=300 alt="No more">


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

<br><br><br>

---

## 8.6 Zlib install
### 8.6.1 Compile and check
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf zlib-*.tar.*
cd zlib-*/

# Installation here
./configure --prefix=/usr
make
make check
}
```
Expected output of `make check` contains these 3 lines (make sure OK):
```
		*** zlib test OK ***
		*** zlib 64-bit test OK ***
		*** zlib shared test OK ***
```

### 8.6.2 Install
Approximate time required: x SBU
```bash
time {
make install
rm -fv /usr/lib/libz.a
}
cd /sources/
rm -rf zlib-*/
```


---
## 8.7 Bzip2 install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf bzip2-*.tar.*
cd bzip2-*/

# Installation here
patch -Np1 -i ../bzip2-1.0.8-install_docs-1.patch
sed -i 's@\(ln -s -f \)$(PREFIX)/bin/@\1@' Makefile
sed -i "s@(PREFIX)/man@(PREFIX)/share/man@g" Makefile

make -f Makefile-libbz2_so
make clean
make
make PREFIX=/usr install

cp -av libbz2.so.* /usr/lib
ln -sv libbz2.so.1.0.8 /usr/lib/libbz2.so
cp -v bzip2-shared /usr/bin/bzip2
for i in /usr/bin/{bzcat,bunzip2}; do
  ln -sfv bzip2 $i
done

rm -fv /usr/lib/libbz2.a
}

cd /sources/
rm -rf bzip2-*/
```

---
## 8.8 Xz install
### 8.8.1 Compile and run tests
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf xz-*.tar.*
cd xz-*/

# Installation here
./configure --prefix=/usr    \
            --disable-static \
            --docdir=/usr/share/doc/xz-5.4.4
make
make check
}
```
Expected summary of `make check`
```
============================================================================
Testsuite summary for XZ Utils 5.4.4
============================================================================
# TOTAL: 19
# PASS:  19
# SKIP:  0
# XFAIL: 0
# FAIL:  0
# XPASS: 0
# ERROR: 0
============================================================================
```
### 8.8.2 Install
Approximate time required: x SBU
```bash
time {
make install
}

cd /sources/
rm -rf xz-*/
```

---
## 8.9 Zstd install
> In the test output there are several places that indicate 'failed'. These are expected and only 'FAIL' is an actual test failure.

Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf zstd-*.tar.*
cd zstd-*/

# Installation here
make prefix=/usr
make check
make prefix=/usr install
rm -v /usr/lib/libzstd.a
}

cd /sources/
rm -rf zstd-*/
```

---
## 8.10 File install
Approximate time required: x SBU\
Make sure no errors during installation
```bash
cd /sources/

time {
tar xf file-*.tar.*
cd file-*/

# Installation here
./configure --prefix=/usr
make
make check
make install
}

cd /sources/
rm -rf file-*/
```

---
## 8.11 Readline install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf readline-*.tar.*
cd readline-*/

# Installation here
sed -i '/MV.*old/d' Makefile.in
sed -i '/{OLDSUFF}/c:' support/shlib-install
patch -Np1 -i ../readline-8.2-upstream_fix-1.patch

./configure --prefix=/usr    \
            --disable-static \
            --with-curses    \
            --docdir=/usr/share/doc/readline-8.2
make SHLIB_LIBS="-lncursesw"
make SHLIB_LIBS="-lncursesw" install
install -v -m644 doc/*.{ps,pdf,html,dvi} /usr/share/doc/readline-8.2
}

cd /sources/
rm -rf readline-*/
```

---
## 8.12 M4 install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf m4-*.tar.*
cd m4-*/

# Installation here
./configure --prefix=/usr
make
make check
make install
}

cd /sources/
rm -rf m4-*/
```

---
## 8.13 Bc install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf bc-*.tar.*
cd bc-*/

# Installation here
CC=gcc
./configure --prefix=/usr -G -O3 -r
make
make test
make install
}

cd /sources/
rm -rf bc-*/
```

---
## 8.14 Flex install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf flex-*.tar.*
cd flex-*/

# Installation here
./configure --prefix=/usr \
            --docdir=/usr/share/doc/flex-2.6.4 \
            --disable-static
make
make check
make install

ln -sv flex   /usr/bin/lex
ln -sv flex.1 /usr/share/man/man1/lex.1
}

cd /sources/
rm -rf flex-*/
```

---
## 8.15 Tcl install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf tcl-*.tar.*
cd tcl-*/

# Installation here
SRCDIR=$(pwd)
cd unix
./configure --prefix=/usr           \
            --mandir=/usr/share/man

make

sed -e "s|$SRCDIR/unix|/usr/lib|" \
    -e "s|$SRCDIR|/usr/include|"  \
    -i tclConfig.sh

sed -e "s|$SRCDIR/unix/pkgs/tdbc1.1.5|/usr/lib/tdbc1.1.5|" \
    -e "s|$SRCDIR/pkgs/tdbc1.1.5/generic|/usr/include|"    \
    -e "s|$SRCDIR/pkgs/tdbc1.1.5/library|/usr/lib/tcl8.6|" \
    -e "s|$SRCDIR/pkgs/tdbc1.1.5|/usr/include|"            \
    -i pkgs/tdbc1.1.5/tdbcConfig.sh

sed -e "s|$SRCDIR/unix/pkgs/itcl4.2.3|/usr/lib/itcl4.2.3|" \
    -e "s|$SRCDIR/pkgs/itcl4.2.3/generic|/usr/include|"    \
    -e "s|$SRCDIR/pkgs/itcl4.2.3|/usr/include|"            \
    -i pkgs/itcl4.2.3/itclConfig.sh

unset SRCDIR
make test
make install

chmod -v u+w /usr/lib/libtcl8.6.so
make install-private-headers
ln -sfv tclsh8.6 /usr/bin/tclsh
mv /usr/share/man/man3/{Thread,Tcl_Thread}.3
cd ..
tar -xf ../tcl8.6.13-html.tar.gz --strip-components=1
mkdir -v -p /usr/share/doc/tcl-8.6.13
cp -v -r  ./html/* /usr/share/doc/tcl-8.6.13
}

cd /sources/
rm -rf tcl-*/
```

---
## 8.16 Expect install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf expect-*.tar.*
cd expect-*/

# Installation here
./configure --prefix=/usr           \
            --with-tcl=/usr/lib     \
            --enable-shared         \
            --mandir=/usr/share/man \
            --with-tclinclude=/usr/include
make
make test
make install
ln -svf expect5.45.4/libexpect5.45.4.so /usr/lib
}

cd /sources/
rm -rf expect-*/
```

---
## 8.17 DejaGNU install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf dejagnu-*.tar.*
cd dejagnu-*/

# Installation here
mkdir -v build
cd       build
../configure --prefix=/usr
makeinfo --html --no-split -o doc/dejagnu.html ../doc/dejagnu.texi
makeinfo --plaintext       -o doc/dejagnu.txt  ../doc/dejagnu.texi
make install
install -v -dm755  /usr/share/doc/dejagnu-1.6.3
install -v -m644   doc/dejagnu.{html,txt} /usr/share/doc/dejagnu-1.6.3
make check
}

cd /sources/
rm -rf dejagnu-*/
```

---
## 8.18 Binutils install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf binutils-*.tar.*
cd binutils-*/

# Installation here

}

cd /sources/
rm -rf binutils-*/
```

---
## 8.19 GMP install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf gmp-*.tar.*
cd gmp-*/

# Installation here

}

cd /sources/
rm -rf gmp-*/
```

---
## 8.20 MPFR install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf mpfr-*.tar.*
cd mpfr-*/

# Installation here

}

cd /sources/
rm -rf mpfr-*/
```

---
## 8.21 MPC install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf mpc-*.tar.*
cd mpc-*/

# Installation here

}

cd /sources/
rm -rf mpc-*/
```

---
## 8.22 Attr install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf attr-*.tar.*
cd attr-*/

# Installation here

}

cd /sources/
rm -rf attr-*/
```

---
## 8.23 Acl install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf acl-*.tar.*
cd acl-*/

# Installation here

}

cd /sources/
rm -rf acl-*/
```

---
## 8.24 Libcap install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf libcap-*.tar.*
cd libcap-*/

# Installation here

}

cd /sources/
rm -rf libcap-*/
```

---
## 8.25 Libxcrypt install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf libxcrypt-*.tar.*
cd libxcrypt-*/

# Installation here

}

cd /sources/
rm -rf libxcrypt-*/
```

---
## 8.26 Shadow install
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf shadow-*.tar.*
cd shadow-*/

# Installation here

}

cd /sources/
rm -rf shadow-*/
```



## Continue to next section
Next section: [8.27 GCC](lfsch8s27gcc.md)