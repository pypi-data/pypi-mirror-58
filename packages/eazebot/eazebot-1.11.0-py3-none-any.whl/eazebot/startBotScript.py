try:
    import os.path
    # check if script is started from package folder or not
    if os.path.isfile('EazeBot.py') :
        from EazeBot import *
    else:
    	from eazebot.EazeBot import *
    start_bot()
except Exception as e:
    print('An error occured:\n%s\n\nPress Enter to abort'%str(e))
    input()