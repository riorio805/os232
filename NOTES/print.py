named = ['Man-pages', 'Iana-Etc', 'Glibc', 'Zlib', 'Bzip2', 'Xz', 'Zstd', 'File', 'Readline', 'M4', 'Bc', 'Flex', 'Tcl', 'Expect', 'DejaGNU', 'Binutils', 'GMP', 'MPFR', 'MPC', 'Attr', 'Acl', 'Libcap', 'Libxcrypt', 'Shadow', 'GCC', 'Pkgconf', 'Ncurses', 'Sed', 'Psmisc', 'Gettext', 'Bison', 'Grep', 'Bash', 'Libtool', 'GDBM', 'Gperf', 'Expat', 'Inetutils', 'Less', 'Perl', 'XML::Parser', 'Intltool', 'Autoconf', 'Automake', 'OpenSSL', 'Kmod', 'Libelf from Elfutils', 'Libffi', 'Python', 'Flit-Core', 'Wheel', 'Ninja', 'Meson', 'Coreutils', 'Check', 'Diffutils', 'Gawk', 'Findutils', 'Groff', 'GRUB', 'Gzip', 'IPRoute2', 'Kbd', 'Libpipeline', 'Make', 'Patch', 'Tar', 'Texinfo', 'Vim', 'MarkupSafe', 'Jinja2', 'Udev from Systemd', 'Man-DB', 'Procps-ng', 'Util-linux', 'E2fsprogs', 'Sysklogd', 'Sysvinit']
lower = ['man-pages', 'iana-etc', 'glibc', 'zlib', 'bzip2', 'xz', 'zstd', 'file', 'readline', 'm4', 'bc', 'flex', 'tcl', 'expect', 'dejagnu', 'binutils', 'gmp', 'mpfr', 'mpc', 'attr', 'acl', 'libcap', 'libxcrypt', 'shadow', 'gcc', 'pkgconf', 'ncurses', 'sed', 'psmisc', 'gettext', 'bison', 'grep', 'bash', 'libtool', 'gdbm', 'gperf', 'expat', 'inetutils', 'less', 'perl', 'XML-Parser', 'intltool', 'autoconf', 'automake', 'openssl', 'kmod', 'elfutils', 'libffi', 'Python', 'flit_core', 'wheel', 'ninja', 'meson', 'coreutils', 'check', 'diffutils', 'gawk', 'findutils', 'groff', 'grub', 'gzip', 'iproute2', 'kbd', 'libpipeline', 'make', 'patch', 'tar', 'texinfo', 'vim', 'MarkupSafe', 'Jinja2', 'systemd', 'man-db', 'procps-ng', 'util-linux', 'e2fsprogs', 'sysklogd', 'sysvinit']

def str_format(idx:int):
    return f"""\
---
## 8.{idx+3} {named[idx]} install
### 8.{idx+3}.1 Compile and run tests
Approximate time required: x SBU
```bash
cd /sources/

time {{
tar xf {lower[idx]}-*.tar.*
cd {lower[idx]}-*/


}}
```
Expected summary of `make check`
```
```

### 8.{idx+3}.2 Install
Approximate time required: x SBU
```bash
time {{
make install
}}
cd /sources/
rm -rf {lower[idx]}-*/
```

"""

def str_format_ls(idx:int):
    return f"ls {lower[idx]}*\n"

with open('text.md', 'w') as file:
    file.write('\n')
    for i in range(13, len(named)):
        file.write(str_format(i))

# with open('text.txt', 'w') as file:
#     for i in range(len(named)):
#         file.write(str_format_ls(i))