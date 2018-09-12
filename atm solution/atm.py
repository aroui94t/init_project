
def atm(request,amount):
    # variables for calculate count paper cash
    paper_100 = 0
    paper_50  = 0
    paper_10  = 0
    paper_5   = 0
    rest      = 0
    
    
    print "The number of amount is:"+str(amount)
    if request > amount:
        print "sorry,you can not extract this amount "
    else:
        while request > 0:
            if request >= 100:
                request -=100
                paper_100+=1
                print "give 100"
            elif request >=50:
                request -= 50
                paper_50+=1
                print "give 50"
            elif request >= 10:
                request -= 10
                paper_10+=1
                print "give 10"
            elif request>=5:
                request -= 5
                paper_5+=1
                print "give 5"
            else:
                rest+=1
                print"give "+str(request)
                break
        
        
        if paper_100 >=1:
             print "count paper 100 : "+  str(paper_100) +" papers"
        if paper_50 >= 1:
             print "count paper 50 : "+ str(paper_50) + " papers"
        if paper_10 >= 1:
             print "count paper 10 : " + str(paper_10) + " papers"
        if paper_5 >= 1:
             print "count paper 5 : " + str(paper_5) +" papers"
        else:
             print "rest : " + str(rest)       

atm(245,500)
