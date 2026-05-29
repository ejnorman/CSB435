OverTheWire 

Find password in readme with cat readme. 

Password: ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If

Password in \- file, did cat \- and had to close command, did cat ./- instead and worked

Password: 263JGJPfgU6LtdEvgfWU1XP5yac29mFx

cat \--spaces in this filename--

cat: unrecognized option '--spaces'

Tried: cat “--spaces in this filename–”, cat –spaces\\ in\\ this\\ filename–

Solution: cat \-- "--spaces in this filename--"

Notes: This took a while even with google searches since I didn’t realize this problem had two parts. \- \- is a flag (that google docs loves to autocorrect).

Password: MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx

cd inhere

ls (nothing shows up)

find (. and ./...Hiding-From-You)

cat ./...Hiding-From-You

Password: 2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ (first try\!)

cd inhere

ls (-file00  \-file01  \-file02  \-file03  \-file04  \-file05  \-file06  \-file07  \-file08  \-file09)

That's a lot of files, so there is another part to the problem, finding what is human readable.

file ./\* 

This ended up showing the type of data in each of the files. file07 had text data while every other one was just data (not human readable)![][image1]

cat ./-file07

Password: 4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw

Ended here.

Time elapsed: \~40 minutes

Hack This Site 

Had to find the password hidden somewhere in the sites HTML. Thought I wouldn’t pass the Idiot Test for a second but found it as a comment below the description text.

Password: 798892f3 

Sam forgot to upload the file to compare my password to. At first I stupidly was looking for the file (that Sam didn’t upload). Then I realized there is no password to compare, so the password is blank.

Sam uploaded the file and set the value to password.php. So I just went to URL/password.php to retrieve the password. 

Password: 6f4bbec4  

Sam now has a script that sends the password to his email. This script is embedded into the site. So I made the script send the password to my email instead of his.

![][image2]

Password: 3c1cd7d6 

![][image3]

The level 5 challenge said Sam made his script more secure, but I did the same thing and I was still able to get the correct password.

Password: 1cd5dbf6 

Sam has now set up encryption for his password. I can see the encrypted value is **dgd4h587** so now I have to decipher the encryption.

Typed a and saw the encrypted version was a. Type abc and saw the encrypted version is ace. Looks like every letter is shifted its own amount. Typed 8 a’s (aaaaaaaa) to figure out the shift. Result: abcdefgh, simple enough. Resulting password is: dfb1d020 

This took longer than expected, especially since I originally encrypted the encrypted password instead of decrypting.

Times up. I kind of wish I did some of the other challenges that weren’t the basic ones.

Time elapsed: \~40 minutes

Google Gruyere 

Started out by reading a paragraph about black box and white box hacking. Black box \- no access to source code. White box \- access to source code. 

Had to: create account, create snippet, create private snippet, look at other account snippets, upload a file. 

This one is a lot wordier than the others.

First challenge: XSS Attack. Inject HTML or JavaScript code into a website. This is a black box technique.

“**Can you upload a file that allows you to execute arbitrary script on the `google-gruyere.appspot.com` domain?** ” Funny thing is when it asked me to upload a file I uploaded a script. No file type sanitization. 

**To exploit,** upload a `.html` file containing a script like this:

\<script\>  
alert(document.cookie);  
\</script\>

To fix this you can host user files on a separate domain so scripts can’t reach the main one. 

I know I’m just reading the answers, but it took a long time to set up this lab and I want to get to the more complicated parts.

Next is a reflected XSS attack. They want me to put the attack into the browser. 

Tried adding \<script\>alert()\</script\> to the end of the webpage URL and it worked.

They say to fix this you need to escape user input. This can be done with the :text modifier  
\<div class="message"\>{{\_message:text}}\</div\>

Now I need to find a way to do a stored XSS.

Lets put the alert script into a new snippet.

Nothing happens and it doesn’t run alert()

Not very familiar with XSS or ways I can exploit this so I’ll use a hint

It says to use some invalid syntax

Tried a couple of things and I don’t seem to be getting anywhere.

It says to use \<p \<script\>alert(1)\</script\>hello

Still didn’t work and the guide explains it. It’s because “Snippets are sanitized in `_SanitizeTag` in the [`sanitize.py`](https://google-gruyere.appspot.com/code/?sanitize.py) file ”. So our exploits are already patched.

The solution: (1') \<a ONMOUSEOVER="alert(1)" href="\#"\>read this\!\</a\>

![][image4]

This works because the sanitization is case sensitive and HTML is not. So if we put ONMOUSEOVER in caps the sanitization doesn’t catch it.

I stopped here since I somehow already hit over 40 minutes. This exercise was very educational but also very challenging.

Summary

The three labs I tested were

* OverTheWire: Use Linux and the command line to access files that contain passwords. It was a lot about learning how to deal with certain edge scenarios, like dashes and spaces, and what to type in the command line to overcome them.  
* HackThisSite: Look at the HTML code of the site to find vulnerabilities based on the challenges. Manipulate the HTML code of the site to your advantage. Also there was a cryptography challenge.  
* GoogleGruyere: A detailed guide that shows many different vulnerabilities that can happen within a website. I mostly explored XSS attacks, how to perform them, and how to fix the site from those types of attacks. 

Which was your favourite penetration lab or testing target?

While each of them had their flaws, I’d like to say that I liked OverTheWire the most. I enjoyed learning the different quirks and techniques of the command line and Linux. I think this is a fun and interactive way to learn this. HackThisSite was cool but I probably should have chosen something harder than basic, like realistic. A lot of the security issues were easy to figure out and probably something that wouldn’t be on an actual website. GoogleGruyere was good but it was very text heavy and took a while to set up. I would probably come back to this if I wanted to learn more about website security, but since I had limited time it wasn’t the right fit.

Based on this experience, what security issues will you now be more aware of? What coding or configuration practices have you identified to reduce risk from the sorts of attacks you practised in these labs?

Based on the command line experience, I will try to avoid having spaces and dashes in my files. Based on HackThisSite, I’ll make sure to set up my password authentication system a bit more securely, maybe use an existing library instead of Sam. Based on Gruyere, I’ll host my files on a separate domain so that malicious code from those files doesn’t leak onto the site itself. Most importantly, Gruyere showed the importance of sanitizing user input and accounting for various exploits like broken HTML and case sensitivity.

 

[image1]: https://github.com/ejnorman/CSB435/blob/main/images/WindowsTerminal_xtvVUfebDe.png

[image2]: https://github.com/ejnorman/CSB435/blob/main/images/SamSentEmail.png

[image3]: https://github.com/ejnorman/CSB435/blob/main/images/HTSBasic6.png

[image4]: https://github.com/ejnorman/CSB435/blob/main/images/StoredXSSGruyere.png
