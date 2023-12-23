import string
import random
class Password:
    List_cahr=[]
    Account_passowrd={}
    def Creating_dic(self,key,item):
        if key in   self.Account_passowrd:
            self.Account_passowrd[key].append(item)
        else:
            self.Account_passowrd[key]=item
    def Gentrate_password(self):
        self.Account=input("Why do you need a password :-")
        self.length=12
        self.Alphabets=string.ascii_letters
        self.Numbers=list(map(str,range(1,11)))
        self.Punctuation=string.punctuation
        self.All_Char_pass=self.Alphabets+''.join(self.Numbers)+self.Punctuation
        for i in self.All_Char_pass:
            self.List_cahr.append(i)
        pass_word=''.join(random.choice(self.List_cahr) for _ in range(self.length))
        self.Creating_dic(self.Account,pass_word)
        print('Password Genterated....')
    def Display(self):
        with open('Password.txt','r') as file: 
            pass_w=file.readline()
        print(pass_w)
    def Save_Password(self):
        for k,v in self.Account_passowrd.items():
            with open('Password.txt','w') as file: file.write(f"{k} = {v}")
        print('Saved..')
    def No_password(self):
        print(f' The   Number of Password :- | {len(self.Account_passowrd)} |')
    def get_password(self,item):
        print(f'Password ---> {self.Account_passowrd[item]}')
    def Delete(self,key):
        del self.Account_passowrd[key]  
        print('...Delete..')
password=Password()
while True:
        print("-------------------------------------")
        print('1| Generate Password ?') 
        print('2| Save Password ')
        print('3| Number of password storde')
        print('4| what password is it ?')   
        print('5| How many account ') 
        print('6| Display  ') #6
        print('7| Delete Password ')  
        print('8| Quits') 
        print("-------------------------------------")
        user_input=input('Enter Input Hear:-')
        if user_input=="1":
            password.Gentrate_password() 
        elif user_input=="2":
            password.Save_Password()  
        elif user_input=="3":
            password.No_password()  
        elif user_input=="4":
            item=input('Enter the account:- ')
            password.get_password(item)  
        elif user_input=="5":
            for Account in password.Account_passowrd:
                print(Account)  
        elif user_input=="6": 
            password.Display()
        elif user_input=="7":
            key=input("enter Account which you want to Delete:-")
            password.Delete(key)   
        elif user_input=="8":
            break
        else:
            print('invalide user input')