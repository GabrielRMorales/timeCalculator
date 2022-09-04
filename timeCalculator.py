def add_time(start, duration, day="Sunday"):
    start_time = { }
    duration_time = { }
    #extrapolate hours, minutes, and AM/PM from start
    #convert hours/minutes to int
    start_time["hours"] = start.split(":")[0]
    start_time["minutes"] = start.split(":")[1].split(" ")[0]
    start_time["am_or_pm"] = start.split(" ")[1]
    print(start_time)
    #extrapolate hours, minutes from duration
    duration_time["hours"] = duration.split(":")[0]
    duration_time["minutes"] = duration.split(":")[1]
    print(duration_time)
    #convert hours/minutes to int

    #add duration minutes to start minutes
        #calculate if it goes beyond 60-if so add 1 to start hour

    #add duration hour to start hour
        #calculate if it goes beyond 12
            #use % 12?
        #calculate if it's AM or PM
        #calculate if it's a N days later
            #use % 24?

            #if 1, use (next day)
            #if >1, use (N days later)
        
    #print result

#ex: add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("3:00 PM", "3:10")

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

#add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

#add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

#add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

#add_time("6:30 PM", "205:12")