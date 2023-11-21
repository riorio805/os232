# The all in one install script for chapter 6
# IMPORTANT: Run this script as `lfs` and make sure $LFS is set
# Just CTRL+A, CTRL+C, CTRL+V, or bash it
# Output time will be total time for all scripts
# Approximate time required: 16.6 SBU
cd $LFS/sources/

time {
for i in {m4,ncurses,bash,coreutils,diffutils,file,findutils,gawk,grep,gzip,make,patch,sed,tar,xz,binutils,gcc}; do
    tar xfv $i-*.tar.*
done

cd $LFS/sources/m4-*/
./configure --prefix=/usr\
            --host=$LFS_TGT\
            --build=$(build-aux/config.guess)
make
make DESTDIR=$LFS install

cd $LFS/sources/ncurses-*/
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

cd $LFS/sources/bash-*/
./configure --prefix=/usr                      \
            --build=$(sh support/config.guess) \
            --host=$LFS_TGT                    \
            --without-bash-malloc
make
make DESTDIR=$LFS install
ln -sv bash $LFS/bin/sh

cd $LFS/sources/coreutils-*/
./configure --prefix=/usr                     \
            --host=$LFS_TGT                   \
            --build=$(build-aux/config.guess) \
            --enable-install-program=hostname \
            --enable-no-install-program=kill,uptime \
            gl_cv_macro_MB_CUR_MAX_good=y
make
make DESTDIR=$LFS install
mv -v $LFS/usr/bin/chroot              $LFS/usr/sbin
mkdir -pv $LFS/usr/share/man/man8
mv -v $LFS/usr/share/man/man1/chroot.1 $LFS/usr/share/man/man8/chroot.8
sed -i 's/"1"/"8"/'                    $LFS/usr/share/man/man8/chroot.8

cd $LFS/sources/diffutils-*/
./configure --prefix=/usr   \
            --host=$LFS_TGT \
            --build=$(./build-aux/config.guess)
make
make DESTDIR=$LFS install

cd $LFS/sources/file-*/
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
rm -v $LFS/usr/lib/libmagic.la

cd $LFS/sources/findutils-*/
./configure --prefix=/usr                   \
            --localstatedir=/var/lib/locate \
            --host=$LFS_TGT                 \
            --build=$(build-aux/config.guess)
make
make DESTDIR=$LFS install

cd $LFS/sources/gawk-*/
sed -i 's/extras//' Makefile.in

cd $LFS/sources/grep-*/
./configure --prefix=/usr   \
            --host=$LFS_TGT \
            --build=$(./build-aux/config.guess)
make
make DESTDIR=$LFS install

cd $LFS/sources/gzip-*/
./configure --prefix=/usr --host=$LFS_TGT
make
make DESTDIR=$LFS install

cd $LFS/sources/make-*/
./configure --prefix=/usr   \
            --without-guile \
            --host=$LFS_TGT \
            --build=$(build-aux/config.guess)
make
make DESTDIR=$LFS install

cd $LFS/sources/patch-*/
./configure --prefix=/usr   \
            --host=$LFS_TGT \
            --build=$(build-aux/config.guess)
make
make DESTDIR=$LFS install

cd $LFS/sources/sed-*/
./configure --prefix=/usr   \
            --host=$LFS_TGT \
            --build=$(./build-aux/config.guess)
make
make DESTDIR=$LFS install

cd $LFS/sources/tar-*/
./configure --prefix=/usr   \
            --host=$LFS_TGT \
            --build=$(build-aux/config.guess)
make
make DESTDIR=$LFS install

cd $LFS/sources/xz-*/
./configure --prefix=/usr                 \
            --host=$LFS_TGT                   \
            --build=$(build-aux/config.guess) \
            --disable-static                  \
            --docdir=/usr/share/doc/xz-5.44
make
make DESTDIR=$LFS install
rm -v $LFS/usr/lib/liblzma.la

cd $LFS/sources/binutils-*/
sed '6009s/$add_dir//' -i ltmain.sh
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
rm -v $LFS/usr/lib/lib{bfd,ctf,ctf-nobfd,opcodes,sframe}.{a,la}

cd $LFS/sources/gcc-*/
tar -xf ../mpfr-4.2.0.tar.xz
mv -v mpfr-4.2.0 mpfr
tar -xf ../gmp-6.3.0.tar.xz
mv -v gmp-6.3.0 gmp
tar -xf ../mpc-1.3.1.tar.gz
mv -v mpc-1.3.1 mpc
case $(uname -m) in
  x86_64)
    sed -e '/m64=/s/lib64/lib/' -i.orig gcc/config/i386/t-linux64
  ;;
esac
sed '/thread_header =/s/@.*@/gthr-posix.h/' \
    -i libgcc/Makefile.in libstdc++-v3/include/Makefile.in
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
ln -sv gcc $LFS/usr/bin/cc

cd $LFS/sources/
for i in {m4,ncurses,bash,coreutils,diffutils,file,findutils,gawk,grep,gzip,make,patch,sed,tar,xz,binutils,gcc}; do
    rm -rf $LFS/sources/$i-*/
done
}