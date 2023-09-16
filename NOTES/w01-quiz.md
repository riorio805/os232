## week 01
Solutions are based on either the book or some "research" (googling)<br>
Currently indefinitely incomplete.<br>
[License thing](#i-have-to-put-this-here-or-else-you-too)

## 1. 2016-1
Circle or cross: ”T” if True – ”F” if False.

**(T)** / F A service-mark is a mark to identify a service rather than a product. For example MGM (Metro-Goldwyn-Mayer) uses the sound of a lion’s roar.

T / **(F)** Regular Expression:
`^.[aiueo].[aiueo]$`
will match this following string:
`"sate satu"`
>Matches: "sate", "satu, "aaaa", "batu", "puku", etc.

T / **(F)** Free software is always free of charge.
>"Free software is a matter of liberty, not price; all users are legally free to do what they want with their copies of a free software regardless of how much is paid to obtain the program." (direct quote from wikipedia)

T / **(F)** Open Source Software is not always free of charge.
>Similarly to free software, OSS is not neccesarily free of charge.

T / **(F)** There are many Free Software licenses, however, there is only one copyleft license, i.e. the GNU / General Public Licenses.
>see FAL (Free Art License)

T / **(F)** The output of script:
`echo \a b c d" | echo \a b c d"`
is
```
a b c d
a b c d
```
>Actual output: `a b c d | echo \a b c d`

T / **(F)** The output of script:
```
for II in A B C
do
echo X$II
done
```
is
```
A
B
C
```
>Actual output:
>```
>XA
>XB
>XC
>```

---
## 2. 2016-2a
Circle or cross: ”T” if True – ”F” if False.

T / F EULA (End User License Agreement) is an example of a non-free software license.
> I don't know what this question is

**(T)** / F You don’t own the propriety software you have bought.
> Yep

T / **(F)** Public Domain software is not Free Software.
> It is, No copyright => users can do whatever they want

**(T)** / F Free Software is not always Copy-left.
> Public domain is free software, but it allows anyone to convert it to proprietary software.

T / **(F)** `[ˆc]at` matches all strings matched by ` at` except `cat`.
> `.at`, not ` at`.

**(T)** / F `[a-z0-9]` matches any single letter or any single digit.
> Yes

---
## 3. 2016-2b
These following are some scripting examples. Fill remaining empty ”output” cells.
|Script (date=19 Oct 2016)|Output|
|-----|-----|
|`echo "1 2 3 4 5" \| awk '{print $1 " " $5}'`|`1 5`|
|`date +"%d %b %Y"`|`19 Oct 2016`|
|`echo \abc" \| tr '[a-z]' '[A-Z]'`|??? doesn't output anything|
|`echo 0123456789 \| cut -c5-9`|`45678`|
|<pre>VAR="hallo"<br>case "$VAR" in<br>  hallo) echo "Hallo too!"<br>        ;;<br>  *)     echo "What?"<br>        ;;<br>esac<br>exit 0</pre>|`Hallo too!`|
|`date +"%d %b %Y" \| awk '{print $2 " " $1 ", " $3}'`|`Oct 19, 2016`|
|<pre>ID="VWXYZ"<br>echo "$ID" \| cut -c1-3 \| tr ’[a-z]’ ’[A-Z]’</pre>|`VWX`|
|<pre>VAR="hello"<br>case "$VAR" in<br>  hallo) echo "Hallo too!"<br>        ;;<br>  *)     echo "What?"<br>        ;;<br>esac<br>exit 0</pre>|`What?`|

---
## 2017-1
Circle or cross: ”T” if True – ”F” if False.

T / **(F)** According to the Free Software Movement, free software developers should never be paid.
> "[...] if you are redistributing copies of free software, you might as well charge a substantial fee and *make some money*. Redistributing free software is a good and legitimate activity; if you do it, you might as well make a profit from it." (https://www.gnu.org/philosophy/selling.html)

T / **(F)** Free Software never has a license
> Copyleft: ...

T / **(F)** The Open Source Initiative (OSI) agrees with the Free Software Foundation (FSF) about how to promote the (Free or Open Source) software.
> "Like the FSF, the OSI’s founders supported the development and distribution of free software, but they disagreed with the FSF about how to promote it, believing that software freedom was primarily a practical issue rather than an ideological one" ([source](https://opensource.org/faq/#free-software))

**(T)** / F Both Free Software Licenses and Open Source Licenses may not discriminate against anyone. Giving everyone freedom means giving evil people freedom, too.

T / **(F)** The Free Software Movement hates Microsoft and consider it the Great Satan.
> ?????? who wrote this lol (see [this article](https://www.gnu.org/philosophy/microsoft.en.html) for answer)

**(T)** / F Copyleft is method to keep a free-software – and its modification – to be free.
> It is

**(T)** / F Most free software projects are developed by a single developer (or with no contributor).
> "More than half of these free software projects—and even most projects that have made several successful releases and been downloaded frequently, are the work of a single developer with little outside help." ([source](https://www.gnu.org/philosophy/when-free-software-isnt-practically-superior.en.html))


---
### I have to put this here or else (you too)
BinKadal, Sdn. Bhd. (editor)<br>
© 2016 - 2022 — Rev: 43 – 27-Oct-2022. URL: https://rms46.vlsm.org/2/196.pdf. Kumpulan soal ujian lainnya dapat diakses melalui URL: https://os.vlsm.org/. Silakan mengubah, memperbanyak, serta mendistribusikan dokumen ini selama tidak menghapus ketentuan ini!

Personal modifications:<br>
Most code blocks are like `this` instead of "this"<br>
Some questions omitted for similarity to previous questions.<br>