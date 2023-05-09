---
title: "How to Bypass the Invisible Malicious Ad Button"
date: 2023-05-08T14:31:47-05:00
draft: false
description: "How a malicious website design leads to uBlock"
tags: ["tech"]
type: post
weight: 25
showTableOfContents: true
---

![](/images/Pasted%20image%2020230508144818.png)

# Disclaimer
The Copyright Act of 1976 grants copyright holders “exclusive rights” to make copies of their work, distribute it and perform it publicly.  And an individual user's watching a stream — even if it’s unauthorized by the copyright holder — doesn’t technically violate these rights.[^1] Plus, I have Prime Video membership. I just don't use it that often. 
# Problem
When I was rewatching (Shaun of the Dead)[https://www.imdb.com/title/tt0365748/] on some mysterious [website](https://xiaobaotv.net/index.php/vod/play/id/41003/sid/1/nid/1.html), I tried to fast forward a little, the same thing I have done for a zillion times. Instead, I was redirected to an third-party annoying page. 

![](/images/Pasted%20image%2020230402053620.png)

I would have let it go if the invisible button is gone after I click on it, but it really irritates me when this invisible ad redirector "shows up" every few seconds. I get it. Whoever is responsible for this periodical naughty behavior wants to create an authentic cinematic experience by making it extremely painful for people to pause, fast-forward, or adjust the volume. But you should not be the one to make the call. I should. So I decide to disable this annoying invisible button. 
It's a little trickier than I expected.

# Attempt 1 AdBlocker


![](/images/Pasted%20image%2020230402045938.png)

Given the fact that clicking on any part of the screen would redirct I assume there should be a giant redirector element that overlaps the entire page, the first thing on my mind is to use my AdBlocker's selector to block it. 
It turns out there isn't one. 
That's wierd.
# Attempt 2 Developer Tool
So I decide to dive deeper using the developer tool. 
![](/images/Pasted%20image%2020230402050629.png)
Wait, "Paused in debugger"? 
I keep clicking the F8 (Resume Script Execution), but it keeps back to this breakpoint "debugger".  
![](/images/Pasted%20image%2020230402051007.png)
Obviously this page checks the width between the border and the inner page to detects whether the developer tool is being used. CLassic Anti-Debugger. "The more you hide, the more you stand out."[^2] 
![](/images/Pasted%20image%2020230402052031.png)
Done. By adding it to ignore list, the debugger no longer blocks the script from running even if it cries for help. 
Now let's see how it works.

# Attempt 3 Network Analysis
![](/images/Pasted%20image%2020230402053041.png)
It seems that there are mainly 2 kinds of requests going on. One is the medix_xxx.ts, which contains the media data. The other, however, look much more suspicious, whose response contains a url.
![](/images/Pasted%20image%2020230402053454.png)
Let's see where you leads to.
![](/images/Pasted%20image%2020230402053620.png)
Aha. Gotcha. This is exactly got me started. The Developer Tool allows me to trace back to the script that initiates it: [61650:1](https://qg.catdomepimyth.com/tvnWRQVkIKEIujSu/61650). This same script is also clearing my console.
![](/images/Pasted%20image%2020230402054041.png)
Now the only thing left is to locate this script and diable it. Before that, let's take a look at the script.
![](/images/Pasted%20image%2020230402060618.png)
Complete mess. Let's through it to a [JavaScript Beautifier](https://beautifier.io/). 
![](/images/Pasted%20image%2020230402061205.png)
A little better, but zero comment. It's never meant to be understood or maintained. The developer tool told me that this snippet is the root cause, so I kept pressing Shift+F12 in VSCode to see who is referencing it and its parents, which finnally lead me to an aync function. 
![](/images/Pasted%20image%2020230402061529.png)

# Disable Specific JavaScript
By searching 61650, I quickly located it in the HTML elements.
![](/images/Pasted%20image%2020230402054240.png)
I can't disbale the whole JavaScript because it's also used to stream, so [uBlock](https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm) comes in handy because it allows you to develop custome rules to block scripts such as those that . Done! I gained my control back!

[^1]:  [When is streaming illegal?](https://www.allconnect.com/blog/is-streaming-illegal#:~:text=Watching%20a%20stream%20of%20unlicensed,it%20and%20perform%20it%20publicly.)
[^2]:  Quote from a reverse engineer [Jason Batchelor](https://github.com/jxb5151)
