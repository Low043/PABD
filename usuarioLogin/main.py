from sqlManager import *
from interfaceMenu import *

database = Database('20221214010004','postgres','localhost','pabd',5432)

#database.createTable('UserLogin',columns=['userName VARCHAR(20) not null','userPassword VARCHAR(20) not null'])
#database.save()

#database.insertIn('UserLogin',['userName','userPassword'],values=["'Usuário'","'Senha'"])
#database.save()

menu = LoginMenu(database)
menu.mainloop()