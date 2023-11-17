## CHAPTER 5: Compiling a Cross-Toolchain
#### Complete log version, for debugging reasons.

### IMPORTANT
Log files are created in `$HOME/log/`.<br>
Create the log directory
```bash
if [ ! -d "$HOME/lfs-log" ]; then
    mkdir $HOME/lfs-log
fi
```
If log directory doesn't exist, the log won't be created

---
Binutils install (Pass 1)
Run as `lfs`
```bash
cd /mnt/lfs/sources/

tar xf binutils-*.tar.xz
cd binutils-*/

mkdir -v build
cd       build

time {
  ../configure --prefix=$LFS/tools \
      --with-sysroot=$LFS \
      --target=$LFS_TGT   \
      --disable-nls       \
      --enable-gprofng=no \
      --disable-werror 2>&1 | tee $HOME/log/binutils-pass1-configure.log;
  make 2>&1 | tee $HOME/log/binutils-pass1-make.log;
  make install 2>&1 | tee $HOME/log/binutils-pass1-make-install.log;
}
echo "I am $(whoami); using $(uname -r) with $(nproc) cores."

cd /mnt/lfs/sources/
rm -rf binutils-*/
```

---
GCC install (Intel x64 only)
Don't delete source, later used to install libstdc++
```bash
cd /mnt/lfs/sources/

tar xf gcc-*.tar.xz
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
        --enable-languages=c,c++ 2>&1 | tee $HOME/log/gcc-pass1-configure.log;
    make 2>&1 | tee $HOME/log/gcc-pass1-make.log;
    make install 2>&1 | tee $HOME/log/gcc-pass1-make-install.log;
}

cd ..
cat gcc/limitx.h gcc/glimits.h gcc/limity.h > \
  `dirname $($LFS_TGT-gcc -print-libgcc-file-name)`/include/limits.h
  
rm -rf build/
```


---
Linux headers install
```bash
cd /mnt/lfs/sources/

tar xf linux-*.tar.xz
cd linux-*/

time {
    make mrproper 2>&1 | tee $HOME/log/linux-make-mrproper.log;
    make headers 2>&1 | tee $HOME/log/linux-make-headers.log;
    find usr/include -type f ! -name '*.h' -delete;
    cp -rv usr/include $LFS/usr;
}

cd /mnt/lfs/sources/
rm -rf linux-*/
```

---
glibc install
```bash
cd /mnt/lfs/sources/

tar xf glibc-*.tar.xz
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
        libc_cv_slibdir=/usr/lib 2>&1 | tee $HOME/log/glibc-configure.log;
    # compile and install
    make 2>&1 | tee $HOME/log/glibc-make.log;
	make DESTDIR=$LFS install 2>&1 | tee $HOME/log/glibc-make-install.log;
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
cd /mnt/lfs/sources/
rm -rf glibc-*/
```

---


libstdc++ install (in gcc after glibc)
```bash
if [ ! -d /mnt/lfs/sources/gcc-*/ ]; then
    echo "GCC source not found. Extracting..."
    cd /mnt/lfs/sources/
    tar xf gcc-*.tar.xz
fi
cd /mnt/lfs/sources/gcc-*/
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
        --with-gxx-include-dir=/tools/$LFS_TGT/include/c++/13.2.0 2>&1 | tee $HOME/log/libstd++-configure.log;
    make 2>&1 | tee $HOME/log/libstd++-make.log;
    make DESTDIR=$LFS install 2>&1 | tee $HOME/log/libstd++-make-install.log;
}

rm -v $LFS/usr/lib/lib{stdc++,stdc++fs,supc++}.la

cd /mnt/lfs/sources/
```