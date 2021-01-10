#----------------------------------------------------------------------------------
#C-STORE
#F-Food or Snacks|J=Juices|ET=Emergency tools
######################################################


import os
import pickle
print "Welcome to             "
print " |''''''       |'''''''''''  '''''|'''''   |'''''''|      |''''''''|    |''''''''''           "
print " |          ~ |...........        |         |  O  |      |  ____|    |-----               "
print " |.......       ............|      |        |.......|      |   \          |..........  Admin "
print "  ___________________________________|     \_________________                                "
print
print


#------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                #Food/Snacks Main
#------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Food:
    def foodfunc(self):
        food=open("Snacks_Backup.dat","ab")
        self.itno=input("Enter Item Number >>")
        self.f=raw_input("Enter Food name >>")
        self.fc=input("Enter Food cost >>")
        self.stock=input("Enter Stock left >>")
        self.sold=0
        self.moneyobt=self.fc*self.sold
        self.x="|Item number  "+str(self.itno)+"|"+str(self.f)+"|"+"AED:  "+str(self.fc)+"|"+"Stock left   "+str(self.stock)+"|"+"Sold   "+str(self.sold)+"|"+"Money Obtained   "+str(self.moneyobt)+"|"
        pickle.dump(self.x,food)
        food.close()
    def upfunc(self):
        food=open("Temp.dat","ab")
        self.itno=input("Enter Item Number >>")
        self.f=raw_input("Enter Food name >>")
        self.fc=input("Enter Food cost >>")
        self.stock=input("Enter Stock left >>")
        self.sold=0
        self.moneyobt=self.fc*self.sold
        self.x="|Item number  "+str(self.itno)+"|"+str(self.f)+"|"+"AED:  "+str(self.fc)+"|"+"Stock left   "+str(self.stock)+"|"+"Sold   "+str(self.sold)+"|"+"Money Obtained   "+str(self.moneyobt)+"|"
        pickle.dump(self.x,food)
        food.close()
    def BuyC(self):
        if os.path.isfile("Snacks.dat"):
            f=open("Snacks.dat","rb")
            g=open("Temp.dat","wb")
            itn=input("Enter Item Number >")
            try:
                while True:
                        H=pickle.load(f)
                        if H[14] != str(itn):
                            pickle.dump(H,g)
                        elif H[14]==str(itn):
                            y=''
                            for i in len(H):
                                if i==48:
                                    x=int(H[48])+1
                                    y+=str(x)
                                    c=x*int(H[24])
                                elif i==39:
                                    p=int(H[39])-1
                                    y+=str(p)
                                elif i==67:
                                    y+=str(c)                                   
                                
            except EOFError:
                        g.close()
                        f.close()
            os.remove("Snacks.dat")
            os.rename("Temp.dat","Snacks.dat")
        else:
            print "File does not exist"
    def display_food(self):
        if os.path.isfile("Food.dat"):
            f=open("Food.dat","rb")
            try:
                while True:
                    x=pickle.load(f)
                    print x.x
            except EOFError:
                print "End of Menu"
                f.close()
    def totalmoney(self):
        if os.path.isfile("Snacks.dat"):
            f=open("Snacks.dat","rb")
            sums=0
            try :
                while True:
                    x=pickle.load(f)
                    sums+=x.moneyobt
            except EOFError:
                print "End of Menu"
                f.close()




#.............................................................................................................
                                                    #JUICE
#.............................................................................................................
class Juice:
    def jfunc(self):
        juice=open("Juice.dat","ab")
        self.jno=input("Enter Item Number >>")
        self.j=raw_input("Enter Juice name >>")
        self.jc=input("Enter Juice cost >>")
        self.jstock=input("Enter Stock left >>")
        self.jsold=0
        self.jmoneyobt=self.jc*self.jsold
        x="|Item number  "+str(self.jno)+"|"+str(self.j)+"|"+"AED:  "+str(self.jc)+"|"+"Stock left   "+str(self.jstock)+"|"+"Sold   "+str(self.jsold)+"|"+"Money Obtained   "+str(self.jmoneyobt)+"|"
        pickle.dump(x,juice)
        juice.close()
    def display_juice(self):
        if os.path.isfile("Juice.dat"):
            f=open("Juice.dat","rb")
            try:
                while True:
                    x=pickle.load(f)
                    print x.x
            except EOFError:
                print "End of Menu"
                f.close()
    def jtotalmoney(self):
        if os.path.isfile("Juice.dat"):
            f=open("Juice.dat","rb")
            sums=0
            try :
                while True:
                    x=pickle.load(f)
                    sums+=x.moneyobt
            except EOFError:
                print "End of Menu"
                f.close()




#----------------------------------------------------------------------------------
                                                #Emergency Tools
#-----------------------------------------------------------------------------------
class Etools:
    def etfunc(self):
        etools=open("Emergency tools.dat","ab")
        self.etno=input("Enter Item Number >>")
        self.et=raw_input("Enter Item name >>")
        self.etc=input("Enter Item cost >>")
        self.etstock=input("Enter Stock left >>")
        self.etsold=0
        self.etmoneyobt=self.etc*self.etsold
        x="|Item number  "+str(self.etno)+"|"+str(self.et)+"|"+"AED:  "+str(self.etc)+"|"+"Stock left   "+str(self.etstock)+"|"+"Sold   "+str(self.etsold)+"|"+"Money Obtained   "+str(self.etmoneyobt)+"|"
        pickle.dump(x,etools)
        etools.close()
    def display_etools(self):
         if os.path.isfile("Emergency tools.dat"):
            f=open("Emergency tools.dat","rb")
            
            try:
                while True:
                    x=pickle.load(f)
                    print x.x
            except EOFError:
                print "End of Menu"
                f.close()
    def ettotalmoney(self):
        if os.path.isfile("Emergency tools.dat"):
            f=open("Emergency tools.dat","rb")
            sums=0
            try :
                while True:
                    x=pickle.load(f)
                    sums+=x.moneyobt
            except EOFError:
                print "End of Menu"
                f.close()

#----------------------------------------------------------------------------------
                                        #SEARCH FUNCTIONS 
#----------------------------------------------------------------------------------
def SearchF():                                                                      #food
    if os.path.isfile("Food.dat"):
            f=open("Food.dat","rb")
            
            itn=input("Enter Item Number >")
            try:
                while True:
                        H=pickle.load(f)
                        if H.itno!= itn:
                            pass
                        elif H.itno==itn:
                            print H.x
        
            except EOFError:         
                        f.close()          
    else:
            print "File does not exist"
def SearchJ():                                                                      #Juice
    if os.path.isfile("Juice.dat"):
            f=open("Juice.dat","rb")
            
            itn=input("Enter Item Number >")
            try:
                while True:
                        H=pickle.load(f)
                        if H.jno!= itn:
                            pass
                        elif H.jno==itn:
                            print H.x
        
            except EOFError:         
                        f.close()          
    else:
            print "File does not exist"
def SearchET():                                                                      #Juice
    if os.path.isfile("Emergency tools.dat"):
            f=open("Emergency tools.dat","rb")
            
            itn=input("Enter Item Number >")
            try:
                while True:
                        H=pickle.load(f)
                        if H.etno!= itn:
                            pass
                        elif H.etno==itn:
                            print H.x
        
            except EOFError:         
                        f.close()          
    else:
            print "File does not exist"



#----------------------------------------------------------------------------------
                                            #DELETE FUNCTIONS
#----------------------------------------------------------------------------------            
def DeleteF():                                                                          #Snacks
    if os.path.isfile("Food.dat"):
            f=open("Food.dat","rb")
            g=open("Temp.dat","wb")
            itn=input("Enter Item Number >")
            try:
                while True:
                        H=pickle.load(f)
                        if H.itno !=itn:
                            pickle.dump(H,g)
                        elif H.itno==itn:
                            pass
        
            except EOFError:
                        g.close()
                        f.close()
            os.remove("Food.dat")
            os.rename("Temp.dat","Food.dat")
    else:
            print "File does not exist"
def DeleteJ():                                                                              #Juice
    if os.path.isfile("Juice.dat"):
            f=open("Juice.dat","rb")
            g=open("Temp.dat","wb")
            itn=input("Enter Item Number >")
            try:
                while True:
                        H=pickle.load(f)
                        if H.jno!=itn:
                            pickle.dump(H,g)
                        elif H.jno==itn:
                            pass
        
            except EOFError:
                        g.close()
                        f.close()
            os.remove("Juice.dat")
            os.rename("Temp.dat","Juice.dat")
    else:
            print "File does not exist"
def DeleteET():                                                                              #Juice
    if os.path.isfile("Emergency tools.dat"):
            f=open("Emergency tools.dat","rb")
            g=open("Temp.dat","wb")
            itn=input("Enter Item Number >")
            try:
                while True:
                        H=pickle.load(f)
                        if H.etno!= itn:
                            pickle.dump(H,g)
                        elif H.etno==itn:
                            pass
        
            except EOFError:
                        g.close()
                        f.close()
            os.remove("Emergency tools.dat")
            os.rename("Temp.dat","Emergency tools.dat")
    else:
            print "File does not exist"




#---------------------------------------------------------------------------------
                                            #UPDATE FUNCTIONS
#---------------------------------------------------------------------------------
def UpdateF():
        if os.path.isfile("Food.dat"):
            f=open("Food.dat","rb")
            g=open("Temp.dat","wb")
            itn=input("Enter Item Number >")
            try:
                while True:
                        H=pickle.load(f)
                        if H.itno!= itn:
                            pickle.dump(H,g)
                        elif H.itno==itn:
                            N=Food()
                            N.itno=input("Enter Item Number >>")
                            N.f=raw_input("Enter Food name >>")
                            N.fc=input("Enter Food cost >>")
                            N.stock=input("Enter Stock left >>")
                            N.sold=0
                            N.moneyobt=N.fc*N.sold
                            N.x="|Item number  "+str(N.itno)+"|"+str(N.f)+"|"+"AED:  "+str(N.fc)+"|"+"Stock left   "+str(N.stock)+"|"+"Sold   "+str(N.sold)+"|"+"Money Obtained   "+str(N.moneyobt)+"|"
                            
                            pickle.dump(N,g)
            
            except EOFError:
                        g.close()
                        f.close()
            os.remove("Food.dat")
            os.rename("Temp.dat","Food.dat")
        else:
            print "File does not exist"
def UpdateJ():
        if os.path.isfile("Juice.dat"):
            f=open("Juice.dat","rb")
            g=open("Temp.dat","wb")
            itn=input("Enter Item Number >")
            try:
                while True:
                        H=pickle.load(f)
                        if H.jno!= itn:
                            pickle.dump(H,g)
                        elif H.jno==itn:
                            N=Juice()
                            N.jno=input("Enter Item Number >>")
                            N.j=raw_input("Enter Juice name >>")
                            N.jc=input("Enter Juice cost >>")
                            N.jstock=input("Enter Stock left >>")
                            N.jsold=0
                            N.jmoneyobt=N.jc*N.jsold
                            N.x="|Item number  "+str(N.jno)+"|"+str(N.j)+"|"+"AED:  "+str(N.jc)+"|"+"Stock left   "+str(N.jstock)+"|"+"Sold   "+str(N.jsold)+"|"+"Money Obtained   "+str(N.jmoneyobt)+"|"
                            
                            pickle.dump(N,g)
            except EOFError:
                        g.close()
                        f.close()
            os.remove("Juice.dat")
            os.rename("Temp.dat","Juice.dat")
        else:
            print "File does not exist"
def UpdateET():
        if os.path.isfile("Emergency tools.dat"):
            f=open("Emergency tools.dat","rb")
            g=open("Temp.dat","wb")
            itn=input("Enter Item Number >")
            try:
                
                while True:
                        H=pickle.load(f)
                        if H.etno!= itn:
                            pickle.dump(H,g)
                        elif H.etno==itn:
                            N=Etools()
                            N.etno=input("Enter Item Number >>")
                            N.et=raw_input("Enter Etool name >>")
                            N.etc=input("Enter Etool cost >>")
                            N.etstock=input("Enter Stock left >>")
                            N.etsold=0
                            N.etmoneyobt=N.etc*N.etsold
                            N.x="|Item number  "+str(N.etno)+"|"+str(N.et)+"|"+"AED:  "+str(N.etc)+"|"+"Stock left   "+str(N.etstock)+"|"+"Sold   "+str(N.etsold)+"|"+"Money Obtained   "+str(N.etmoneyobt)+"|"
                            
                            pickle.dump(N,g)
            
            except EOFError:
                        g.close()
                        f.close()
            os.remove("Emergency tools.dat")
            os.rename("Temp.dat","Emergency tools.dat")
        else:
            print "File does not exist"



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                                #MAIN FUNCTION
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
ch="yes"
while ch=="yes":
    print "Enter Option"
    i=raw_input("Food(F),Juice(J) or Emergency Tools(E)>>")


    #Food/Snacks~~~~~~~~
    while i=="f"or i=="F":
        print "|1 for append|2 for display|3 for Update|4 for Delete|5 for Search|"
        c=input("Enter Choice >>")
        if c==1:
            N=Food()
            N.itno=input("Enter Item Number >>")
            N.f=raw_input("Enter Food name >>")
            N.fc=input("Enter Food cost >>")
            N.stock=input("Enter Stock left >>")
            N.sold=0
            N.moneyobt=N.fc*N.sold
            N.x="|Item number  "+str(N.itno)+"|"+str(N.f)+"|"+"AED:  "+str(N.fc)+"|"+"Stock left   "+str(N.stock)+"|"+"Sold   "+str(N.sold)+"|"+"Money Obtained   "+str(N.moneyobt)+"|"
            f=open("Food.dat","ab")
            pickle.dump(N,f)
            d=raw_input("Are you done ?")
            f.close()
            if d=="yes":
                i=raw_input("Food(F),Juice(J) or Emergency Tools(E)>>")
        elif c==2:
            info=Food()
            info.display_food()
            d=raw_input("Are you done ?")
            if d=="yes":
                i=raw_input("Food(F),Juice(J) or Emergency Tools(E)>>")
        elif c==3:
            UpdateF()
            d=raw_input("Are you done ?")
            if d=="yes":
                i=raw_input("Food(F),Juice(J) or Emergency Tools(E)>>")
        elif c==4:
            DeleteF()
            d=raw_input("Are you done ?")
            if d=="yes":
                i=raw_input("Food(F),Juice(J) or Emergency Tools(E)>>")
        elif c==5:
            SearchF()
            d=raw_input("Are you done ?")
            if d=="yes":
                i=raw_input("Food(F),Juice(J) or Emergency Tools(E)>>")
        #"""""""""""""""""""""""""""""""""""""""""""""""""""

                
    #Juice~~~~~~~~~~~~~~~~~~~~~~~~~~~
    while i=="j"or i=="J":
        print "|1 for append|2 for display|3 for Update|4 for Delete|5 for Search|"
        c=input("Enter Choice >>")
        if c==1:
            N=Juice()
            N.jno=input("Enter Item Number >>")
            N.j=raw_input("Enter Juice name >>")
            N.jc=input("Enter Juice cost >>")
            N.jstock=input("Enter Stock left >>")
            N.jsold=0
            N.jmoneyobt=N.jc*N.jsold
            N.x="|Item number  "+str(N.jno)+"|"+str(N.j)+"|"+"AED:  "+str(N.jc)+"|"+"Stock left   "+str(N.jstock)+"|"+"Sold   "+str(N.jsold)+"|"+"Money Obtained   "+str(N.jmoneyobt)+"|"
            f=open("Juice.dat","ab")
            pickle.dump(N,f)
            d=raw_input("Are you done ?")
            f.close()
            d=raw_input("Are you done ?")
            if d=="yes":
                i=raw_input("Food(F),Juice(J) or Emergency Tools(E)>>")
        elif c==2:
            info=Juice()
            info.display_juice()
            d=raw_input("Are you done ?")
            if d=="yes":
                i=raw_input("Food(F),Juice(J) or Emergency Tools(E)>>")
        elif c==3:
            UpdateJ()
            d=raw_input("Are you done ?")
            if d=="yes":
                i=raw_input("Food(F),Juice(J) or Emergency Tools(E)>>")
        elif c==4:
            DeleteJ()
            d=raw_input("Are you done ?")
            if d=="yes":
                i=raw_input("Food(F),Juice(J) or Emergency Tools(E)>>")
        elif c==5:
            SearchJ()
            d=raw_input("Are you done ?")
            if d=="yes":
                i=raw_input("Food(F),Juice(J) or Emergency Tools(E)>>")
        #""""""""""""""""""""""""""""""""""""""""""""""""""""""

                
    #Emergency tools~~~~~~~~~~~~~~~~~~~~~~~~~~
    while i=="e"or i=="E":
        print "|1 for append|2 for display|3 for Update|4 for Delete|5 for Search|"
        c=input("Enter Choice >>")
        if c==1:
            N=Etools()
            N.etno=input("Enter Item Number >>")
            N.et=raw_input("Enter Food name >>")
            N.etc=input("Enter Food cost >>")
            N.etstock=input("Enter Stock left >>")
            N.etsold=0
            N.etmoneyobt=N.etc*N.etsold
            N.x="|Item number  "+str(N.etno)+"|"+str(N.et)+"|"+"AED:  "+str(N.etc)+"|"+"Stock left   "+str(N.etstock)+"|"+"Sold   "+str(N.etsold)+"|"+"Money Obtained   "+str(N.etmoneyobt)+"|"
            f=open("Emergency tools.dat","ab")
            pickle.dump(N,f)
            d=raw_input("Are you done ?")
            f.close()
            d=raw_input("Are you done ?")
            if d=="yes":
                i=raw_input("Food(F),Juice(J) or Emergency Tools(E)>>")
        elif c==2:
            info=Etools()
            info.display_etools()
            d=raw_input("Are you done ?")
            if d=="yes":
                i=raw_input("Food(F),Juice(J) or Emergency Tools(E)>>")
        elif c==3:
            UpdateET()
            d=raw_input("Are you done ?")
            if d=="yes":
                i=raw_input("Food(F),Juice(J) or Emergency Tools(E)>>")
        elif c==4:
            DeleteET()
            d=raw_input("Are you done ?")
            if d=="yes":
                i=raw_input("Food(F),Juice(J) or Emergency Tools(E)>>")
        elif c==5:
            SearchET()
            d=raw_input("Are you done ?")
            if d=="yes":
                i=raw_input("Food(F),Juice(J) or Emergency Tools(E)>>")
                   
