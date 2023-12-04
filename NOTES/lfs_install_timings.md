Timings for builds + compiles + installs\
These times generally use 4 cores\
[Detailed spreadsheet here](https://docs.google.com/spreadsheets/d/1dpSewOUg6HXRobud6-Sv85p0DvN5E9N_i-0j1y3u6lA/edit?usp=sharing)

### Chapter 5 install times
| Package | Time in seconds<br>(approx.) | Time in SBU<br>(approx.) |
|-|-:|-:|
| binutils-pass1   |  67.992 |    1 |
| gcc-pass1        | 551.705 | 8.11 |
| linux-api        |  28.946 | 0.43 |
| glibc            | 262.920 | 3.87 |
| libstdc++        |  53.561 | 0.79 |
|
| One-by-one total | 965.124 | 14.2 |

### Chapter 6 install times
| Package | Time in seconds<br>(approx.) | Time in SBU<br>(approx.) |
|-|-:|-:
| m4               |   33.602 |  0.49 |
| ncurses          |    66.14 |  0.97 |
| bash             |   36.396 |  0.54 |
| coreutils        |   75.348 |  1.11 |
| diffutils        |   26.231 |  0.39 |
| file             |   22.117 |  0.33 |
| findutils        |    40.01 |  0.59 |
| gawk             |   26.958 |   0.4 |
| grep             |   27.306 |   0.4 |
| gzip             |   20.273 |   0.3 |
| make             |   11.347 |  0.17 |
| patch            |   26.502 |  0.39 |
| sed              |   23.113 |  0.34 |
| tar              |   34.875 |  0.51 |
| xz               |    19.36 |  0.28 |
| binutils-pass2   |   84.509 |  1.24 |
| gcc-pass2        |  871.719 | 12.82 |
|
| One-by-one total | 1480.354 | 21.78 |
| All-in-one       | 1250.757 | 18.40 |

### Chapter 7 install times
| Package | Time in seconds<br>(approx.) | Time in SBU<br>(approx.) |
|-|-:|-:
| gettext           | 186.417 | 2.74 |
| bison             |  33.221 | 0.49 |
| perl              | 112.634 | 1.66 |
| python            |  95.915 | 1.41 |
| texinfo           |  34.424 | 0.51 |
| util-linux        |  52.214 | 0.77 |
|
| One-by-one total  | 514.825 | 7.58 |
| All-in-one        | 515.815 | 7.59 |

Backup | Time in seconds<br>(approx.) | Time in SBU<br>(approx.)
-|-:|-:
LFS (1 core)        | 973.008 | 14.31 |
LFS (4 core)        | 316.121 | 4.65  |



### Chapter 8 install times
Package | Time in seconds<br>(approx.) | Time in SBU<br>(approx.)
-|-:|-:
| man-pages            |   10.045 |   0.15 |
| iana-etc             |    0.033 |     <0 |
| glibc                | 3586.912 |  52.75 |
| zlib                 |    2.324 |   0.03 |
| bzip2                |    3.124 |   0.05 |
| xz                   |   22.343 |   0.33 |
| zstd                 |   73.283 |   1.08 |
| file                 |   12.044 |   0.18 |
| readline             |    8.284 |   0.12 |
| m4                   |   61.831 |   0.91 |
| bc                   |     7.37 |   0.11 |
| flex                 |   23.504 |   0.35 |
| tcl                  |  340.937 |   5.01 |
| expect               |   23.058 |   0.34 |
| dejagnu              |    9.906 |   0.15 |
| binutils             |  535.618 |   7.88 |
| gmp                  |   74.505 |    1.1 |
| mpfr                 |   51.656 |   0.76 |
| mpc                  |   21.846 |   0.32 |
| attr                 |    7.851 |   0.12 |
| acl                  |    7.563 |   0.11 |
| libcap               |    2.838 |   0.04 |
| libxcrypt            |   22.654 |   0.33 |
| shadow               |   20.294 |    0.3 |
| gcc                  | 7738.411 | 113.81 |
| pkgconf              |    4.871 |   0.07 |
| ncurses              |   39.131 |   0.58 |
| sed                  |   48.528 |   0.71 |
| psmisc               |   10.503 |   0.15 |
| gettext              |  313.355 |   4.61 |
| bison                |  405.187 |   5.96 |
| grep                 |   66.739 |   0.98 |
| bash                 |  151.824 |   2.23 |
| libtool              |  369.741 |   5.44 |
| gdbm                 |   13.175 |   0.19 |
| gperf                |    5.358 |   0.08 |
| expat                |   11.792 |   0.17 |
| inetutils            |   45.241 |   0.67 |
| less                 |    9.722 |   0.14 |
| perl                 |  950.676 |  13.98 |
| xml::parser          |    2.551 |   0.04 |
| intltool             |    2.948 |   0.04 |
| autoconf             |  362.146 |   5.33 |
| automake             | 1111.009 |  16.34 |
| openssl              |  438.945 |   6.46 |
| kmod                 |    9.158 |   0.13 |
| libelf-from-elfutils |   55.345 |   0.81 |
| libffi               |  218.656 |   3.22 |
| python               |  252.338 |   3.71 |
| flit-core            |    0.817 |   0.01 |
| wheel                |     0.81 |   0.01 |
| ninja                |   43.947 |   0.65 |
| meson                |    2.185 |   0.03 |
| coreutils            |  214.484 |   3.15 |
| check                |  187.648 |   2.76 |
| diffutils            |   51.931 |   0.76 |
| gawk                 |   31.149 |   0.46 |
| findutils            |   98.685 |   1.45 |
| groff                |   37.159 |   0.55 |
| grub                 |    64.98 |   0.96 |
| gzip                 |   41.741 |   0.61 |
| iproute2             |   11.212 |   0.16 |
| kbd                  |   17.931 |   0.26 |
| libpipeline          |   19.383 |   0.29 |
| make                 |   69.676 |   1.02 |
| patch                |   31.651 |   0.47 |
| tar                  |  247.399 |   3.64 |
| texinfo              |   62.678 |   0.92 |
| vim                  |  296.294 |   4.36 |
| markupsafe           |    2.217 |   0.03 |
| jinja2               |    1.137 |   0.02 |
| udev-from-systemd    |   36.994 |   0.54 |
| man-db               |    47.11 |   0.69 |
| procps-ng            |   19.008 |   0.28 |
| util-linux           |   96.546 |   1.42 |
| e2fsprogs            |    67.32 |   0.99 |
| sysklogd             |    0.481 |   0.01 |
| sysvinit             |    1.454 |   0.02 |
|
| Total                | 19371.2  | 284.89 |


### Total time wasted
|Chapter | Time in seconds<br>(approx.) | Time in SBU<br>(approx.)
|-|-:|-:
| Chapter 5         |  1125.647 |  16.57 |
| Chapter 6         |  1250.757 |  18.40 |
| Chapter 7         |   831.936 |  12.24 |
| Chapter 8.0-8.5   |  3596.99  |  52.9  |
| Chapter 8.6-8.26  |  1332.833 |  19.62 |
| Chapter 8.27(gcc) |  7738.411 | 113.81 |
| Chapter 8.28-8.46 |  3924.497 |  57.71 |
| Chapter 8.47-8.80 |  1749.978 |  25.73 |
| Chapter 8.81-8.83 |  1028.491 |  15.12 |
|
| Total             | 22460.845 | 330.34 |