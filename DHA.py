#Diffie-Hellman by PRINCE
#here J is the public key for JACK
#K is the public key for KING
#A is the private key for JACK
#B is the private key for KING
#J should always be prime number otherwise the output will be 0

J = int(input("J is a prime number and a public key for JACK:"))
for i in range(2, J):
         # checking for factor
         if J % i == 0:
            print("renter value of J because it's not a prime number")
            J = int(input("J is a prime number and a public key for JACK:"))
print(J)


K = int(input("The Value of K(public keys for KING) is:"))




def DHA(J,K):
    
    #Jack's private key A
    A = int(input("The Private Key A for Jack is: "))
    
    #gets a generated key
    T = int(pow(K,A,J))

    #king's private key B
    B = int(input("The Private Key B for king is: "))

    #get a generated key
    R= int(pow(K,B,J))
    #print(R)

    #secret key for JACK
    pA= int(pow(R,A,J))
    #print(pA)

    #secret key for KING
    pB= int(pow(T,B,J))
    #print(pB)


    print("Secret key for the JACK is :")
    print(pA)

    print("Secret key for the KING is :")
    print(pB)
    

    

DHA(J,K)