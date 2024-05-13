import time, random

class NPC:
    def ADHDNPC():
        print("Knock Knock")
        o = input("[1] > Who's there?\n[2] > Go away hippie\n> ")
        if o == "1":
            input("Hatch\n> ")
            print("Bless you! AH HA")
            time.sleep(.7)
            print("AH HA.")
            time.sleep(.7)
            print("AH HA.")
        elif o == "2":
            print("ok kys")
    def NPC():
        x = random.randint(1,10)
        if x == 1:
            input("Barney: Why can't dinosaurs clap??\n> ")
            print("Barney: Because they're dead. AHAHAHAHAHAHAH")
        elif x == 2:
            print("Wen Qian: Donate me robux at 1886i PLS PLS PLS PLS PLS PLS")
        elif x == 3:
            print("Chad: I am 6'1, have a hellcat, and live in a mansion")
        elif x == 4:
            r = input("Sarah: Am I awesome sauce? Y|N\n> ")
            if r.lower() == "y":
                print("Sarah: Yay thanks! You're also awesome sauce")
            elif r.lower() == "n":
                print("Sarah: You're stinky")
        elif x == 5:
            print("Skobodo Urino: Pod pod pod no no")
        elif x == 6:
            print("Whalen: I am apart of the asian community because how would I know Fei Long if I wasn't?")
        elif x == 7:
            print("JeffBoy_123: In mathematics, the Riemann hypothesis is the conjecture that the Riemann zeta function has its zeros only at the negative even integers and complex numbers with real part 1/2. Many consider it to be the most important unsolved problem in pure mathematics.[1] It is of great interest in number theory because it implies results about the distribution of prime numbers. It was proposed by Bernhard Riemann (1859), after whom it is named. The Riemann hypothesis and some of its generalizations, along with Goldbach's conjecture and the twin prime conjecture, make up Hilbert's eighth problem in David Hilbert's list of twenty-three unsolved problems; it is also one of the Clay Mathematics Institute's Millennium Prize Problems, which offers US$1 million to anyone who solves any of them. The name is also used for some closely related analogues, such as the Riemann hypothesis for curves over finite fields. The Riemann zeta function ζ(s) is a function whose argument s may be any complex number other than 1, and whose values are also complex. It has zeros at the negative even integers; that is, ζ(s) = 0 when s is one of -2, -4, -6, .... These are called its trivial zeros. The zeta function is also zero for other values of s, which are called nontrivial zeros. The Riemann hypothesis is concerned with the locations of these nontrivial zeros, and states that: The real part of every nontrivial zero of the Riemann zeta function is 1/2. Thus, if the hypothesis is correct, all the nontrivial zeros lie on the critical line consisting of the complex numbers 1/2 + it, where t is a real number and i is the imaginary unit.")
        elif x == 8:
            f = input("Davinki: Hai wanna be apart of my newest drawing? (I have come back from the dead) Y|N\n> ")
            if f.lower() == "y":
                print("Davinki: Actually, after further inspection, no thanks!")
            elif f.lower() == "n":
                print("Davinki: Whatever, you weren't cut out to model anyway")
        elif x == 9:
            print("Drake: Kendrick is NOT skboodo urino.")
        elif x == 10:
            print("Kendrick: Drake is a MEANIE WEANIE")
