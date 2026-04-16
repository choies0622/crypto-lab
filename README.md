# crypto-lab
> ***<font color="red">H</font><font color="orangered">a</font><font color="orange">v</font><font color="gold">i</font><font color="yellow">n</font><font color="greenyellow">g </font><font color="lime">f</font><font color="springgreen">u</font><font color="aqua">n </font><font color="darkturquoise">w</font><font color="dodgerblue">i</font><font color="blue">t</font><font color="navy">h </font><font color="indigo">c</font><font color="darkviolent">r</font><font color="magenta">y</font><font color="deeppink">p</font><font color="red">t</font><font color="orangered">o</font>***

### To Do
- [x] RSA
- [x] RSA attack demo
- [ ] Classical crypto adventure
    - [x] Caesar crypto
- [ ] Develop my Logistic map crypto

## Caesar
1. **Background**  
    *Caesar cipher* is one of the simplest and most widely known encryption techniques.  
    It is a type of *substitution cipher*, which is a part of *symmetric cryptosystem*.  
    This cipher was named after Julius Caesar, the Roman general, who used it in his private correspondence.
2. **Steps**  
    Each letter in the plaintext is replaced by a letter some fixed number of positions along the alphabet.  
    
    To **encrypt** a message $m$:  
    $$E_n(x) = (x + n) \bmod 26$$
    To **decrypt** a cipher $c$:
    $$D_n(x) = (x - n) \bmod 26$$
    *i.e. lets use **left shift of 3 places** for encryption.*  
    |Plain|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|
    |--|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
    |Cipher|X|Y|Z|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|
    
    **`Plaintext : THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG`**  
    **`Ciphertext: QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD`**  
3. **Ideas**
    - Modulus
    - Submitution cipher
4. **File Structure**  
    ```
    crypto-lab/
    └─ caeser/
       ├─ caeser.py
       └─ demo.py
    ```
5. **Run and Output**
    - Run: `python caeser/caeser.py`
    - Output:
    ```
    Enter the message [str & int]: Hello world 123
    Enter the key [int]: 3
    Encrypted: KHOOR ZRUOG 456
    Decrypted: HELLO WORLD 123
    ```
6. **Limitation**  
    As key is an integer between $0$ and $25$, and therefore there is only 26 cases, why don't we just try them all?  
    → This attack method is called **Brute Force Attack**.  
    *→ See `caeser/attack.py` and `rsa/attack_demo.py`.*  
    
    - Run: `python caeser/attack_demo.py`
    - Output:  
    (The brute-force attack has been successfully decrypted, as shown in the line 8.)
    ```
    Enter the message [str & int]: Hello world 123
    Enter the key [int]: 3
    Encrypted: KHOOR ZRUOG 456
    Decrypt trial:
    KHOOR ZRUOG 456
    JGNNQ YQTNF 345
    IFMMP XPSME 234
    HELLO WORLD 123
    GDKKN VNQKC 012
    FCJJM UMPJB 901
    EBIIL TLOIA 890
    DAHHK SKNHZ 789
    CZGGJ RJMGY 678
    BYFFI QILFX 567
    AXEEH PHKEW 456
    ZWDDG OGJDV 345
    YVCCF NFICU 234
    XUBBE MEHBT 123
    WTAAD LDGAS 012
    VSZZC KCFZR 901
    URYYB JBEYQ 890
    TQXXA IADXP 789
    SPWWZ HZCWO 678
    ROVVY GYBVN 567
    QNUUX FXAUM 456
    PMTTW EWZTL 345
    OLSSV DVYSK 234
    NKRRU CUXRJ 123
    MJQQT BTWQI 012
    LIPPS ASVPH 901
    ```

## RSA
1. **Background**  
    *RSA algorithm* is a part of the old **public-key cryptosystem**, or *asymmetric cryptosystem*, which uses **different keys for encryption and decryption**.  
    This algorithm was invented by Ron Rivest, Adi Shamir and Leonard Adleman, firstly published in 1977.  
2. **Steps**  
    Generate Keypairs:
    1. Select an any prime numbers $p$ and $q$.  
    2. Calculate $n = p \times q$.  
    3. Calculate $\varphi = (p - 1)(q - 1)$.  
    4. Choose an integer $e$ such that $1 < e < \varphi$ and $\gcd(e, \varphi) = 1$.  
    5. Calculate $d$ such that $d \times e \equiv 1 \pmod \varphi$.  

    The **public key** is $(n, e)$, and the **private key** is $(n, d)$.  

    To **encrypt** a message $m$:
    $$c = m^e \bmod n$$
    To **decrypt** a cipher $c$:
    $$m = c^d \bmod n$$
3. **Ideas**
    - Modulus
    - Euler totient
    - Modular inverse
    - Public/private key separation
4. **File Structure**  
    ```
    crypto-lab/
    └─ rsa/
       ├─ rsa.py
       ├─ demo.py
       ├─ attack.py
       └─ attack_demo.py
    ```
5. **Run and Output**  
    - Run: `python rsa/demo.py`
    - Output:
        ```
        Keypair: (229039, 26953, 216937)
        Enter the message: Hello world 123
        Encrypted: [222252, 45740, 59485, 59485, 48754, 160075, 125796, 48754, 204598, 59485, 228093, 160075, 190764, 1032, 53066]
        Decrypted: Hello world 123
        ```
        - used ASCII for non-numbers.
6. **Limitation**  
    **Small primes for $p, q$ is NOT secure.**  
    *→ See `rsa/attack.py` and `rsa/attack_demo.py`.*  
    
    - Run: `python rsa/attack_demo.py`
    - Output:
    ```
    Keypair: (164959, 31903, 111143)
    Enter the message: Hello world 123
    Encrypted: [107124, 29466, 73140, 73140, 130659, 103808, 78432, 130659, 28709, 73140, 60982, 103808, 130328, 160132, 104614]
    Public Key: (164959, 31903)
    Factored n into p=293, q=563
    Recovered private exponent d=111143
    Decrypted message: Hello world 123
    ```