I use these two files to display an html file on new tabs w/o extensions.

Paste autoconfig.cfg into /usr/lib/firefox/ and autoconfig.js into /usr/lib/firefox/defaults/pref/

NOTE:
The autoconfig.cfg file contains this line:
" var newTabURL = "file:///home/emermer/Documents/Configs/Firefox/homepagehtml/index.html"; "

As you can see, it contains a file directory that isn't on your system. This file directory tells Firefox what to display on new tabs.
So, if you want to have a custom new tabs homepage like me, you will need to change the file directory to where your html file is located.
The directory should look like this for Firefox to recognize it: file:///path/to/file/index.html

You will need an html file to have a custom homepage. If you don't have one you can either use mine and change it to how you see fit or search up how to get make one.
Video I used to make and customize mine: https://www.youtube.com/watch?v=Hb0p-TxgZzs

ANOTHER NOTE:
In case you want to have your html file display on your homepage, you can change the "Homepage and new windows" setting in Firefox to "Custom URLs...", then just paste the same file directory you used for the autoconfig.cfg file.
