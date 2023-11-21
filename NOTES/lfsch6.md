[<- Back](.)

#### Preface:
chapter 7 is in it's own page [here](./lfsch7.md)

again, hopefully this works lol good luck

I recommend you just run the all-in-one script because no checking is required


# CHAPTER 6: Cross Compiling Temporary Tools
#### Run every script as `lfs`

## 6.0 Chapter 6 setup
### 6.0.C Check user `lfs` and `$LFS`
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
Check your “LFS”, “ARCH”, “NPROC”, and “MAKEFLAGS” environment variables
```bash
echo "LFS=\"$LFS $(df $LFS|tail -1|awk '{print $1,int($2/1000000)"G"}')\" ARCH $(arch) NPROC=$(nproc) MAKEFLAGS=$MAKEFLAGS"
```


### 6.0.P Copy-paste mania
This chapter but all in one [here (text file)](./lfsch6all-in-1.txt)\
Or use this script (run as `lfs`)
```bash
cd
wget -c https://riorio805.github.io/os232/NOTES/lfsch6all-in-1.sh
bash lfsch6all-in-1.sh
```

---
## 6.2 M4 install
Approximate time required: 0.25 SBU
```bash
cd $LFS/sources/

time {
tar xf m4-*.tar.xz
cd m4-*/

# Installation here
./configure --prefix=/usr\
            --host=$LFS_TGT\
            --build=$(build-aux/config.guess)
make
make DESTDIR=$LFS install
}

cd $LFS/sources/
rm -rf m4-*/
```

---
## 6.3 Ncurses install
Approximate time required: 0.35 SBU

```bash
cd $LFS/sources/

time {
tar xf ncurses-*.tar.gz
cd ncurses-*/

# Check gawk first
sed -i s/mawk// configure

mkdir build
pushd build
  ../configure
  make -C include
  make -C progs tic
popd

./configure --prefix=/usr                \
            --host=$LFS_TGT              \
            --build=$(./config.guess)    \
            --mandir=/usr/share/man      \
            --with-manpage-format=normal \
            --with-shared                \
            --without-normal             \
            --with-cxx-shared            \
            --without-debug              \
            --without-ada                \
            --disable-stripping          \
            --enable-widec
make
make DESTDIR=$LFS TIC_PATH=$(pwd)/build/progs/tic install
echo "INPUT(-lncursesw)" > $LFS/usr/lib/libncurses.so
}

cd $LFS/sources/
rm -rf ncurses-*/
```


---
## 6.4 Bash install
Approximate time required: 0.35 SBU
```bash
cd $LFS/sources/

time {
tar xf bash-*.tar.gz
cd bash-*/

# Installation here
./configure --prefix=/usr                      \
        --build=$(sh support/config.guess) \
        --host=$LFS_TGT                    \
        --without-bash-malloc
make
make DESTDIR=$LFS install
}

ln -sv bash $LFS/bin/sh

cd $LFS/sources/
rm -rf bash-*/
```


---
## 6.5 Coreutils install
Approximate time required: 0.75 SBU
```bash
cd $LFS/sources/

time {
tar xf coreutils-*.tar.xz
cd coreutils-*/

# Installation here

./configure --prefix=/usr                     \
            --host=$LFS_TGT                   \
            --build=$(build-aux/config.guess) \
            --enable-install-program=hostname \
            --enable-no-install-program=kill,uptime \
            gl_cv_macro_MB_CUR_MAX_good=y
make
make DESTDIR=$LFS install
}

mv -v $LFS/usr/bin/chroot              $LFS/usr/sbin
mkdir -pv $LFS/usr/share/man/man8
mv -v $LFS/usr/share/man/man1/chroot.1 $LFS/usr/share/man/man8/chroot.8
sed -i 's/"1"/"8"/'                    $LFS/usr/share/man/man8/chroot.8

cd $LFS/sources/
rm -rf coreutils-*/
```

---
## 6.6 Diffutils install
Approximate time required: 0.2 SBU
```bash
cd $LFS/sources/

time {
tar xf diffutils-*.tar.xz
cd diffutils-*/

# Installation here

./configure --prefix=/usr   \
        --host=$LFS_TGT \
        --build=$(./build-aux/config.guess)
make
make DESTDIR=$LFS install
}

cd $LFS/sources/
rm -rf diffutils-*/
```

---
## 6.7 File install
Approximate time required: 0.2 SBU
```bash
cd $LFS/sources/

time {
tar xf file-*.tar.gz
cd file-*/

# Installation here
mkdir build
pushd build
  ../configure --disable-bzlib      \
               --disable-libseccomp \
               --disable-xzlib      \
               --disable-zlib
  make
popd
./configure --prefix=/usr --host=$LFS_TGT --build=$(./config.guess)
make FILE_COMPILE=$(pwd)/build/src/file
make DESTDIR=$LFS install

}

rm -v $LFS/usr/lib/libmagic.la

cd $LFS/sources/
rm -rf file-*/
```

---
## 6.8 Findutils install
Approximate time required: 0.3 SBU
```bash
cd $LFS/sources/

time {
tar xf findutils-*.tar.xz
cd findutils-*/

# Installation here

./configure --prefix=/usr                   \
        --localstatedir=/var/lib/locate \
        --host=$LFS_TGT                 \
        --build=$(build-aux/config.guess)
make
make DESTDIR=$LFS install
}

cd $LFS/sources/
rm -rf findutils-*/
```

---
## 6.9 Gawk install (haha very funny)
Approximate time required: 0.25 SBU
```bash
cd $LFS/sources/

time {
tar xf gawk-*.tar.xz
cd gawk-*/

sed -i 's/extras//' Makefile.in

# Installation here
./configure --prefix=/usr   \
            --host=$LFS_TGT \
            --build=$(build-aux/config.guess)
make
make DESTDIR=$LFS install
}

cd $LFS/sources/
rm -rf gawk-*/
```

---
## 6.10 Grep install
Approximate time required: 0.2 SBU
```bash
cd $LFS/sources/

time {
tar xf grep-*.tar.xz
cd grep-*/

# Installation here

./configure --prefix=/usr   \
        --host=$LFS_TGT \
        --build=$(./build-aux/config.guess)
make
make DESTDIR=$LFS install
}

cd $LFS/sources/
rm -rf grep-*/
```

---
## 6.11 Gzip install
Approximate time required: 0.15 SBU
```bash
cd $LFS/sources/

time {
tar xf gzip-*.tar.xz
cd gzip-*/

# Installation here
./configure --prefix=/usr --host=$LFS_TGT
make
make DESTDIR=$LFS install
}

cd $LFS/sources/
rm -rf gzip-*/
```

---
## 6.12 Make install
Approximate time required: 0.1 SBU
```bash
cd $LFS/sources/

time {
tar xf make-*.tar.gz
cd make-*/

# Installation here
./configure --prefix=/usr   \
        --without-guile \
        --host=$LFS_TGT \
        --build=$(build-aux/config.guess)
make
make DESTDIR=$LFS install
}


cd $LFS/sources/
rm -rf make-*/
```

---
## 6.13 Patch install
Approximate time required: 0.17 SBU
```bash
cd $LFS/sources/

time {
tar xf patch-*.tar.xz
cd patch-*/

# Installation here
./configure --prefix=/usr   \
        --host=$LFS_TGT \
        --build=$(build-aux/config.guess)
make
make DESTDIR=$LFS install
}

cd $LFS/sources/
rm -rf patch-*/
```

---
## 6.14 Sed install
Approximate time required: 0.2 SBU
```bash
cd $LFS/sources/

time {
tar xf sed-*.tar.xz
cd sed-*/

# Installation here
./configure --prefix=/usr   \
        --host=$LFS_TGT \
        --build=$(./build-aux/config.guess)
make
make DESTDIR=$LFS install
}

cd $LFS/sources/
rm -rf sed-*/
```

---
## 6.15 Tar install
Approximate time required: 0.3 SBU
```bash
cd $LFS/sources/

time {
tar xf tar-*.tar.xz
cd tar-*/

# Installation here
./configure --prefix=/usr   \
        --host=$LFS_TGT \
        --build=$(build-aux/config.guess)
make
make DESTDIR=$LFS install
}

cd $LFS/sources/
rm -rf tar-*/
```

---
## 6.16 Xz install
Approximate time required: 0.2 SBU
```bash
cd $LFS/sources/

time {
tar xf xz-*.tar.xz
cd xz-*/

# Installation here
./configure --prefix=/usr                 \
        --host=$LFS_TGT                   \
        --build=$(build-aux/config.guess) \
        --disable-static                  \
        --docdir=/usr/share/doc/xz-5.44
make
make DESTDIR=$LFS install
}

rm -v $LFS/usr/lib/liblzma.la

cd $LFS/sources/
rm -rf xz-*/
```

---
## 6.17 Binutils pass 2 install
Approximate time required: 1.3 SBU
```bash
cd $LFS/sources/

time {
tar xf binutils-*.tar.xz
cd binutils-*/

# Fix an issue with sysroot support
sed '6009s/$add_dir//' -i ltmain.sh

# Installation here
mkdir -v build
cd       build

../configure                   \
    --prefix=/usr              \
    --build=$(../config.guess) \
    --host=$LFS_TGT            \
    --disable-nls              \
    --enable-shared            \
    --enable-gprofng=no        \
    --disable-werror           \
    --enable-64-bit-bfd
make
make DESTDIR=$LFS install
}

# Remove the libtool archive files
rm -v $LFS/usr/lib/lib{bfd,ctf,ctf-nobfd,opcodes,sframe}.{a,la}

cd $LFS/sources/
rm -rf binutils-*/
```

---
## 6.18 Gcc pass 2 install
Approximate time required: 11.3 SBU
```bash
cd $LFS/sources/

time {
tar xf gcc-*.tar.xz
cd gcc-*/

# additional required packages
tar -xf ../mpfr-4.2.0.tar.xz
mv -v mpfr-4.2.0 mpfr
tar -xf ../gmp-6.3.0.tar.xz
mv -v gmp-6.3.0 gmp
tar -xf ../mpc-1.3.1.tar.gz
mv -v mpc-1.3.1 mpc

# 64 bit lib name
case $(uname -m) in
  x86_64)
    sed -e '/m64=/s/lib64/lib/' -i.orig gcc/config/i386/t-linux64
  ;;
esac

sed '/thread_header =/s/@.*@/gthr-posix.h/' \
    -i libgcc/Makefile.in libstdc++-v3/include/Makefile.in

# Installation here
mkdir -v build
cd       build

../configure                                       \
    --build=$(../config.guess)                     \
    --host=$LFS_TGT                                \
    --target=$LFS_TGT                              \
    LDFLAGS_FOR_TARGET=-L$PWD/$LFS_TGT/libgcc      \
    --prefix=/usr                                  \
    --with-build-sysroot=$LFS                      \
    --enable-default-pie                           \
    --enable-default-ssp                           \
    --disable-nls                                  \
    --disable-multilib                             \
    --disable-libatomic                            \
    --disable-libgomp                              \
    --disable-libquadmath                          \
    --disable-libsanitizer                         \
    --disable-libssp                               \
    --disable-libvtv                               \
    --enable-languages=c,c++
make
make DESTDIR=$LFS install
}

ln -sv gcc $LFS/usr/bin/cc

cd $LFS/sources/
rm -rf gcc-*/
```