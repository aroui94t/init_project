
def atm(request,amount):
    print "The number of amount is:"+str(amount)
    if request > amount:
        print "sorry,you can not extract this amount "
    else:
        while request > 0:
            if request >= 100:
                request -=100
                print "give 100"
            elif request >=50:
                request -= 50
                print "give 50"
            elif request >= 10:
                request -= 10
                print "give 10"
            elif request>=5:
                request -= 5
                print "give 5"
            else:
                print"give "+str(request)
                break

atm(245,500)
