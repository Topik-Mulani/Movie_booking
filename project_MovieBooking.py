movie = {"xyz":[20,20,20],"pqr":[20,20,20],"abc":[20,20,20]}
info = []


while True :
     var = input("""
     1. Booking
     2. Owner 
     3. exit : """)
     if var == "1":
          mo_name = input("""
          1. xyz 500/-PT
          2. pqr 500/-PT
          3. abc 500/-PT  : """)
          if mo_name == "1":
               time = input(f"""
               1 9-12 AM : {movie["xyz"][0]}
               2 1-3  PM : {movie["xyz"][1]}
               3 5-8  PM :  {movie["xyz"][2]}  : """)
               if time == "1":
                    no_se = int(input("no of seat : "))
                    if no_se <=movie["xyz"][0] :
                         phone = int(input("enter your no : "))
                         bill = no_se*500
                         y_n = input(f"your bill : {bill} y/n : ")
                         if y_n == "y" :
                              print("booked")
                              info.append([phone,"xyz","9-12 AM",no_se,bill])
                              movie["xyz"][0] = movie["xyz"][0] - no_se
                         else :
                              print("thank you : ")
                    else :
                         print("wrong input : ")
               elif time == "2":
                    no_se = int(input("no of seat : "))
                    if no_se <=movie["xyz"][1] :
                         phone = int(input("enter your no : "))
                         bill = no_se*500
                         y_n = input(f"your bill : {bill} y/n : ")
                         if y_n == "y" :
                              print("booked")
                              info.append([phone,"xyz","1-3  PM",no_se,bill])
                              movie["xyz"][1] = movie["xyz"][1] - no_se
                         else :
                              print("thank you : ")
                    else :
                         print("wrong input : ")
               elif time == "3":
                    no_se = int(input("no of seat : "))
                    if no_se <=movie["xyz"][2] :
                         phone = int(input("enter your no : "))
                         bill = no_se*500
                         y_n = input(f"your bill : {bill} y/n : ")
                         if y_n == "y" :
                              print("booked")
                              info.append([phone,"xyz","5-8  PM",no_se,bill])
                              movie["xyz"][2] = movie["xyz"][2] - no_se
                         else :
                              print("thank you : ")
                    else :
                         print("wrong input : ")
               else :
                    print("wrong input : ")



          elif mo_name == "2":
               time = input(f"""
               1 9-12 AM : {movie["pqr"][0]}
               2 1-3  PM : {movie["pqr"][1]}
               3 5-8  PM :  {movie["pqr"][2]}  : """)
               if time == "1":
                    no_se = int(input("no of seat : "))
                    if no_se <=movie["pqr"][0] :
                         phone = int(input("enter your no : "))
                         bill = no_se*500
                         y_n = input(f"your bill : {bill} y/n : ")
                         if y_n == "y" :
                              print("booked")
                              info.append([phone,"pqr","9-12 AM",no_se,bill])
                              movie["pqr"][0] = movie["pqr"][0] - no_se
                         else :
                              print("thank you : ")
                    else :
                         print("wrong input : ")
               elif time == "2":
                    no_se = int(input("no of seat : "))
                    if no_se <=movie["pqr"][1] :
                         phone = int(input("enter your no : "))
                         bill = no_se*500
                         y_n = input(f"your bill : {bill} y/n : ")
                         if y_n == "y" :
                              print("booked")
                              info.append([phone,"pqr","1-3  PM",no_se,bill])
                              movie["pqr"][1] = movie["pqr"][1] - no_se
                         else :
                              print("thank you : ")
                    else :
                         print("wrong input : ")
               elif time == "3":
                    no_se = int(input("no of seat : "))
                    if no_se <=movie["pqr"][2] :
                         phone = int(input("enter your no : "))
                         bill = no_se*500
                         y_n = input(f"your bill : {bill} y/n : ")
                         if y_n == "y" :
                              print("booked")
                              info.append([phone,"pqr","5-8  PM",no_se,bill])
                              movie["pqr"][2] = movie["pqr"][2] - no_se
                         else :
                              print("thank you : ")
                    else :
                         print("wrong input : ")
               else :
                    print("wrong input : ")

          elif mo_name == "3":
               time = input(f"""
               1 9-12 AM : {movie["abc"][0]}
               2 1-3  PM : {movie["abc"][1]}
               3 5-8  PM :  {movie["abc"][2]}  : """)
               if time == "1":
                    no_se = int(input("no of seat : "))
                    if no_se <=movie["abc"][0] :
                         phone = int(input("enter your no : "))
                         bill = no_se*500
                         y_n = input(f"your bill : {bill} y/n : ")
                         if y_n == "y" :
                              print("booked")
                              info.append([phone,"abc","9-12 AM",no_se,bill])
                              movie["abc"][0] = movie["abc"][0] - no_se
                         else :
                              print("thank you : ")
                    else :
                         print("wrong input : ")
               elif time == "2":
                    no_se = int(input("no of seat : "))
                    if no_se <=movie["abc"][1] :
                         phone = int(input("enter your no : "))
                         bill = no_se*500
                         y_n = input(f"your bill : {bill} y/n : ")
                         if y_n == "y" :
                              print("booked")
                              info.append([phone,"abc","1-3  PM",no_se,bill])
                              movie["abc"][1] = movie["abc"][1] - no_se
                         else :
                              print("thank you : ")
                    else :
                         print("wrong input : ")
               elif time == "3":
                    no_se = int(input("no of seat : "))
                    if no_se <=movie["abc"][2] :
                         phone = int(input("enter your no : "))
                         bill = no_se*500
                         y_n = input(f"your bill : {bill} y/n : ")
                         if y_n == "y" :
                              print("booked")
                              info.append([phone,"abc","5-8  PM",no_se,bill])
                              movie["abc"][2] = movie["abc"][2] - no_se
                         else :
                              print("thank you : ")
                    else :
                         print("wrong input : ")
               else :
                    print("wrong input : ")
          else :
               print("wrong input : ")

     elif var == "2":
          code = input("enter your code : ")
          if code =="qwe123":
               for i in info :
                    print(i)
          else :
               print("wrong code : ")
     elif var == "3":
          print("thank you : ")
          break
     else :
          print("wrong input:")