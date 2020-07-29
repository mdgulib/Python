
#something more about functions!!!!---------------

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Positional argument<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
# def infos(name,city,number):
#     print(f"hello {name} ,hope you are well in your {city} city.We are sending a code at {number}")
# # infos("shahriar" , "Dhaka" , "+8801701394789") #order is compulsory
# # infos( city= "Dhaka" ,number= "+8801701394789",name="shahriar") # order is optional here


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Default argument<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
# def infos(name , number,city = "Dhaka"):
#          print(f"hello {name} ,hope you are well in your {city} city.We are sending a code at {number}")
# """
# infos(name ="Kawser" , city ="chittagong" , number  = 99012312123)
# infos(name ="Arif" , number  = 99012312123)"""

# infos("kawsar" , 909101292 , "Rangpur")
# infos("Arif" , 909101292)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Optional Argument<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#

# def infos(name , age , city=''):
#     if city:
#         print(f'My name is {name} , I am {age} years old and I am from {city}')
#     else:
#         print(f'My name is {name} , I am {age} years old')

# infos("Kawsar" , 22 , "Dhaka")
# infos("Arif" , 29)



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Arbitary number of Argument<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#

# def students(*roll):
#     print(roll , type(roll))
#     for i in roll:
#         print(i)
# students(98,99,100,101,102,103)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Arbitary number of Positional Argument<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#

def players(player1,player2,player3,*other_players):
    print('Main captain is' , player1)
    print()
    print('Second captain is ', player2)
    print()
    print('3rd captain is ', player3)
    print()
    print('Others are' , end=' ')
    
    for i in other_players:
        print(i , end=" ")
    print()

players("Shakib" , "Mashrafe" , "Mushfiqur" , "Sabbir" , "Mahmudullah" , "Miraz")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Arbitary number of Keyword Argument<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#


# def players(player1 , player2 , **others):
#     print(player1)
#     print(player2)
#     print(others)
# players(player1 = "Abir" , player2 = "Sabbir" , lame_1 = "rafid" , lame_2 = "simin" ,lame_3 = "abdul")

















































# password = "127JHINUKshahriar"
# def check_pass():
#     tries = 3
#     while True:
#         password = input("Enter his password")
#         if password=="1234":
#             print("Entering the database....")
#             break
#         else:
#             tries-=1
#             if(tries<1):
#                 print("Sorry you cannot try to login for next 24 hours")
#                 break
#             else:
#                 print(f"Wrong password! , you have {tries} chance(s) left")


# choices = input("Galib's Database or Arif? : ")
# if choices=="Galib":
#     check_pass()
# else:
#     print(f"Sorry {choices} database is not available right now")