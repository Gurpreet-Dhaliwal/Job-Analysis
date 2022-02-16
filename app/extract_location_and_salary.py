
#fun to extract the location and the salary from the description 
if __name__ == "__main__":
    l = []
    #call the fun for the list of dict data
    #data = data_extract()
    #print(data[0][0])
    for d in data:
        
        if(len(d) > 0):
            di= {}
            for d1 in d:
                if(len(d1)> 0):

                    #common attributes in both the datasets 
                    di["title"] = d1['title'] 
                    di["link"] = d1['link']
                    di["pubdate"] = d1['pubdate']
                    loc1 = d1["title"].split("-")
                    loc = loc1[-1].split(',')  
                   
                    #if true then indeed job else this job posting in on monster
                    if(len(loc) == 2 and len(loc[1].strip()) ==2):
                        print(d1)
                        di["location"] = loc[0] + ',' + loc[1] 
                        di["job"] = loc1[0]
                        di["company"] = loc1[1]
                        #for extracting the salary
                        payindex = d1["description"].find('$')
                        if(payindex != -1):
                            indexlast = d1["description"].find('an hour')
                            di["salary"] = d1["description"][payindex : indexlast]
                        else:
                            di["salary"] = None
                        print(di)
                    else:
                        des = d1["description"]
                        di["location"] = des.split(",")[0]
                        payindex = des.find('$')
                      
                        if(payindex != -1):
                            lastindex = des[payindex +1 :].find('$')
                            if(lastindex != -1):
                                lastindex = payindex + lastindex
                            else:
                                lastindex = payindex
                            last = des[lastindex +1 :].find(' ')
                            print(des[payindex : last + lastindex + 1] + '\n')
                            di['salary'] = des[payindex : last + lastindex + 1]
            l.append(di)
            
    print(l)  