from src.connections import connect
import bcrypt
class authorization:
    """"result=0 failure
        result=1 success
        result=2 user does not exist
        result=3 user already exist (for signup only)
        result=4 unknown error
        result=5 wrong otp"""
    def __init__(self) -> None:
        pass
    def login(self,email:str,password:str):
        try:
            conn=connect()
            cur=conn.cursor()
            cur.execute("select password from `user` where email=%s",email)
            password=password.encode("utf-8")
            if(cur.rowcount==1):
                result=cur.fetchone()
                hashed_password=result[0].encode("utf-8")
                if(bcrypt.checkpw(password,hashed_password)):
                    conn.close()
                    return {"result":1,"name":"rahim","email":email}
                else:
                    conn.close()
                    return {"result":0}
            else:
                conn.close()
                return {"result":2}
        except:
            conn.close()
            return {"result":4}
       
    def signup(self,email:str,password:str):
        password=password.encode('utf-8')
        salt=bcrypt.gensalt()
        hashed_password=bcrypt.hashpw(password,salt)
        try:
            conn=connect()
            cur=conn.cursor()
            cur.execute("insert into user(email,password) values(%s,%s)",[email,hashed_password])
            conn.commit()
            conn.close()
            return{"result":1}
        except:
            return {"result":3}
    
    def reset_password(self,email:str,otp:int,new_password:str):
        try:
            conn=connect()
            cur=conn.cursor()
            cur.execute("select otp from `user` where email=%s",[email])
            if(cur.rowcount==1):
                result=cur.fetchone()
                otp_in_db=result[0]
                if(otp==otp_in_db):
                    new_password=new_password.encode("utf-8")
                    salt=bcrypt.gensalt()
                    hashed_password=bcrypt.hashpw(new_password,salt)
                    cur.execute("insert into user(password) values(%s)",[hashed_password])
                    conn.commit()
                    conn.close()
                    return {"result":1}
                else:
                    conn.close()
                    return {"result":5}
            else:
                conn.close()
                return {"result":2}

        except:
            conn.close()
            return {"result":4}       
# obj=authorization()
# obj.login("j.rahim@codeverse.com","rahim123")
# obj.signup("k.rahim@codeverse.com","rahim123")