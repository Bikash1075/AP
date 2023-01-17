import string as s
import random as r
if __name__=='__main__':
    s1=s.ascii_lowercase
    s2=s.ascii_uppercase
    s3=s.digits
    s4=s.punctuation
    plen=int(input("Enter password length\n"))

    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    # print(s)

    r.shuffle(s)
    print(f"Your password is : {''.join(s[:plen])}")




    