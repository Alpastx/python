def converter(N):
    print("bytes:",N)
    print("kilobytes:",N/1024)
    print("megabytes:",N/(1024**2))
    print("gigabytes:",N/(1024**3))
    print("terabytes:",N/(1024**4))
N = int(input("Enter the amount in bytes: "))
converter(N)