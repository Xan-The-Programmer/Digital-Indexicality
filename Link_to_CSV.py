import pyautogui #Pyautogui is used for the majority of desktop simulation
import pyperclip #pyperclip is used to read from the local clipboard for certain trigger events
import time #time is used for some miscelanous timing on the browser end
import Playback as p

Captcha = 'C:/Users/david/OneDrive - Osceola County School District/2025-2026 School Year/AP Research Evans Xan/Data Collection/Code/Assets/CAPTCHA.png'
loadbutton = 'C:/Users/david/OneDrive - Osceola County School District/2025-2026 School Year/AP Research Evans Xan/Data Collection/Code/Assets/loadb.png'
Load_1 = 'C:/Users/david/OneDrive - Osceola County School District/2025-2026 School Year/AP Research Evans Xan/Data Collection/Code/Assets/load_more.png'
Load_2 = 'C:/Users/david/OneDrive - Osceola County School District/2025-2026 School Year/AP Research Evans Xan/Data Collection/Code/Assets/load2.png'
download = 'C:/Users/david/OneDrive - Osceola County School District/2025-2026 School Year/AP Research Evans Xan/Data Collection/Code/Assets/download.png'
back = 'C:/Users/david/OneDrive - Osceola County School District/2025-2026 School Year/AP Research Evans Xan/Data Collection/Code/Assets/back.png'
wnload = 'C:/Users/david/OneDrive - Osceola County School District/2025-2026 School Year/AP Research Evans Xan/Data Collection/Code/Assets/wnload.png'
checkmark = 'C:/Users/david/OneDrive - Osceola County School District/2025-2026 School Year/AP Research Evans Xan/Data Collection/Code/Assets/checkmark.png'
file_confirmed = 'C:/Users/david/OneDrive - Osceola County School District/2025-2026 School Year/AP Research Evans Xan/Data Collection/Code/Assets/file_confirmed.png'
end_scroll = 'C:/Users/david/OneDrive - Osceola County School District/2025-2026 School Year/AP Research Evans Xan/Data Collection/Code/Assets/end_scroll.png'

def GetLink(First = False):
    #This function contains the main code for copy and pasting a link from a word document into the igcomment website and submitting them


    # setting the initial x and y mouse position
    x,y = 1225,460

    pyautogui.moveTo(x,y)

    #Tripple clicking does three things:

    # The first click activates the word window
    # The second click brings the cursor to the left end of the line
    # The third click se5lects the entire line

    if First:
        pyautogui.tripleClick()

    else:

        pyautogui.click()
        pyautogui.press('down')
        pyautogui.press('up')
        pyautogui.keyDown('shift')
        pyautogui.press('down')
        pyautogui.keyUp('shift')
        


    pyautogui.hotkey('ctrl', 'c') #copy the selected line

    # move to the TikTok Comment Viewer

    pyautogui.moveTo(500,600)

    # enter text box
    pyautogui.doubleClick()

    #select all text
    pyautogui.hotkey('ctrl', 'a')

    #delete whatever was there
    pyautogui.press('backspace')

    #paste link
    pyautogui.hotkey('ctrl','v')

    #Go down to submit button
    pyautogui.moveTo(500,800)  
    #click submit button
    ScreenshotTrigger(checkmark)

    pyautogui.click()

    #let the submit process
    time.sleep(10)

def LinkTrigger(target, timeout = 2):
    #clip will basically hold whatever is currently in the clipboard
    clip = ""
    itime = 0

    while itime < timeout and clip != target:
        #checks browser url and keeps looping until timeout or found target
        urlx, urly = 500, 85
        pyautogui.moveTo(urlx, urly)

        #click into url bar, by default this selects the entire url
        pyautogui.click()

        #copy url into clipboard
        pyautogui.hotkey('ctrl','c')

        #click off the url before doing the next comparison
        pyautogui.moveTo(urlx + 300, urly + 400)
        pyautogui.click()
        
        #increments time to actually enforce timeout
        time.sleep(1)
        itime += 1

        #save copied text to clip

        clip = pyperclip.paste()
        print(clip)

    if itime >= timeout:
        raise Exception(f"LinkTrigger has timed out while waiting for {target}")

    else:
        print("Success!")

def click_image(image, find = False):

    if find:
        image = ScreenshotTrigger(image, local = True)

    cord = pyautogui.center(image)

    pyautogui.moveTo(cord.x, cord.y)

    pyautogui.click()

def LoadComments():
    #This function's only job is to get the webpage to load the neccessary amount of comments
        pyautogui.moveTo(800,485)

        #move to load button
        cord = ScreenshotTrigger(Load_1, local = True, scrollsearch = True)

        click_image(cord)

        ScreenshotTrigger(wnload, NOTFLAG= True)
        ScreenshotTrigger(wnload, local = True, scrollsearch = True)
        

def ScreenshotTrigger(image, NOTFLAG = False, local = False, scrollsearch = False):
    #Keeps checking for an image or for the lack of an image, based on NOTFLAG
    
    TRY_AGAIN = True

    while TRY_AGAIN:

        if scrollsearch:
            for i in range(10):

                pyautogui.scroll(-1000)

        #check for the given image
        try:
            load_location = pyautogui.locateOnScreen(image)
            print(f"Image: {image} found")
            print(load_location)

            #if NOTFLAG is false, as by default, then once the image is detected, we're done
            if not NOTFLAG:

                if local:
                    return load_location
                
                else:
                    return 0
                
            if NOTFLAG:

                print(f"Image: {image} still detected")

        except pyautogui.ImageNotFoundException:
            print(f"Image: {image} not found")
            #if the image is not detected, the behavior is determined be NOTFLAG

            #if NOTFLAG is true, then not finding the image means we are done waiting, and the rest of the code can be executed
            if NOTFLAG:

                TRY_AGAIN = False

            #if NOTFLAG is false, as by default, then we just check again
            else:
                
                continue

    return 1

def click_download():
    click_image(wnload, True)

def page_back():
    click_image(back, True)

