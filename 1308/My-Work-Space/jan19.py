# class Student:
#     c_name="TKA"

#     # class variable
#     def __init__(self,r,n,m):
#         self.roll=r
#         self.name=n
#         self.marks=m

#     # Instance Variable
#     def displayAllDetails(self):
#         print(self.roll)
#         print(self.name)
#         print(self.marks)
    
#     def getRoll(self):
#         return self.roll
    
#     def getName(self):
#         return self.name

#     def getMarks(self):
#         return self.marks


# s1=Student(1,"Jay",88)
# print(s1.getRoll())
# print(s1.getName())
# print(s1.getMarks())





# class Student:
#     c_name="TKA"

#     # class variable
#     def __init__(self,r,n,m):
#         self.roll=r
#         self.name=n
#         self.marks=m

#     # Instance Variable
#     @classmethod
#     def displayCollage(cls):
#         print(cls.c_name)

#     def displayCollage1(self):
#         print(self.c_name)
#         print(self.roll)

#     @classmethod
#     def updateCollage2(cls,nc):
#         cls.c_name=nc

# s1=Student(2,"Prem",98)
# Student.updateCollage2("JBK")
# s1.displayCollage()
# s1.displayCollage1()




# class Student:
#     c_name="TKA"

#     # class variable
#     def __init__(self,r,n,m):
#         self.roll=r
#         self.name=n
#         self.marks=m

#     # Instance Variable
#     @classmethod
#     def displayCollage(cls):
#         print(cls.c_name)

#     def displayCollage1(self):
#         print(self.c_name)
#         print(self.name)

#     @staticmethod
#     def Cal_percentage(m1,m2,m3,m4,m5):
#         total=m1+m2+m3+m4+m5
#         per=(total/500)*100
#         print(per)

# s1=Student(2,"Prem",98)
# s1.Cal_percentage(88,89,95,98,90)
# s1.displayCollage()
# s1.displayCollage1()




class Player:
    # Constructor
    def __init__(self, jersey_no, p_name, runs, wickets, team_name):
        self.jersey_no = jersey_no
        self.p_name = p_name
        self.runs = runs
        self.wickets = wickets
        self.team_name = team_name

    # ---------- GET METHODS ----------
    def getJerseyNo(self):
        return self.jersey_no

    def getName(self):
        return self.p_name

    def getRuns(self):
        return self.runs

    def getWickets(self):
        return self.wickets

    def getTeamName(self):
        return self.team_name

    # ---------- UPDATE METHODS ----------
    def updateJerseyNo(self, jno):
        self.jersey_no = jno

    def updateName(self, name):
        self.p_name = name

    def updateRuns(self, runs):
        self.runs = runs

    def updateWickets(self, wickets):
        self.wickets = wickets

    def updateTeamName(self, team):
        self.team_name = team

    # Display method
    def displayPlayer(self):
        print("Jersey No :", self.jersey_no)
        print("Name      :", self.p_name)
        print("Runs      :", self.runs)
        print("Wickets   :", self.wickets)
        print("Team Name :", self.team_name)


S1 = Player(18, "Virat", 12000, 4, "India")

S1.displayPlayer()

print("\nAfter Update:\n")
S1.updateRuns(12500)
S1.updateTeamName("RCB")

S1.displayPlayer()
