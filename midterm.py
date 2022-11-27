import tkinter
import json
islogin=False
login_user=""
def jread():
    try:
        with open("info.json") as f:
            users=json.load(f)
    except:
        print("users file is damaged!trying to make a new file")
        users={"admin":"123456789"}
        jwrite(users)
    return users

def jwrite(users):
    with open("info.json",'w')as f:
        json.dump(users,f)

def login():
    global islogin,login_user
    lst=[]
    if islogin==True:
        lbl.configure(text="you are already logged in!",fg="red")
        return
    user=txt_user.get()
    passw=txt_passw.get()
    users=jread()
    if (user in users) and (users[user]==passw):
        lbl.configure(text="welcome!",fg="green")
        islogin=True
        login_user=user
        lst.append(user)
        with open("login.json",'w') as f:
            json.dump(lst,f)   
    else:
        lbl.configure(text="wrong user/pass!",fg="red")
            
def submit():
    user=txt_user.get()
    passw=txt_passw.get()
    if len(passw)<5:
        lbl.configure(text="password length error!",fg="red")
        return
    users=jread()
    if user in users:
        lbl.configure(text="username exist!",fg="red")
        return
    users={"admin":"123456789"}
    users[user]=passw
    jwrite(users)
    lbl.configure(text="you have been submitted!",fg="green")
    
def logout():
    global islogin,login_user
    islogin=False
    login_user=""
    lbl.configure(text="you are logged out now!",fg="green")

def deleteAcc():
    global islogin,login_user
    if islogin==False:
        lbl.configure(text="please login first!",fg="red")
        return
    if login_user=="admin":
        lbl.configure(text="admin account is not removable!",fg="red")
        return
    users=jread()
    
############################## new window pop out    
    win1=tkinter.Tk()
    win1.title('delete account')
    win1.geometry('240x200')
    win1.configure(bg="cyan")
    lbldel=tkinter.Label(win1,text="are you sure to delete your account?!",fg="blue")
    lbldel.pack()
    lbldel.place(x=20,y=50)
    
############################## making yes\no for deleteAcc       
    def yes():
        global login_user,islogin
        users.pop(login_user)
        jwrite(users)
        islogin=False
        login_user=""
        lbl.configure(text="your account is deleted!",fg="green")
        win1.destroy()
        return        
        
    def no():
        lbl.configure(text="ok,cancel!",fg="blue")
        win1.destroy()
        return
            
############################## yes\no button
    btnYes=tkinter.Button(win1,text="YES",command=yes).place(x=80,y=110)
    btnNo=tkinter.Button(win1,text="NO",command=no).place(x=110,y=110)
        
def usersList():
    global login_user
    if login_user!="admin":
        lbl.configure(text="just admin can!",fg="red")
        return
    with open("login.json") as f:
        logins=json.load(f)
    for user in logins:
        lstbx.insert("end",user)

        
win=tkinter.Tk()
win.title('win1')
win.geometry('360x450')
win.configure(bg="#CACAFF")

############################## make label
lbl=tkinter.Label(win,text="hello!",fg="#6E6E8B")
lbl.pack()
lbl.place(x=110,y=20)
lbl2=tkinter.Label(win,text = "Username")
lbl2.pack()
lbl2.place(x=40,y=60)
lbl3=tkinter.Label(win,text = "Password") 
lbl3.pack()
lbl3.place(x=40,y=90)

lstbx=tkinter.Listbox(win)
lstbx.pack()
lstbx.place(x=110,y=210)

############################## make entry
txt_user=tkinter.Entry(win,width=20)
txt_user.place(x=110,y=60)

txt_passw =tkinter.Entry(win,width=20)
txt_passw.place(x=110,y=90)

############################## make button
btnLogin=tkinter.Button(win,text="login",command=login).place(x=40,y=130)
btnSubmit=tkinter.Button(win,text="submit",command=submit).place(x=100,y=130)
btnLogout=tkinter.Button(win,text="logout",command=logout).place(x=160,y=130)
btnDelete=tkinter.Button(win,text="delete account",command=deleteAcc).place(x=220,y=130)
btnLoginusers=tkinter.Button(win,text="login users",command=usersList).place(x=135,y=175)
##btnChangepass=tkinter.Button(win,text="change password",command=changePass)


win.mainloop()


