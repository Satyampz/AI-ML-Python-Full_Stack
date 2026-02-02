fd = open("demo.txt","a")

data="\nGo to next \t\t line"

l=["hello\n", "All !!!\n", "Good Morning\n"]
fd.writelines(l)

fd.close()