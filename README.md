# crypto-lab
> ***<font color="red">H</font><font color="orangered">a</font><font color="orange">v</font><font color="gold">i</font><font color="yellow">n</font><font color="greenyellow">g </font><font color="lime">f</font><font color="springgreen">u</font><font color="aqua">n </font><font color="darkturquoise">w</font><font color="dodgerblue">i</font><font color="blue">t</font><font color="navy">h </font><font color="indigo">c</font><font color="darkviolent">r</font><font color="magenta">y</font><font color="deeppink">p</font><font color="red">t</font><font color="orangered">o</font>***

### To Do
- [ ] End writing RSA section
- [ ] Logistic map crypto
- [ ] Diffi-Helmen Key Exchange

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
3. **About my code**  
    - Import `/rsa/rsa.py`
    - For detail information, see `/rsa/demo.py`.