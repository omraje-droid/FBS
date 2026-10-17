#1. position parameter  was used in default parameter.
#2. for neglect the position parameter we use the keyword parameter.
#3. Position parameter was flow from left to right
# means assigned the vales in left to right sequenc.


def mi(id , clg , fees , date ):
    return f'ID = {id} \nCLG = {clg} \nFEES ={fees} \nDATE = {date}' 

res = mi(1234 , 'Hi TECH ' , 48700 , "12/10/2026")
print(res)

print("########################################################")
def me(name , age , BOD ):
    print("NAME :",name)
    print("Age :", age)
    print("BOD :", BOD)
me(21,'OM DESHMANE',"18/02/2005")
print("######################################")
me(name = "Om" , age = 21 , BOD = "18/02/2005")


# We can in both code if sequence will change they print as it is left to right .