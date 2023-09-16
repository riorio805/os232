## week 02
Solutions are based on either the book, experimentation, or some "research" (googling)<br>
Currently incomplete.<br>
[License thing](#i-have-to-put-this-here-or-else-you-too)

time: 130

## 2016-1
Circle or cross: ”T” if True – ”F” if False.

T / **(F)** Principle of least privilege: programs, users and systems should be given unlimited privileges to perform their tasks.
> “The principle of least privilege. Every program and every privileged user of the system should operate using the least amount of privilege necessary to complete the job.”— Jerome H. Saltzer, describing a design principle of the Multics operating system in 1974 (ch16.2 p627)

**(T)** / F Computer system objects may be hardware or software.
> "Computer systems contain objects that must be protected from misuse. Objects may be hardware (such as memory, CPU time, and I/O devices) or software (such as files, programs, and semaphores)." (ch17.13, p696)

**(T)** / F Breach of confidentiality involves unauthorized reading of data.<br>
T / **(F)** Breach of integrity involves preventing legitimate use of the system.<br>
**(T)** / F Breach of availability involves unauthorized destruction of data.
> - "Breach of confidentiality. This type of violation involves **unauthorized reading** of data (or theft of information)."
> - "Breach of integrity. This violation involves **unauthorized modification** of data."
> - "Denial of service. This violation involves **preventing legitimate use** of the system."
> - "Breach of availability. This violation involves **unauthorized destruction** of data."
(ch16.1, p622)

T / **(F)** An attack is always malicious and never accidental.
> September 24, 2023, The Adaptable incident.

T / **(F)** Script kiddies are persons who write scripts or codes to crack into computers.
> "[...]one hacker can determine the bug and then write an exploit. Anyone with rudimentary computer skills and access to the exploit— a so-called **script kiddie**—can then try to launch the attack at target systems." (ch16.2, p631)

---
## 2016-2
Circle or cross: ”T” if True – ”F” if False.
```
$ ls -al
total 12
drwxr-xr-x 3 demo demo 4096 Oct 17 17:05 .
drwxrwxrwt 8 root root 4096 Oct 17 17:04 ..
dr-x--x--x 2 demo demo 4096 Oct 17 17:06 tmp
```
**(T)** / F All users can enter directory “tmp/”.
> The `x` permission is enabled for the user "demo", the group "demo" and all other users.

**(T)** / F Only user “demo” can read directory “tmp/”.
> The `r` permission is only enabled for the user "demo", and disabled for all other users.

**(T)** / F A cyber breach occurs when someone accesses a database through an insufficiently secured network connection.<br>
**(T)** / F A physical breach occurs when an unauthorized person is able to physically access a piece of equipment.
> idk, just a guess

T / **(F)** ”Security” is an internal problem. On the other hand, ”protection” also requires consideration of the external environment.
> "Protection is an internal problem. Security, in contrast, must consider both the computer system and the environment..." (ch16.8, p664)

**(T)** / F A backdoor is a method of bypassing normal authentication.
> "This type of security breach [is called] a trap door (or back door)... For instance, the code might check for a specific user ID or password, and it might circumvent normal security procedures when it receives that ID or password." (ch16.1, p626-627)

T / **(F)** A trojan horse is an example of a backdoor.
> A trojan horse is a program that pretends to be something that it isn't, and a backdoor is a program that has intentionally placed weak points.

**(T)** / F A Keylogger is the action of recording (covertly) a keyboard.
> "...a keystroke logger, which records everything entered on the keyboard (including passwords and credit-card numbers)." (ch16.2, p634)


---
## 2017-1
Circle or cross: ”T” if True – ”F” if False.

T / **(F)** Security is a mechanism for controlling processes or users to resources (Yakoob et. al.).
> Protection is the set of mechanisms that control the access of processes and users to the resources defined by a computer system.

T / F Operating Systems automatically apply permissions to files and folder, however users can manually apply them too (Yakoob et. al.).

T / F Symmetric cryptography is much faster than asymmetric one.

**(T)** / F Protection is strictly an internal problem. On the other hand, security is strictly an external problem.

T / F The security mechanisms control access to a system. On the other hand, protection system prevents unauthorized access.

T / F The three aspects to a protection mechanism are authentication, authorization, and access enforcement.

T / F In GNU/Linux, users can be organized into groups, with a single Access Control List (ACL) for an entire group.

T / F Trojan horses are often computer games software infected with viruses.

T / F An access list is a list of objects and the operations allowed on those objects for each domain (OSC9).

T / F If users are allowed to perform their own I/O operation, system integrity will be guaranteed (OSC9).


C language code snippet
```
009 #include <stdio.h>
010 int tambah(int ii, int jj) {
011 return ii + jj;
012 }
013
014 void main(void) {
015 int ii = 4;
016 printf("The return of tambah is %d\n", tambah(1,ii));
017 }
```
Program Output (Line 016):<br>
```
The return of tambah is 5

```


---
## 2017-2

Principle of least **(01)** dictates that programs, users, and even systems be given just enough privileges to perform their tasks (OSC9).<br>
**(02)** is strictly an internal problem (OSC9).<br>
**(03)** requires also consideration of the external environment within which the system operates (OSC9).<br>
A system is **(04)** if its resources are used and accessed as intended under all circumstances (OSC9).<br>
Security is often deployed for **(05)** against external threats (OSC9).<br>
Breach of **(06)** involves unauthorized reading of data (OSC9).<br>
Breach of **(07)** involves unauthorized modification of data (OSC9).<br>
Breach of **(08)** involves unauthorized destruction of data (OSC9).<br>
**(09)** of service involves unauthorized use of resources (OSC9).<br>
**(10)** of service involves preventing legitimate use of the system (OSC9).<br>
**(11)** is when one participant in a communication pretends to be someone else (OSC9).<br>
In a session **(12)**, an active communication session is intercepted (OSC9).<br>
A code segment that misuses its environment is called a **(13)** (OSC9).<br>
**(14)** are self-replicating and are designed to infect other programs (OSC9).<br>
A **(15)** is a process that uses the spawn mechanism to duplicate itself (OSC9).<br>
In a **(16)** encryption algorithm, the same key is used to encrypt and to decrypt (OSC9).<br>
In an **(17)** encryption algorithm, there are different encryption and decryption keys (OSC9).<br>
**(18)** are very useful in that they enable anyone to verify the authenticity of the message (OSC9).<br>
**(19)** is the ability of an individual or group to seclude themselves, or information about themselves, and thereby express themselves selectively (WIKI).<br>

#### Answers:
- (01) Privilege
- (02) Protection
- (03) Security
- (04) Secure
- (05) Protection
- (06) Confidentiality
- (07) Integrity
- (08) Availability
- (09) Theft
- (10) Denial
- (11) Masquerading
- (12) Hijacking
- (13) Trojan horse
- (14) Viruses
- (15) worm
- (16) Symmetric
- (17) Asymmetric
- (18) Digital signatures
- (19) Privacy


C language code snippet
```
009 #include <stdio.h>
010
011 char globalChar=’a’;
012
013 char* getGlobal(void) {
014     char* charPTR = &globalChar;
015     printf("getGlobal1 %c\n", globalChar);
016     *charPTR=’b’;
017     printf("getGlobal2 %c\n", *charPTR);
018     return charPTR;
019 }
021 void main (void) {
022     char localChar=’c’;
023     printf("==== main1 %c\n", localChar);
024     localChar=*getGlobal();
025     printf("==== main2 %c\n", localChar);
026 }
```
Program Output:
```
==== main1 c
getGlobal1 a
getGlobal2 b
==== main2 b
```

---
## 2018-1
Match the number of the sentence above with these following phrases:<br>
An **(01)** list is a list for each object consisting of the domains with a nonempty set of access rights for that object.<br>
A **(02)** list is a list of objects and the operations allowed on those objects for each domain.<br>
Proper access to the hardware is necessary for system **(03)**.<br>
It will be difficult to **(04)** a system if users are allowed to access the hardware.<br>
The **(05)** principle is useful in limiting the amount of damage from a faulty process.<br>
Typically, a breach of confidentiality is the goal of an **(06)**.<br>
Breach of integrity can result in passing of **(07)** to an innocent party.<br>
**(08)** is a common example of breach of availability.<br>
Theft of service involves **(09)** use of resources.<br>
**(10)** is not an attack but rather a means for a cracker to detect a system’s vulnerabilities to attack.<br>

Answers
- (01) access
- (02) capability
- (03) integrity
- (04) protect
- (05) need-to-know
- (06) intruder
- (07) liability
- (08) Website defacement
- (09) unauthorized
- (10) Port scanning


Program written in C:
```
001 /* (c) 2018 This is a free program */
002 /* Rahmat M. Samik-Ibrahim */
003
004 #include <stdio.h>
005
006 void main(void) {
007     char string[]="HALLO";
008     printf("START\n");
009     printf("%s\n", string);
010     printf("%c\n", *string);
011     printf("%c\n", string[1]);
012     printf("STOP\n");
013 }
```
Program output:
```
START
HALLO
H
A
STOP
```



## 2018-2

Program written in C:
```
001 /* (c) 2018 This is free software *
002 * NOTE: ASCII 61H = a; 62H = b */
003 #include <stdio.h>
004 void main(void) {
005     unsigned int ii=’a’;
006     unsigned char ch=’b’;
007     unsigned char* st="dcba";
008     printf("START\n");
009     printf(" ii    = %X or %c\n", ii, ii);
010     printf(" ch    = %X or %c\n", ch, ch);
011     printf("*st    = %X or %c\n", *st, *st);
012     printf(" st[2] = %X or %c\n", st[2], st[2]);
013     printf("STOP\n");
014 }
```
Program output:
```
START
 ii    = 61 or a
 ch    = 62 or b
*st    = 64 or d
 st[2] = 62 or b
STOP
```

## 2019-1
Match the number(s) in the sentence above with these following phrases:<br>
**(01)** ensures the authentication of system users to protect the integrity as well as the physical.<br>
The **(02)** mechanism must provide a means for specifying the controls to be imposed.<br>
A(n) **(03)** is an attempt to break security.<br>
Computer attacks such as **(08)** require human interaction, while **(09)** are self-perpetuating.<br>
**(10)** is capturing data as it is transmitted over a network.<br>
**(11)** attacks are launched from multiple sites at once, toward a common target.<br>
A **(12)** is a token that gives the system permission to access an object.<br>

Answers:
- (01) Security
- (02) Protection
- (03) Attack
- (04) Threat
- (08) Viruses
- (09) Worms
- (10) Sniffing
- (11) Distributed denial-of-service
- (12) Capability


Snippet of program written in C:
```
004 #include <stdio.h>
005 void main (void) {
006     unsigned char ch1=’a’, ch2=’y’, ch3=’z’;
007     printf("START\n");
008     printf("1) ch1 = %c or ASCII %#X\n", ch1, ch1);
009     ch1 = ch1 + ch3 - ch2;
010     printf("2) ch1 = %c or ASCII %#X\n", ch1, ch1);
011     printf("STOP\n");
012 }
```
Program output:
```
START
1) ch1 = a or ASCII 0X61
2) ch1 = b or ASCII 0X62
STOP
```

## 2019-2

Snippet of program written in C:
```
003 #include <stdio.h>
004 int aa=0;
005 int* function(int* bb) {
006     return bb;
007 }
008 void main (void) {
009     int cc=aa++;                                    // cc = 0, aa = 1
010     printf("START\n");
011     printf("1. aa = %d\n", aa);
012     printf("2. *function()=%d\n", *function(&cc));
013     printf("3. cc = %d\n", ++cc);                   // cc = 1 when print
014     printf("STOP\n");
015 }
```
Program output:
```
1. aa = 1
2. *function()=0
3. cc = 1
```


## 2020-1/2022-1
Define/explain briefly (maximum two sentences):

(a) ”Personally Identifying Information (PII)” or ”Personal Data” or ”Personal Information” (88%):
> Information that can be used to identify a specific person, usually relating to individual features or characteristics of said person.
(b) ”Password Manager” (85%):
> An application/a thing that can store all of your passwords for different login pages.
(c) ”Strong Password” (94%):
> A password that is uncrackable if given the whole universe of computing power and the lifespan of the universe. Usually contains many characters and a mix of random ASCII characters.
(d) ”Two-Factor Authentication” (68%):
> A method in which a user is only granted access after verifying 2 factors of authentication. Three factors of authentication include: something the user knows, something the user has, or something the user is.


Snippet of program written in C:
```
003 #include <stdio.h>
004 int returnInt(int ii) {
005     return ii;
006 }
007 char returnChar(char cc) {
008     return cc;
009 }
010 void main(void) {
011     int ii=0x41424344;                  // ii = "DCBA", byte-by-byte char interpretation
012     printf("returnChar=%c\n",
013             returnChar((char) ii));
014     printf("returnChar=%#x\n",
015             (int) returnChar((char) ii));
016     printf("returnInt==%c\n",
017             (char) returnInt(ii));
018     printf("returnInt==%#x\n",
019             returnInt(ii));
020 }
```
Program output:
```
returnChar=D
returnChar=0x44
returnInt==D
returnInt==0x41424344
```


---
### I have to put this here or else (you too)
BinKadal, Sdn. Bhd. (editor)<br>
© 2016 - 2022 — Rev: 43 – 27-Oct-2022. URL: https://rms46.vlsm.org/2/196.pdf. Kumpulan soal ujian lainnya dapat diakses melalui URL: https://os.vlsm.org/. Silakan mengubah, memperbanyak, serta mendistribusikan dokumen ini selama tidak menghapus ketentuan ini!

Personal modifications:<br>
Most code blocks are like `this` instead of "this"<br>
Some questions omitted for similarity to previous questions.<br>