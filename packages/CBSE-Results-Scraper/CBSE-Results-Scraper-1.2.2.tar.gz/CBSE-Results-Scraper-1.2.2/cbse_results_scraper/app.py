import os
from selenium import webdriver

class CBSEResultsScraper():
    
    def resultVersion() :

        print("Enter the version of results to be scraped: \n Original(O)  Revised(R)  Compartment(C)")

        VersionFlag = input()

        if VersionFlag == "O":
            Version = Original

        elif VersionFlag == "R":
            Version = Revised

        elif VersionFlag == "C":
            Version = Compartment

        return Version
    
    def schoolCredential() :
        print("Enter school number: ")
        SchoolNo = input()

        return SchoolNo

    def centreCredential() :
        print("Enter the centre number: ")
        CentreNo = input()
        
        return CentreNo
    
    def knowStudentName():
        
        print("Do you know student's name initial? (Y/N)")
        StdFlag = input()
        
        return True if StdFlag == "Y" else False

    def studentNameCredential():
        
        print("Enter the student's first name initial: ")
        StdName = input()
            
        return StdName
    
    def knowMotherName():
        
        print("Do you know student's mother's name initial? (Y/N)")
        MotFlag = input()
        
        return True if MotFlag == "Y" else False
    
    def motherNameCredential():       

        print("Enter the student's mother's first name initial: ")
        MotName = input()
        
        return MotName
    
    def knowRollNumber():
        
        print("Do you know student's exact roll number? (Y/N)")
        RollFlag = input()
        
        return True if RollFlag == "Y" else False
    
    def singleRollNumberCredential():
        
            print("Enter the student's roll number: ")
            RollNum = input()
            
            return RollNum
            
    def multipleRollNumberCredential():
        
            print("Enter the range of roll numbers to check! ")
            
            print("Enter the lower limit roll number to check: ")
            LowRollNum = input()
            
            print("Enter the number of roll numbers to check: ")
            CountRollNum = input()
            
            return LowRollNum, CountRollNum

def main():

    Version = CBSEResultsScraper.resultVersion()
    SchoolNo = CBSEResultsScraper.schoolCredential()
    CentreNo = CBSEResultsScraper.centreCredential()
    
    AdmitId = None
    
    # Checks report if roll number is known
    if CBSEResultsScraper.knowRollNumber():

        knowStudentName = CBSEResultsScraper.knowStudentName()
        knowMotherName = CBSEResultsScraper.knowMotherName()
        RollNum = CBSEResultsScraper.singleRollNumberCredential()
        
        # Checks report if student's initial and mother's initial are known
        if knowStudentName and knowMotherName:
            
            StdName = CBSEResultsScraper.studentNameCredential()
            MotName = CBSEResultsScraper.motherNameCredential()
            
            AdmitId = (
                StdName
                + MotName
                + str(int(RollNum) % 100).zfill(2)
                + str(SchoolNo)[:2]
                + str(int(CentreNo) % 100)
            )
            
            # Opens a browser window
            browser = webdriver.Chrome(executable_path= os.getcwd()+"/chromedriver")
            browser.get((Version))

            regno = browser.find_element_by_name("regno")
            regno.send_keys(RollNum)
            sch = browser.find_element_by_name("sch")
            sch.send_keys(SchoolNo)
            cno = browser.find_element_by_name("cno")
            cno.send_keys(CentreNo)
            admid = browser.find_element_by_name("admid")
            admid.send_keys(AdmitId)
            submitButton = browser.find_element_by_name("B2")
            submitButton.click()

            if Text not in browser.page_source:
                print("Found the report card of "+ RollNum + "!")
                browser.save_screenshot(os.getcwd()+"/Scraped-Results/" + RollNum + " Report.png")
                
            # Closes browser window
            browser.close()

        # Checks report if student's initial is unknown and mother's initial is known
        elif not knowStudentName and knowMotherName:
            
            MotName = CBSEResultsScraper.motherNameCredential()
            
            for alp in Alphabet:
                AdmitId = (
                    alp
                    + MotName
                    + str(int(RollNum) % 100).zfill(2)
                    + str(SchoolNo)[:2]
                    + str(int(CentreNo) % 100)
                )

                # Opens a browser window
                browser = webdriver.Chrome(executable_path= os.getcwd()+"/chromedriver")
                browser.get((Version))

                regno = browser.find_element_by_name("regno")
                regno.send_keys(RollNum)
                sch = browser.find_element_by_name("sch")
                sch.send_keys(SchoolNo)
                cno = browser.find_element_by_name("cno")
                cno.send_keys(CentreNo)
                admid = browser.find_element_by_name("admid")
                admid.send_keys(AdmitId)
                submitButton = browser.find_element_by_name("B2")
                submitButton.click()

                if Text not in browser.page_source:
                    print("Found the report card of "+ RollNum + "!")
                    browser.save_screenshot(os.getcwd()+"/Scraped-Results/" + RollNum + " Report.png")
                    
                # Closes browser window
                browser.close()

        # Checks report if student's initial is known and mother's initial is unknown
        elif knowStudentName and not knowMotherName:
            
            StdName = CBSEResultsScraper.studentNameCredential()
            
            for alp in Alphabet:
                AdmitId = (
                    StdName
                    + alp
                    + str(int(RollNum) % 100).zfill(2)
                    + str(SchoolNo)[:2]
                    + str(int(CentreNo) % 100)
                )

                # Opens a browser window
                browser = webdriver.Chrome(executable_path= os.getcwd()+"/chromedriver")
                browser.get((Version))

                regno = browser.find_element_by_name("regno")
                regno.send_keys(RollNum)
                sch = browser.find_element_by_name("sch")
                sch.send_keys(SchoolNo)
                cno = browser.find_element_by_name("cno")
                cno.send_keys(CentreNo)
                admid = browser.find_element_by_name("admid")
                admid.send_keys(AdmitId)
                submitButton = browser.find_element_by_name("B2")
                submitButton.click()

                if Text not in browser.page_source:
                    print("Found the report card of "+ RollNum + "!")
                    browser.save_screenshot(os.getcwd()+"/Scraped-Results/" + RollNum + " Report.png")
                    
                # Closes browser window
                browser.close()

        # Checks report if student's initial and mother's initial are unknown
        elif not knowStudentName and not knowMotherName:
            
            for alp in Alphabet:
                for bet in Alphabet:
                    AdmitId = (
                        alp
                        + bet
                        + str(int(RollNum) % 100).zfill(2)
                        + str(SchoolNo)[:2]
                        + str(int(CentreNo) % 100)
                    )

                    # Opens a browser window
                    browser = webdriver.Chrome(executable_path= os.getcwd()+"/chromedriver")
                    browser.get((Version))

                    regno = browser.find_element_by_name("regno")
                    regno.send_keys(RollNum)
                    sch = browser.find_element_by_name("sch")
                    sch.send_keys(SchoolNo)
                    cno = browser.find_element_by_name("cno")
                    cno.send_keys(CentreNo)
                    admid = browser.find_element_by_name("admid")
                    admid.send_keys(AdmitId)
                    submitButton = browser.find_element_by_name("B2")
                    submitButton.click()

                    if Text not in browser.page_source:
                        print("Found the report card of "+ RollNum + "!")
                        browser.save_screenshot(os.getcwd()+"/Scraped-Results/" + RollNum + " Report.png")
                        
                    # Closes browser window
                    browser.close()

    # Checks report if roll number is unknown
    else:
        
        knowStudentName = CBSEResultsScraper.knowStudentName()
        knowMotherName = CBSEResultsScraper.knowMotherName()
        RollNum = CBSEResultsScraper.multipleRollNumberCredential()
        
        # Checks report if student's initial and mother's initial are known
        if  knowStudentName and  knowMotherName:
            
            StdName = CBSEResultsScraper.studentNameCredential()
            MotName = CBSEResultsScraper.motherNameCredential()
            
            for i in range(int(RollNum[1])):
                VarRollNum = int(RollNum[0]) + i
                AdmitId = (
                    StdName
                    + MotName
                    + str(int(VarRollNum) % 100).zfill(2)
                    + str(SchoolNo)[:2]
                    + str(int(CentreNo) % 100)
                )

                # Opens a browser window
                browser = webdriver.Chrome(executable_path= os.getcwd()+"/chromedriver")
                browser.get((Version))

                regno = browser.find_element_by_name("regno")
                regno.send_keys(RollNum)
                sch = browser.find_element_by_name("sch")
                sch.send_keys(SchoolNo)
                cno = browser.find_element_by_name("cno")
                cno.send_keys(CentreNo)
                admid = browser.find_element_by_name("admid")
                admid.send_keys(AdmitId)
                submitButton = browser.find_element_by_name("B2")
                submitButton.click()

                if Text not in browser.page_source:
                    print("Found the report card of "+ VarRollNum + "!")
                    browser.save_screenshot(os.getcwd()+"/Scraped-Results/" + VarRollNum + " Report.png")
                    
                # Closes browser window
                browser.close()

        # Checks report if student's initial is unknown and mother's initial is known
        elif not knowStudentName and knowMotherName:
            
            MotName = CBSEResultsScraper.motherNameCredential()
            
            for alp in Alphabet:
                for i in range(int(RollNum[1])):
                    VarRollNum = int(RollNum[0]) + i
                    AdmitId = (
                        alp
                        + MotName
                        + str(int(VarRollNum) % 100).zfill(2)
                        + str(SchoolNo)[:2]
                        + str(int(CentreNo) % 100)
                    )

                    # Opens a browser window
                    browser = webdriver.Chrome(executable_path= os.getcwd()+"/chromedriver")
                    browser.get((Version))

                    regno = browser.find_element_by_name("regno")
                    regno.send_keys(RollNum)
                    sch = browser.find_element_by_name("sch")
                    sch.send_keys(SchoolNo)
                    cno = browser.find_element_by_name("cno")
                    cno.send_keys(CentreNo)
                    admid = browser.find_element_by_name("admid")
                    admid.send_keys(AdmitId)
                    submitButton = browser.find_element_by_name("B2")
                    submitButton.click()

                    if Text not in browser.page_source:
                        print("Found the report card of "+ VarRollNum + "!")
                        browser.save_screenshot(os.getcwd()+"/Scraped-Results/" + VarRollNum + " Report.png")

                    # Closes browser window
                    browser.close()
                    
        # Checks report if student's initial is known and mother's initial is unknown
        elif knowStudentName and not knowMotherName:
            
            StdName = CBSEResultsScraper.studentNameCredential()
            
            for alp in Alphabet:
                for i in range(int(RollNum[1])):
                    VarRollNum = int(RollNum[0]) + i
                    AdmitId = (
                        StdName
                        + alp
                        + str(int(VarRollNum) % 100).zfill(2)
                        + str(SchoolNo)[:2]
                        + str(int(CentreNo) % 100)
                    )

                    # Opens a browser window
                    browser = webdriver.Chrome(executable_path= os.getcwd()+"/chromedriver")
                    browser.get((Version))

                    regno = browser.find_element_by_name("regno")
                    regno.send_keys(RollNum)
                    sch = browser.find_element_by_name("sch")
                    sch.send_keys(SchoolNo)
                    cno = browser.find_element_by_name("cno")
                    cno.send_keys(CentreNo)
                    admid = browser.find_element_by_name("admid")
                    admid.send_keys(AdmitId)
                    submitButton = browser.find_element_by_name("B2")
                    submitButton.click()

                    if Text not in browser.page_source:
                        print("Found the report card of "+ VarRollNum + "!")
                        browser.save_screenshot(os.getcwd()+"/Scraped-Results/" + VarRollNum + " Report.png")
                        
                    # Closes browser window
                    browser.close()

        # Checks report if student's initial and mother's initial are unknown
        elif not knowStudentName and not knowMotherName:
            
            for alp in Alphabet:
                for bet in Alphabet:
                    for i in range(int(RollNum[1])):
                        VarRollNum = int(RollNum[0]) + i
                        AdmitId = (
                            alp
                            + bet
                            + str(int(VarRollNum) % 100).zfill(2)
                            + str(SchoolNo)[:2]
                            + str(int(CentreNo) % 100)
                        )

                        # Opens a browser window
                        browser = webdriver.Chrome(executable_path= os.getcwd()+"/chromedriver")
                        browser.get((Version))

                        regno = browser.find_element_by_name("regno")
                        regno.send_keys(RollNum)
                        sch = browser.find_element_by_name("sch")
                        sch.send_keys(SchoolNo)
                        cno = browser.find_element_by_name("cno")
                        cno.send_keys(CentreNo)
                        admid = browser.find_element_by_name("admid")
                        admid.send_keys(AdmitId)
                        submitButton = browser.find_element_by_name("B2")
                        submitButton.click()

                        if Text not in browser.page_source:
                            print("Found the report card of "+ VarRollNum + "!")
                            browser.save_screenshot(os.getcwd()+"/Scraped-Results/" + VarRollNum + " Report.png")
                        
                        # Closes browser window
                        browser.close()  
                        
if __name__ == '__main__' :
    main()