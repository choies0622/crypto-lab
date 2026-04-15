# crypto-lab
> ***<font color="red">H</font><font color="orangered">a</font><font color="orange">v</font><font color="gold">i</font><font color="yellow">n</font><font color="greenyellow">g </font><font color="lime">f</font><font color="springgreen">u</font><font color="aqua">n </font><font color="darkturquoise">w</font><font color="dodgerblue">i</font><font color="blue">t</font><font color="navy">h </font><font color="indigo">c</font><font color="darkviolent">r</font><font color="magenta">y</font><font color="deeppink">p</font><font color="red">t</font><font color="orangered">o</font>***

### To Do
- [x] RSA
- [ ] RSA attack demo
- [ ] Classical crypto adventure
- [ ] Develop my Logistic map crypto

## RSA
1. **Background**  
    *RSA algorithm* is a part of the old **public-key cryptosystem**, or asymmetric cryptosystem, which uses different key to encrypt and decrypt.  
    This algorithm was invented by Ron Rivest, Adi Shamir and Leonard Adleman, firstly published in 1977.  
2. **Steps**  
    Generate Keypairs:
    1. Select an any prime number $p$, $q$.  
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
    - Modulurs
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
        Keypair: (350633, 282323, 338267)
        Enter the message: hello I am homo sapiens
        Encrypted: [10445, 205055, 231431, 231431, 156233, 263688, 170647, 263688, 22320, 272231, 263688, 10445, 156233, 272231, 156233, 263688, 152115, 22320, 43420, 14604, 205055, 220719, 152115]
        Decrypted: hello I am homo sapiens
        ```
        - used ASCII for non-numbers.
6. **Limitation**  
    **Small primes for $p, q$ is NOT secure.**  
    *→ See `rsa/attack.py` and `rsa/attack_demo.py`.*  
    
    - Run: `python rsa/attack_demo.py`
    - Output:
    ```
    Keypair: (122539, 110171, 66803)
    Enter the message: I am homo sapiens 123
    Encrypted: [50706, 36447, 23296, 95729, 36447, 53402, 93282, 95729, 93282, 36447, 33710, 23296, 47701, 20759, 85789, 38751, 33710, 36447, 10957, 109133, 11527]
    Public Key: (122539, 110171)
    Factored n into p=283, q=433
    Recovered private exponent d=66803
    Decrypted message: I am homo sapiens 123
    ```