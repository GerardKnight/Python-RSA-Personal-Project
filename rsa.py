import rsa_primes

def gcd(a,b):
    rs=[a,b]
    abu=True
    while abu:
        r_next=rs[-2]%rs[-1]
        if r_next==0:
            out=rs[-1]
            abu=False
        else:
            rs.append(r_next)
    return out

def lcm(a,b):
    return (a*b)//gcd(a,b)

def mod_inverse(a,n):
    qs=[0,0]
    rs=[a,n]
    ss=[1,0]
    ts=[0,1]
    abu=True
    while abu:
        qr_next=divmod(rs[-2],rs[-1])
        q_next=qr_next[0]
        r_next=qr_next[1]
        s_next=ss[-2]-ss[-1]*q_next
        t_next=ts[-2]-ts[-1]*q_next
        if r_next==0:
            return ss[-1]%n
        else:
            rs.append(r_next)
            qs.append(q_next)
            ss.append(s_next)
            ts.append(t_next)
    

def generate_keys(size=100):
    pq=[0,0]
    for i in range(2):
        pq[i]=rsa_primes.find_large_prime(size)
    n=pq[0]*pq[1]
    lambda_n=lcm(pq[0]-1,pq[1]-1)
    e=2**31-1
    d=mod_inverse(e,lambda_n)
    return (n,d)

def encrypt(m,n):
    ms=[]
    outs=[]
    num=10**rsa_primes.int_log(n,10)
    abu=True
    while abu:
        ms.append(m%num)
        m//=num
        if m==0:
            abu=False
    e=2**31-1
    for i in range(len(ms)):
        outs.append(rsa_primes.fme(ms[i],e,n))
    return outs

def decrypt(ms,n,d):
    num=10**rsa_primes.int_log(n,10)
    num2=1
    out=0
    for i in range(len(ms)):
        out+=rsa_primes.fme(ms[i],d,n)*num2
        num2*=num
    return out

def str_nums(to_num):
    out=0
    num=1
    for i in range(len(to_num)):
        out+=ord(to_num[i])*num
        num*=256
    return out

def nums_str(to_num):
    abu=True
    out=""
    while abu:
        out=out+chr(to_num%256)
        to_num//=256
        if to_num==0:
            abu=False
    return out

def main():
    my_private_key=0
    my_public_key=0
    their_public_key=0
    key_size=100
    layer_1=True
    while layer_1:
        print("What would you like to do?\n1. Generate new keys.\n2. Insert new keys.\n3. Print my keys.\n4. Insert a public key (to encrypt with).\n5. Print current public key.\n6. Write a message to encrypt.\n7. Decrypt a message (must be in array form)\nClose. Close the program.")
        todo=input("-->")
        if todo=="1":
            print("Please wait. This may take a few seconds.")
            keys=generate_keys(key_size)
            my_public_key=keys[0]
            my_private_key=keys[1]
            print("Done.")
            print()
        elif todo=="2":
            print("Please select a new public key. Type in 0 to keep it the same.")
            try:
                num=int(input("-->"))
                if num!=0:
                    my_public_key=num
            except:
                print("The public key must be an integer.")
            print("Please select a new private key. Type in 0 to keep it the same.")
            try:
                num=int(input("-->"))
                if num!=0:
                    my_private_key=num
            except:
                print("The private key must be an integer.")
            print()
        elif todo=="3":
            print("Your private key is: "+str(my_private_key))
            print()
            print("Your public key is: "+str(my_public_key))
            print()
        elif todo=="4":
            print("Please select a new public key. Type in 0 to keep it the same.")
            try:
                num=int(input("-->"))
                if num!=0:
                    their_public_key=num
            except:
                print("The public key must be an integer.")
            print()
        elif todo=="5":
            print("You will encrypt with: "+str(their_public_key))
            print()
        elif todo=="6":
            if their_public_key==0:
                print("You must first initialise the key you would like to encrypt with. Please select option 4.")
            else:
                print("Please type in your message.")
                message=input("-->")
                message_num=str_nums(message)
                print(encrypt(message_num,their_public_key))
            print()
        elif todo=="7":
            if my_private_key*my_public_key==0:
                print("You must first initialise your keys. Please select option 1 or 2.")
            else:
                print("Please type in the message you would like to decrypt.")
                message=input("-->")
                message_nums=eval(message)
                try:
                    message_nums_2=decrypt(message_nums,my_public_key,my_private_key)
                    print(nums_str(message_nums_2))
                except:
                    print("Please enter a valid message.")
            print()
        elif todo.lower()=="close":
            print("Goodbye!")
            layer_1=False
        else:
            print()

main()
