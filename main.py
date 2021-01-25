import json 
import re

user=input("What do you want to do? 1. Login  2. Singup Enter `l` or `s` respectively!:--")
if user == "s":
    dic={}
    dic2={}
    List=[]
    check = 0
    user_name=input("enter user name:--")
    password1=input("enter the first password:--")
    password2=input("confirm the password:--")
    if password1!=password2:
        print("both password are not same")
    else:
        
        if "$" in password1 or "#" in password1:
            if re.findall(r"^\w+",password1):
                try:
                    json_data=open("userdetails.json", "r")
                    all_data=json.load(json_data)
                    json_data.close()
                    i=0
                    while i<len(all_data["user"]):
                        a=(all_data["user"][i])
                        if a["username"]==user_name:
                            print("alredy exist")
                            check = 1
                            break
                        i=i+1
                except:
                    check = 1
                    dic["username"]=user_name
                    dic["Password"]=password1
                    List.append(dic)
                    dic2["user"]=List
                    data=open("userdetails.json", "w")
                    json.dump(dic2, data)
                    data.close()
                    print("congrarts", user_name, "you are Signed Up Successfully")
                    details=input("enter the discreption:---")
                    Birthday_date=input("enter the birthday date:---")
                    Hobbis=input("enter the hobbis:---")
                    Gender=input("enter the gender:---")
                    dic_bio={}
                    dic_bio["Descreption"]=details
                    dic_bio["dob"]=Birthday_date
                    dic_bio["Hobbis"]=Hobbis
                    dic_bio["Gender"]=Gender
                    dic["profile"]=dic_bio
                    bio_data = open("userdetails.json","w")
                    json.dump(dic2, bio_data, indent=2)
                    bio_data.close() 
                if(check != 1):
                    newDic = {}
                    newDic["username"]=user_name
                    newDic["password"]=password1
                    all_data['user'].append(newDic)
                    my_data=open("userdetails.json", "w")
                    json.dump(all_data, my_data)
                    my_data.close()
                    print("congrarts", user_name, "you are Signed Up Successfully")
                    details=input("enter the discreption:---")
                    Birthday_date=input("enter the birthday date:---")
                    Hobbis=input("enter the hobbis:---")
                    Gender=input("enter the gender:---")
                    dic_bio={}
                    dic_bio["Descreption"]=details
                    dic_bio["dob"]=Birthday_date
                    dic_bio["Hobbis"]=Hobbis
                    dic_bio["Gender"]=Gender
                    newDic["profile"]=dic_bio
                    bio_data = open("userdetails.json","w")
                    json.dump(all_data, bio_data, indent=2)
                    bio_data.close()
             
            else:
                 print("Error, atleast one number and one special charecter should in password")

        else:
           print("Error, atleast one number and one special charecter should in password")
else:
    username_old=input("enter the username:--")
    password=input("enter the password:--")
    j_data=open("userdetails.json", "r")
    a_data=json.load(j_data)
    j_data.close()
    i=0
    while i<len(a_data["user"]):
        a=(a_data["user"][i])
        if a["username"]==username_old:
            print(username_old, "you are logged In Successfully")
            print("profile")
            print("Username:",username_old)
            print("Gender:", a['profile']['Gender'])
            print("Bio:", a['profile']["Descreption"])
            print("Hobbis:", a['profile']['Hobbis'])
            print("Dob:", a['profile']['dob'])
            break
        i=i+1
    else:
        print("invalid username")
    




