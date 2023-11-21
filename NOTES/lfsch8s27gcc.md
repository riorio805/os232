Please prepare at least 5 hours or else\
Otherwise good luck :grinning::grinning::grinning:


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
and enter chroot environment
```bash


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

## 8.0.B Backup
Leave the chroot environment to get to root\
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
time {
    tar -cJpvf $HOME/lfs-temp-tools-12.0.tar.xz .;
}
cd
```
Mount virtual file systems 
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


## 8.27P Performance tips
Some performance tips to hop
### 8.27P.A Check for multicore usage
Using a different user logged in to the same host, run `top` and press `1`\
On the top, it will show CPU usage for each of the cores\
Make sure all cores are running.\
If not, either run
```bash
export MAKEFLAGS='-j4'
```
or replace
```bash
su tester -c "PATH=$PATH make -k check"
```
with
```bash
su tester -c "PATH=$PATH make -j4 -k check"
```


---
## 8.27 GCC install

### 8.27.1 Compile and run tests
Approximate time required: x SBU
```bash
cd /sources/

time {
tar xf gcc-*.tar.*
cd gcc-*/

case $(uname -m) in
  x86_64)
    sed -e '/m64=/s/lib64/lib/' \
        -i.orig gcc/config/i386/t-linux64
  ;;
esac

mkdir -v build
cd       build

../configure --prefix=/usr            \
             LD=ld                    \
             --enable-languages=c,c++ \
             --enable-default-pie     \
             --enable-default-ssp     \
             --disable-multilib       \
             --disable-bootstrap      \
             --disable-fixincludes    \
             --with-system-zlib

make
ulimit -s 32768
chown -Rv tester .
su tester -c "PATH=$PATH make -k check"
../contrib/test_summary | grep '^FAIL:'
}
```
Expected output of `test_summary | grep ...`
```
FAIL: g++.dg/asan/asan_test.C   -O2  AddressSanitizer_StrtollOOBTest Strtol(array + 3, NULL, 0) execution test
FAIL: g++.dg/asan/asan_test.C   -O2  AddressSanitizer_StrtollOOBTest Strtol(array - 1, NULL, 0) execution test
FAIL: g++.dg/asan/asan_test.C   -O2  AddressSanitizer_StrtollOOBTest Strtol(array, NULL, 0) execution test
FAIL: g++.dg/asan/asan_test.C   -O2  AddressSanitizer_StrtollOOBTest Strtol(array, NULL, 36) execution test
FAIL: g++.dg/asan/asan_test.C   -O2  AddressSanitizer_StrtollOOBTest Strtol(array, NULL, 0) execution test
FAIL: g++.dg/asan/asan_test.C   -O2  AddressSanitizer_StrtollOOBTest Strtol(array, NULL, 0) execution test
FAIL: g++.dg/asan/asan_test.C   -O2  AddressSanitizer_StrtollOOBTest Strtol(array, NULL, 0) execution test
FAIL: g++.dg/asan/asan_test.C   -O2  AddressSanitizer_StrtolOOBTest Strtol(array + 3, NULL, 0) execution test
FAIL: g++.dg/asan/asan_test.C   -O2  AddressSanitizer_StrtolOOBTest Strtol(array - 1, NULL, 0) execution test
FAIL: g++.dg/asan/asan_test.C   -O2  AddressSanitizer_StrtolOOBTest Strtol(array, NULL, 0) execution test
FAIL: g++.dg/asan/asan_test.C   -O2  AddressSanitizer_StrtolOOBTest Strtol(array, NULL, 36) execution test
FAIL: g++.dg/asan/asan_test.C   -O2  AddressSanitizer_StrtolOOBTest Strtol(array, NULL, 0) execution test
FAIL: g++.dg/asan/asan_test.C   -O2  AddressSanitizer_StrtolOOBTest Strtol(array, NULL, 0) execution test
FAIL: g++.dg/asan/asan_test.C   -O2  AddressSanitizer_StrtolOOBTest Strtol(array, NULL, 0) execution test
FAIL: g++.dg/asan/interception-malloc-test-1.C   -O0  execution test
FAIL: g++.dg/asan/interception-malloc-test-1.C   -O1  execution test
FAIL: g++.dg/asan/interception-malloc-test-1.C   -O2  execution test
FAIL: g++.dg/asan/interception-malloc-test-1.C   -O3 -g  execution test
FAIL: g++.dg/asan/interception-malloc-test-1.C   -Os  execution test
FAIL: g++.dg/asan/interception-malloc-test-1.C   -O2 -flto -fno-use-linker-plugin -flto-partition=none  execution test
FAIL: g++.dg/asan/interception-malloc-test-1.C   -O2 -flto -fuse-linker-plugin -fno-fat-lto-objects  execution test
FAIL: gcc.dg/analyzer/data-model-4.c (test for excess errors)
FAIL: gcc.dg/analyzer/torture/conftest-1.c   -O0  (test for excess errors)
FAIL: gcc.dg/analyzer/torture/conftest-1.c   -O1  (test for excess errors)
FAIL: gcc.dg/analyzer/torture/conftest-1.c   -O2  (test for excess errors)
FAIL: gcc.dg/analyzer/torture/conftest-1.c   -O3 -g  (test for excess errors)
FAIL: gcc.dg/analyzer/torture/conftest-1.c   -Os  (test for excess errors)
FAIL: gcc.dg/analyzer/torture/conftest-1.c   -O2 -flto -fno-use-linker-plugin -flto-partition=none  (test for excess errors)
FAIL: gcc.dg/pr56837.c scan-tree-dump-times optimized "memset ..c, 68, 16384.;" 1
FAIL: 23_containers/vector/bool/allocator/copy.cc (test for excess errors)
```



### 8.27.2 Install
Approximate time required: x SBU
```bash
time {
make install
chown -v -R root:root \
    /usr/lib/gcc/$(gcc -dumpmachine)/13.2.0/include{,-fixed}
ln -svr /usr/bin/cpp /usr/lib
ln -sv gcc.1 /usr/share/man/man1/cc.1
ln -sfv ../../libexec/gcc/$(gcc -dumpmachine)/13.2.0/liblto_plugin.so \
        /usr/lib/bfd-plugins/
echo 'int main(){}' > dummy.c
cc dummy.c -v -Wl,--verbose &> dummy.log
readelf -l a.out | grep ': /lib'
grep -E -o '/usr/lib.*/S?crt[1in].*succeeded' dummy.log
grep -B4 '^ /usr/include' dummy.log
grep 'SEARCH.*/usr/lib' dummy.log |sed 's|; |\n|g'
grep "/lib.*/libc.so.6 " dummy.log
grep found dummy.log
rm -v dummy.c a.out dummy.log
mkdir -pv /usr/share/gdb/auto-load/usr/lib
mv -v /usr/lib/*gdb.py /usr/share/gdb/auto-load/usr/lib
}
cd /sources/
rm -rf gcc-*/
```
Expected output:
```
[Requesting program interpreter: /lib64/ld-linux-x86-64.so.2]
/usr/lib/gcc/x86_64-pc-linux-gnu/13.2.0/../../../../lib/Scrt1.o succeeded
/usr/lib/gcc/x86_64-pc-linux-gnu/13.2.0/../../../../lib/crti.o succeeded
/usr/lib/gcc/x86_64-pc-linux-gnu/13.2.0/../../../../lib/crtn.o succeeded
#include <...> search starts here:
 /usr/lib/gcc/x86_64-pc-linux-gnu/13.2.0/include
 /usr/local/include
 /usr/lib/gcc/x86_64-pc-linux-gnu/13.2.0/include-fixed
 /usr/include
SEARCH_DIR("/usr/x86_64-pc-linux-gnu/lib64")
SEARCH_DIR("/usr/local/lib64")
SEARCH_DIR("/lib64")
SEARCH_DIR("/usr/lib64")
SEARCH_DIR("/usr/x86_64-pc-linux-gnu/lib")
SEARCH_DIR("/usr/local/lib")
SEARCH_DIR("/lib")
SEARCH_DIR("/usr/lib");
attempt to open /usr/lib/libc.so.6 succeeded
found ld-linux-x86-64.so.2 at /usr/lib/ld-linux-x86-64.so.2
```


## Continue to next section
Next section: [8.28-8.46](lfsch8s27gcc.md)