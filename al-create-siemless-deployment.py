# SIEMLESS DEPLOYMENT SCRIPT
# Currently for AWS Deployment (Not Including Scope Configuration)

#This script will help you create the credential file in the AL backend and 
#then use it to create a manual deployment.

#You need to have already created the SIEMless manual IAM Role, and have the
#Role ARN and external ID values
#Contributers - Tambu Ebuta, Gabrielle Crawford, Shane Davis, Kyle Butcher, Greg Ryan

#banner

print("    ___    __       _____ ____________  _____              ")
print("   /   |  / /      / ___//  _/ ____/  |/  / /__  __________")
print("  / /| | / /       \__ \ / // __/ / /|_/ / / _ \/ ___/ ___/")
print(" / ___ |/ /___    ___/ // // /___/ /  / / /  __(__  |__  ) ")
print("/_/ _||/_____|_  |____/___/_____/_/  /_/__|___/____/____/  ")
print("   /   |  / __ \/  _/  / __ \___  ____  / /___  __  __     ")
print("  / /| | / /_/ // /   / / / / _ \/ __ \/ / __ \/ / / /     ")
print(" / ___ |/ ____// /   / /_/ /  __/ /_/ / / /_/ / /_/ /      ")
print("/_/  |_/_/   /___/  /_____/\___/ .___/_/\____/\__, /       ")
print("                              /_/            /____/        \n\n")
print("Alert Logic Deployment Tool - 2019 - v1.0\n")

#Get Customer Email
#username=input('Enter AL User Email Address: ')

#Get Customer Password
password=input('Enter Password: ')

#Get Key
key=input('Enter Key: ')
