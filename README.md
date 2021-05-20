# Personalized Email-and-Text-Messages-Scheduler
An application that sends personalized scheduled emails and text messages from a csv file using a python script. The text messages are pushed through an API (In this project I used -ScreenMagicAPI).

***************************************************************************************************
                                           README FILE
***************************************************************************************************

=>Extract the zip file to a desired path say "C:\Downloads\Email_and_Text_Scheduler"

=>If you have a csv file containing required data:

     - Rename and Replace it as Data.csv file in the 'Email_and_Text_Scheduler\Dataset' Folder.

     - If you wish to add new data to the same dataset:
           Append the data manually in the Data.xlsx file and convert it into csv file and then replace
           it as mentioned above.
                         
=> You may also choose to run the project with the already present dataset in the Project.


=> Running the project on the terminal:
    1.Open terminal and type $cd 'path to the project file ex.C:\Downloads\Email_and_Text_Scheduler'
    2.Activate the virtual environment
                You can activate the python environment by running the following command:

                For Mac OS / Linux:
                $source Screenenv/bin/activate

                For Windows:
                $Screenenv\Scripts\activate

    3.To run project type: $python Main_file.py  and hit 'Enter'

=> Running the project on Pycharm IDE:
    1.Open the project folder from the Pycharm IDE.
    2.Select the interpreter - eg:"C:\Downloads\Email_and_Text_Scheduler\Screenenv"
    3.Run the Email_Scheduler file.

Success or Failure of the transactions:

    The success or failure status of the emails and the messages are stored in the Mail_History.txt
     and the Message_History.txt files respectively under the folder 'Email_and_Text_Scheduler\Dataset'.

