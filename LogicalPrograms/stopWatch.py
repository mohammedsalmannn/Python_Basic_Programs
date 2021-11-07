def stopWatch():
    from timeit import default_timer as timer
    from datetime import timedelta
    start_watch=int(input("Enter To Start The Watch:"))
    end_watch=int(input("Enter To Stop The Watch:"))
    start_watch=timer()
    end_watch=timer()
    print("Elapsed Time In Seconds:")
    print(timedelta(end_watch - start_watch))
stopWatch()