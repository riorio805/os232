# The all in one install script for chapter 7.7 - 7.12
# IMPORTANT: Run this script in `chroot` environment
# Just CTRL+A, CTRL+C, CTRL+V
# Output time will be total time for all scripts
# Approximate time required: 16.6 SBU
cd /sources/

time {
for i in gettext bison perl Python texinfo util-linux; do
    tar xfv $i-*.tar.*
done

cd gettext-*/
./configure --disable-shared
make
cp -v gettext-tools/src/{msgfmt,msgmerge,xgettext} /usr/bin

cd bison-*/
./configure --prefix=/usr \
        --docdir=/usr/share/doc/bison-3.8.2;
make
make install

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

cd Python-*/
./configure --prefix=/usr   \
        --enable-shared \
        --without-ensurepip
make
make install

cd texinfo-*/
./configure --prefix=/usr
make
make install

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

cd /sources/
for i in gettext bison perl Python texinfo util-linux; do
    rm -rf $LFS/sources/$i-*/
done
}