# class Player:
    
#     def __init__(self,jn,pn,r,w,tn):
#         self.j_no=jn
#         self.p_name=pn
#         self.runs=r
#         self.wicket=w
#         self.t_name=tn

#     def display(self):
#         print(f"player name is {self.p_name} and runs are {self.runs}")

# obj=Player(18,"Virat",7878,10,"RCB")
# print(obj.runs)



# class Player:
    
#     def __init__(self,jn,pn,r,w,tn):
#         self.__j_no=jn
#         self.__p_name=pn
#         self.__runs=r
#         self.__wicket=w
#         self.__t_name=tn

#     def get_JerseyNo(self):
#         return self.__j_no

#     def set_JerseyNo(self,nj):
#         self.__j_no= nj

# p1=Player(45,"Rohit",6767,10,"MI")
# print(p1.__runs)

# jn=p1.get_JerseyNo()
# print(jn)
# p1.set_JerseyNo(46)
# jn=p1.get_JerseyNo()
# print(jn)





class Player:
    
    def __init__(self,jn,pn,r,w,tn):
        self.__j_no=jn
        self.p_name=pn
        self._runs=r
        self.__wicket=w
        self.__t_name=tn

    def __str__(self):
        return f"{self.__j_no} and {self.p_name}"

    

p1=Player(45,"Rohit",6767,10,"MI")
print(p1)

# jn=p1.get_JerseyNo()
# print(jn)
# p1.set_JerseyNo(46)
# jn=p1.get_JerseyNo()
# print(jn)