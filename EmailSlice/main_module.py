from codexplore import emailProcess, printMsg


def main():
    emails = ['buukhanh243@gmail.com', 'youtube243@dev.vku.com', 'thuyngan512@gmail.com']
    for email in emails: 
        username, email_domain = emailProcess(email) 
        printMsg(username,email_domain)
        

if __name__ == '__main__':
    main()