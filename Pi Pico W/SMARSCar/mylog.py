import time

def log_error(e):
    log=open("log.txt","a") # append
    
    try:
        print("An exception occurred")
        year, month, day, hour, mins, secs, weekday, yearday = time.localtime()
        today = "{}-{:02d}-{:02d} {}:{}:{}".format(year, month, day, hour, mins, secs) # YYYY-MM-DD hh:ss:sss
        print(today)
        
        log.write(today + " - ")
        log.write(str(e)+"\n\n")
    finally:
        log.flush()
