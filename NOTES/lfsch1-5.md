#### Preface:
hopefully this works lol good luck\
tip: you can log in as all 3 accounts at once

## CHAPTER 2: Preparing the Host System
#### Run as `user` and `root`

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

## CHAPTER 3: Packages and Patches
#### Run as `root`

Set parallel make using 4 cores
```bash
export MAKEFLAGS='-j4'
```

#### Run as `root`
Create sources directory and package download ([from aos](https://osp4diss.vlsm.org/W08-03.html))
```bash
if [[ "$(id -u)" == "0" ]] ; then
    echo "============================================"
    echo "LFS should be /mnt/lfs AND MAKEFLAGS = cores"
    echo "LFS=$LFS MAKEFLAGS=$MAKEFLAGS"
    echo "============================================"
    sleep 1
    mkdir -pv $LFS/sources/
    chmod -v  a+wt $LFS/sources/
    cd        $LFS/sources/
    wget -c   https://www.linuxfromscratch.org/lfs/view/12.0/wget-list-sysv --directory-prefix=$LFS/sources
    wget -c   --input-file=$LFS/sources/wget-list-sysv --directory-prefix=$LFS/sources
    wget -c   https://www.linuxfromscratch.org/lfs/view/12.0/md5sums --directory-prefix=$LFS/sources
    md5sum -c md5sums
    chown root:root $LFS/sources/*
else
    echo "=== === === === ERROR: ROOT ONLY === === === ERROR ==="
    echo "=== === === === ERROR: ROOT ONLY === === === ERROR ==="
    echo "=== === === === ERROR: ROOT ONLY === === === ERROR ==="
fi
```

> Make sure files “wget-list-sysv” and “md5sums” are in $LFS/sources/
```bash
ls -al $LFS/sources/{md5sums,wget-list-sysv}
# -rw-r--r-- 1 root root 5130 Sep  1 23:00 /mnt/lfs/sources/md5sums
# -rw-r--r-- 1 root root 5932 Sep  1 23:00 /mnt/lfs/sources/wget-list-sysv
```

## CHAPTER 4: Final Preparations
#### Run as `root`

Create the required directory layout
```bash
mkdir -pv $LFS/{etc,var} $LFS/usr/{bin,lib,sbin}

for i in bin lib sbin; do
  ln -sv usr/$i $LFS/$i
done

case $(uname -m) in
  x86_64) mkdir -pv $LFS/lib64 ;;
esac

mkdir -pv $LFS/tools
```

Create a new account `lfs` and input the password of `lfs`
```bash
groupadd lfs
useradd -s /bin/bash -g lfs -m -k /dev/null lfs
passwd lfs
```

Grant `lfs` full access to all the directories under $LFS by making `lfs` the owner
```bash
chown -v lfs $LFS/{usr{,/*},lib,var,etc,bin,sbin,tools}
case $(uname -m) in
  x86_64) chown -v lfs $LFS/lib64 ;;
esac
```


#### Run as `lfs`

`lfs` bash settings
```bash
cat > ~/.bash_profile << "EOF"
exec env -i HOME=$HOME TERM=$TERM PS1='\u:\w\$ ' /bin/bash
EOF
cat > ~/.bashrc << "EOF"
set +h
umask 022
LFS=/mnt/lfs
LC_ALL=POSIX
LFS_TGT=$(uname -m)-lfs-linux-gnu
PATH=/usr/bin
if [ ! -L /bin ]; then PATH=/bin:$PATH; fi
PATH=$LFS/tools/bin:$PATH
CONFIG_SITE=$LFS/usr/share/config.site
export LFS LC_ALL LFS_TGT PATH CONFIG_SITE
EOF
```

Ensure the environment is fully prepared\
Force the bash shell to read the new user profile
```bash
source ~/.bash_profile
```

## CHAPTER 5: Compiling a Cross-Toolchain
NOTE: This section is available with logging enabled [here](./le_fisch_5_with_log.md).

### Binutils install (Pass 1)
#### Run as `lfs`
Approximate time required: 1 SBU\
(~2m35s on my laptop)
```bash
cd $LFS/sources/

tar xfv binutils-*.tar.xz
cd binutils-*/

mkdir -v build
cd       build

time {
  ../configure --prefix=$LFS/tools \
      --with-sysroot=$LFS \
      --target=$LFS_TGT   \
      --disable-nls       \
      --enable-gprofng=no \
      --disable-werror;
  make;
  make install;
}
echo "I am $(whoami); using $(uname -r) with $(nproc) cores."

cd $LFS/sources/
rm -rf binutils-*/
```

---
### GCC install (Intel x64 only)
Don't delete source, later used to install libstdc++\
Approximate time required: 9.8 SBU
```bash
cd $LFS/sources/

tar xfv gcc-*.tar.xz
cd gcc-*/

tar -xf ../mpfr-4.2.0.tar.xz
mv -v mpfr-4.2.0 mpfr
tar -xf ../gmp-6.3.0.tar.xz
mv -v gmp-6.3.0 gmp
tar -xf ../mpc-1.3.1.tar.gz
mv -v mpc-1.3.1 mpc

case $(uname -m) in
  x86_64)
    sed -e '/m64=/s/lib64/lib/' \
        -i.orig gcc/config/i386/t-linux64
 ;;
esac

mkdir -v build
cd       build

time {
  ../configure                  \
      --target=$LFS_TGT         \
      --prefix=$LFS/tools       \
      --with-glibc-version=2.38 \
      --with-sysroot=$LFS       \
      --with-newlib             \
      --without-headers         \
      --enable-default-pie      \
      --enable-default-ssp      \
      --disable-nls             \
      --disable-shared          \
      --disable-multilib        \
      --disable-threads         \
      --disable-libatomic       \
      --disable-libgomp         \
      --disable-libquadmath     \
      --disable-libssp          \
      --disable-libvtv          \
      --disable-libstdcxx       \
      --enable-languages=c,c++;
  make;
  make install;
}

cd ..
cat gcc/limitx.h gcc/glimits.h gcc/limity.h > \
  `dirname $($LFS_TGT-gcc -print-libgcc-file-name)`/include/limits.h
  
rm -rf build/
```


---
### Linux API headers install
Approximate time required: ~0.2 SBU
```bash
cd $LFS/sources/

tar xfv linux-*.tar.xz
cd linux-*/

time {
  make mrproper;
  make headers;
  find usr/include -type f ! -name '*.h' -delete;
  cp -rv usr/include $LFS/usr;
}

cd $LFS/sources/
rm -rf linux-*/
```

---
### glibc install
Approximate time required: 4.2 SBU
```bash
cd $LFS/sources/

tar xfv glibc-*.tar.xz
cd glibc-*/

case $(uname -m) in
  i?86)   ln -sfv ld-linux.so.2 $LFS/lib/ld-lsb.so.3
  ;;
  x86_64) ln -sfv ../lib/ld-linux-x86-64.so.2 $LFS/lib64
          ln -sfv ../lib/ld-linux-x86-64.so.2 $LFS/lib64/ld-lsb-x86-64.so.3
  ;;
esac

patch -Np1 -i ../glibc-2.38-fhs-1.patch

mkdir -v build
cd       build
echo "rootsbindir=/usr/sbin" > configparms

time {
  ../configure                           \
      --prefix=/usr                      \
      --host=$LFS_TGT                    \
      --build=$(../scripts/config.guess) \
      --enable-kernel=4.14               \
      --with-headers=$LFS/usr/include    \
      libc_cv_slibdir=/usr/lib;
  # compile and install
  make;
	make DESTDIR=$LFS install;
}

sed '/RTLDLIST=/s@/usr@@g' -i $LFS/usr/bin/ldd
```

glibc test
```bash
echo 'int main(){}' | $LFS_TGT-gcc -xc -
readelf -l a.out | grep ld-linux
rm -v a.out
# Expected output:
# [Requesting program interpreter: /lib64/ld-linux-x86-64.so.2]
```
    
delete glibc source
```bash
cd $LFS/sources/
rm -rf glibc-*/
```

---

### libstdc++ install
Approximate time required: 0.5 SBU\
(in gcc)
```bash
if [ ! -d $LFS/sources/gcc-*/ ]; then
    echo "GCC source not found. Extracting..."
    cd $LFS/sources/
    tar xfv gcc-*.tar.xz
fi
cd $LFS/sources/gcc-*/
mkdir -v build
cd       build

time {
    ../libstdc++-v3/configure           \
        --host=$LFS_TGT                 \
        --build=$(../config.guess)      \
        --prefix=/usr                   \
        --disable-multilib              \
        --disable-nls                   \
        --disable-libstdcxx-pch         \
        --with-gxx-include-dir=/tools/$LFS_TGT/include/c++/13.2.0;
    make;
    make DESTDIR=$LFS install;
}

rm -v $LFS/usr/lib/lib{stdc++,stdc++fs,supc++}.la

cd $LFS/sources/
```


## FINISHING: bash script
#### Run as `user` (your github account)
```bash
bash $HOME/mywork/WEEK08/08-WEEK08.sh
bash $HOME/git/os232/TXT/myscript.sh
```