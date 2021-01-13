pi = 3.1415926
print("{:.2f}".format(pi)) # 3.14
print("{:,.2f}".format(pi*1000000)) # 3,141,592.60
print("${:,.2f}".format(pi*1000000)) # $3,141,592.60
print("{:.2g}".format(pi*1000000)) # 3.1e+06
print("{:.2e}".format(pi*1000000)) # 3.14e+06
print(f"{pi:.2f}") # 3.14
