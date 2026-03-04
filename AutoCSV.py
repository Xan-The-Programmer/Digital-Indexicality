import Link_to_CSV as ltc

def Auto():
    #this program is meant to be run in a split window with the word document at 160%
    ltc.GetLink(First = True)

    while True:
    
        ltc.LinkTrigger("https://igcomment.com/tiktok-display-comments/", 10)
        ltc.LoadComments()
        ltc.click_download()
        ltc.ScreenshotTrigger(ltc.file_confirmed)
        ltc.page_back()
        ltc.GetLink()

Auto()

