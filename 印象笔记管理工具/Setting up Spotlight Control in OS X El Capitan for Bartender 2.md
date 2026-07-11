# Setting up Spotlight Control in OS X El Capitan for Bartender 2

---

Setting up Spotlight Control in OS X El Capitan for Bartender 2
===============================================================

OS X El Capitan introduced a new Security Feature called System Integrity Protection. With System Integrity Protection Bartender 2 needs additional setup steps performed before it can control Spotlight. Bartender 2 can control all other Apple menu items without these additional steps.

Unfortunately we cannot automate all of the setup and Bartender 2 will need you to temporarily disable System Integrity Protection to allow it to install its System Item control component, System integrity Protection can then be re-enabled.

**Apple have made the steps to temporarily disable SIP quite difficult, so we recommend only performing these steps if you really must control Spotlight with Bartender 2.**

Please follow the instructions below to allow Bartender 2 to control Spotlight.   
(You may wish to print these instructions or open them on another device as you will be restarting OS X).

First you will need to Reboot into OS X's Recovery Mode to Disable System Integrity Protection, to do this:

* Restart your Mac, and as soon as the screen turns black hold down ![](.evernote-content/73C86627-54DF-41DD-B9EE-89735D12DB63/0DABEE5D-44FA-4A98-886A-2D54A7001F4D.png) until the Apple logo appears on your screen.   
  You will know you if you have successfully entered Recovery Mode when the desktop looks like the screenshot below.   
  ![](.evernote-content/73C86627-54DF-41DD-B9EE-89735D12DB63/AC3D5367-D81C-4B27-A023-8A72D8CD7575.png)
* Now click on the "Utilities" menu, and then "Terminal".   
    
  ![](.evernote-content/73C86627-54DF-41DD-B9EE-89735D12DB63/0802D0D3-855F-466B-AEA0-6F2326C99C1B.png)
* In the Terminal Window that opens type:  
    
  **csrutil disable**   
    
  *It may be worth writing the above command down to remember it when in Recovery Mode.*   
    
  Then press the return key, you should then see the following message   
    
  ![](.evernote-content/73C86627-54DF-41DD-B9EE-89735D12DB63/30CE0A23-D31C-42FC-B1F4-00B22AC66475.png)
* Restart OS X, your Mac should then restart as normal with SIP disabled, login and launch Bartender 2, if System Integrity Protection is turned off as it should now be it will ask to install its System Component, press "Continue", you will be prompted for your password.   
  ![](.evernote-content/73C86627-54DF-41DD-B9EE-89735D12DB63/4B604A3B-21C9-44BA-8472-EB1E4D2D1C53.png)<="" li="" style="max-width: 100%; height: auto; border: 0px; width: 600px; display: block; margin-left: auto; margin-right: auto;">

You can now re-enable System Integrity Protection, to do this:

* Restart OS X, as soon as the screen turns black hold down ![](.evernote-content/73C86627-54DF-41DD-B9EE-89735D12DB63/0DABEE5D-44FA-4A98-886A-2D54A7001F4D.png) until the Apple logo appears on your screen.
* Now click on the "Utilities" menu, and then "Terminal".
* In the Terminal Window that opens type:  
    
  **csrutil enable**   
    
  *It may be worth writing the above command down to remember it when in Recovery Mode.*   
    
  Then press the return key, you should then see the following message   
    
  ![](.evernote-content/73C86627-54DF-41DD-B9EE-89735D12DB63/EC0210F7-8763-4A0E-B7FC-55F1A2FD55E9.png)
* Restart OS X, Your Mac should then restart as normal.

Congratulations, Bartender 2 can now control Spotlight and System Integrity Protection is enabled.

[📎 在印象笔记中打开](evernote:///view/207087/s1/8ef97de4-9a54-4a60-91e2-c1687d4e9200/8ef97de4-9a54-4a60-91e2-c1687d4e9200/)