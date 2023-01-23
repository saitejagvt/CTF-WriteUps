# KnightCTF - 2023

## Table of Contents

- [Challenges](#challenges)
    - [Cryptography](#cryptography)
        - [Xorathrust](#xorathrust)
        - [Factorie](#factorie)
        - [I Love Pi](#i-love-pi)
        - [Encode Mania](#encode-mania)
    - [Forensics](#forensics)
        - [D3CRTPT M3](#d3crtpt-m3)
        - [H3LLO IOS](#h3llo-ios)
        - [Take care of this 1](#take-care-of-this-1)
    - [Networking](#networking)
        - [Hello](#hello)
    - [WEB](#web)
        - [GET Me](#get-me)
    - [Misc](#misc)
        - [Dirt](#dirt)


## Challenges

### Cryptography

#### Xorathrust
- Points: 25

Resources/Scripts:
- [Encrypted Flag](./Files/Xorathrust/flag.enc.txt)
- [encrypt.py](./Files/Xorathrust/encrypt.py)
- [decrypt.py](./Files/Xorathrust/decrypt.py)

Solution:
##### It was a basic XOR encoded text which is encoded by [encrypt.py](./Files/Xorathrust/encrypt.py).
- We can make decrypter by reversing encrypter. 
- After decrypting the text by using [decrypt.py](./Files/Xorathrust/decrypt.py) we get the flag.

#### Factorie
- Points: 50

Resources/Scripts:
- [Dcode.fr](https://www.dcode.fr/rsa-cipher)

Solution:
- We are given the modulus n: `2174096211032823084932239036566496093206280423`
- The task is to find the prime numbers with the help of N.
- By just putting the value of N in Dcode.fr's RSA Cipher tool, we get the values of both prime factors P and Q
- Flag : `KCTF{39434538531451803895327_55131777675015246472249}`

![RSA Cipher - https://imgur.com/a/XFWPnsK](https://i.imgur.com/oGGVpXS.png)

#### I Love Pi
- Points: 100

- Isaac Newton left me this piece of code and a message. Can you help me decode this...


Resources/Scripts:
- [CyberChef](https://gchq.github.io/CyberChef/)

Solution:
- The [i_love.py](./Files/iLovePi/i_love.py) splits the flag with the length provided in lengths variable and base64 encodes seperately.
- Mine was manual approach and i didnot write any script for this.
- Split the text with delimiter as `=` or `==`.
- Then manually decode  using [CyberChef](https://gchq.github.io/CyberChef/) until you find the desired text.
- Then combine them to form a flag.
- Flag : `KCTF{4_P1_4_D4Y_K33P5_7H3_H4CK3r5_4W4Y}`


#### Encode Mania
- Points: 150
- Encoding random stuffs is so cool! I just want to encode it over and over and over again...


Resources/Scripts:
- [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Base32('A-Z2-7%3D',false)From_Hex('None')From_Base64('A-Za-z0-9%2B/%3D',true,false)From_Base85('0-9A-Za-z!%23$%25%26()*%2B%5C%5C-;%3C%3D%3E?@%5E_%60%7B%7C%7D~',true,'')From_Hex('None')From_Hex('None')From_Base32('A-Z2-7%3D',false)From_Base64('A-Za-z0-9%2B/%3D',true,false)From_Base85('0-9A-Za-z!%23$%25%26()*%2B%5C%5C-;%3C%3D%3E?@%5E_%60%7B%7C%7D~',true,'')From_Base64('A-Za-z0-9%2B/%3D',true,false)From_Hex('None')From_Base85('0-9A-Za-z!%23$%25%26()*%2B%5C%5C-;%3C%3D%3E?@%5E_%60%7B%7C%7D~',true,''))

Solution:
- The flag is encoded randomly encoded 12 times with Base13, Base32, Base64 and Base85
- Here I used [CyberChef](https://gchq.github.io/CyberChef/) to decode automaticaly and I have given the CyberChef recipe in the Resources ection.

### Forensics

#### D3CRTPT M3
- Points: 25
- Siam downloaded iPhone firmware to bypass his iPhone 6s iCloud. But he needs the decryption key to open the firmware. Find the decryption key and help siam.. :)

Resources/Scripts:
- [Firmware](https://drive.google.com/drive/folders/1_4JBD0wH2yznb4FnlI5TaZUQRmGVnUnN?usp=share_link)
- [DecryptionKey](https://www.theiphonewiki.com/wiki/Boulder_13B139_(iPhone8,1))

Solution:
- I have given a IOS Firmware Link [iphone8,1_9.1_13b139_FIRMWARE.ipsw](https://drive.google.com/drive/folders/1_4JBD0wH2yznb4FnlI5TaZUQRmGVnUnN?usp=share_link) of iPhone 6s to find the decryption Key.
- To find something we have to google first.
- My query was `iphone8,1 9.1 13b139 key`. By searching this I got the first link [ClickHere](https://www.theiphonewiki.com/wiki/Boulder_13B139_(iPhone8,1)).
- There are many keys of different used. I tried the first key and it worked.
- Key: `4e864f1bdfd5cb8573aa68679fa7aa482900ec17734dac022a9a86c073e9e66084adba02`
- Flag : `KCTF{4e864f1bdfd5cb8573aa68679fa7aa482900ec17734dac022a9a86c073e9e66084adba02}`

#### H3LLO IOS
- Points: 100
- Siam is trying to Bypass his iPhone 6s by IOS firmware modification. He decrypt the file but he failed to modify it. but in the Application section, he has dropped a message.

Resources/Scripts:
- [Firmware](https://drive.google.com/drive/folders/1_4JBD0wH2yznb4FnlI5TaZUQRmGVnUnN?usp=share_link)

Solution:
- It is said that He already decrypted the firmware and there's no need to decrypt again so we can directly extract contents in it.

![https://imgur.com/a/d87V8kA](https://i.imgur.com/Ejun3WQ.png)

- We can see the last modified of file `058-25145-076.dmg` is 4 December 2022.
- If the dmg files are encrypted, we can use the decryption key from **D3CRTPT M3** challenge to decrypt it by using [this](https://reincubate.com/support/how-to/how-to-open-dmg-files/). But we can directly open them using 7zip because DMG Extractors have limited features in their free version.
- It is mentioned that there is a message dropped in the Application Section.

![https://imgur.com/a/LfsCkCZ](https://i.imgur.com/4idXsrk.png)

- This is Applications folder, By following Last Modified Folders, we get the file names `Info` with pastebin link.
- Full path of file : `058-25145-076.dmg\Boulder13B139.N71OS\Applications\Setup.app\Info`
- PasteBin Link : https://pastebin.com/WXLAzVdy
- Flag : `KCTF{105_15_4w350m3}`

#### Take care of this-1
- Points: 100
- Recently my friend downloaded a file and now he wants to know what was his file name.Then he thought that few days ago he was doing a system analyst job.His work was to find suspicious attacker address or ip address . Then he think about that job and get an idea to find his latest downlaoding file . And finally he get that file. are you able to find th latest downloding file?
- Tip: Don't rely just on volatility.


Resources/Scripts:
- [WinDbg](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/debugger-download-tools)
- [MEMORY.DMP](https://drive.google.com/file/d/1ABN6RAOtdZot8G8KS0dvoxlLii8JfMaf/view)

Solution:
- We are given a Crash Memory Dump file and was given task to find out the filename that was downloaded before the crash.
- First I tried with voltality and didn't get any good results.
- Then I searched google about analysing Crash Memory Dump files and found this [Article](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/crash-dump-files)
- I downloaded the WinDbg tool and started analysing the dump file.
![https://imgur.com/a/s4hWDYu](https://i.imgur.com/DlxHSQh.png)
- Upon Checking Logs, I found it was downloading the file named `ntkrnlmp.exe` and tried to submit it and it worked.
- Flag : `KCTF{ntkrnlmp.exe}`

### Networking

#### Hello
- Points: 300
- Sir vignere came to my dreams and sent me this packet capture and told me to find the flag from it which is the key to my success. I am a noob in these cases. So I need your help. Please help me find the flag. Will you?


Resources/Scripts:
- [NetWork Capture](./Files/Hello/find-me.pcapng)

Solution:
- This is a simple network analysis using wireshark.
- Open the file in Wireshark.
![https://imgur.com/a/pNO3xic](https://i.imgur.com/3RoY4qh.png)
- After careful observation, we can see the subdomains of DNS query packets are the letters.
- If we note those letters until we get ==,  it forms the base64 encoded text  - `VVBCTHtvMV9tcjNhX2VuMF9oazNfaTBofQ==`
- After we decode it, we get Vigenere cipher encoded text - `UPBL{o1_mr3a_en0_hk3_i0h}`
-  We can identify it as Vigenere cipher because they mentioned `Vigenere` in the Challenge description.
- We need a key to decode the text.
- This text is in the flag format `KCTF{fl4g_h3r3}`. So `UPBL` = `KCTF`.
![https://imgur.com/a/ReK9LUt](https://i.imgur.com/YSOEQEw.png)
- The name of CTF - `KNIGHT CTF`, so when we try `KNIGHT` as key, we get the flag.
- Flag : `KCTF{h1_th3n_wh0_ar3_y0u}`

### WEB

#### GET Me
- Points: 25
- Can you GET the flag from the API ?
- http://167.99.8.90:9009/

Resources/Scripts:
- [BurpSuite](https://portswigger.net/burp)

Solution:
- When we open that link, we get this message.
![https://imgur.com/a/wjEz9YP](https://i.imgur.com/2HqwRVY.png)
- It says we can't **GET** it. GET is a http/https method used to retrieve data from web application.There are other methods for different purposes.
- When i tried POST method, it asked me to provide an url.
![https://imgur.com/a/7OOPWDV](https://i.imgur.com/moxlytr.png)
- I gave url some random URL with content type as below and got an URL in response.
![https://imgur.com/a/oDCY3mA](https://i.imgur.com/qESDXvs.png)
- It is a kind of promotion for HackenProof. I visited that link, created account, and went to `user/security` section and got the flag.

### Misc

#### Dirt
- Points: 50
- My friend loves to travel. Can you help him get the flag?

Resources/Scripts:
- [Dirt.zip](./Files/dirt.zip)
- [G-Drive Link](https://drive.google.com/file/d/1fS4Z07dvFToFXXmSlxVnfvMfppS8VWaC/view)

Solution:
- We have given a G-Drive link of zip file with recursive folders.
- There are 2 ways we can solve.
- One is Manual way by noting folder names.
- Another is by using Linux Command : `unzip dirt.zip`

- Manual Way:
![https://imgur.com/a/MGX67lb](https://i.imgur.com/YWfi2U8.png)
- Linux Way:
![https://imgur.com/a/D2yYDfn](https://i.imgur.com/gGeMn3m.png)

- Folder Names : `}/s/r/3/d/l/0/f/_/3/d/1/5/n/1/_/s/r/3/d/l/0/f/{/F/T/C/K/`
- Remove `/` symbol and we get, `}sr3dl0f_3d15n1_sr3dl0f{FTCK`
- By reversing the string we get the flag.
```
┌──(kali㉿kali)-[~/Desktop/tmp]
└─$ echo }sr3dl0f_3d15n1_sr3dl0f{FTCK | rev
KCTF{f0ld3rs_1n51d3_f0ld3rs}
```
- Flag : `KCTF{f0ld3rs_1n51d3_f0ld3rs}`
