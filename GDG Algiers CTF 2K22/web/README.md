# cookauth

<img src="https://github.com/Malek-Zaag/CTF-Writeups/blob/main/GDG%20Algiers%20CTF%202K22/web/1.png">
We open the link and we get the following page 
<img src="https://github.com/Malek-Zaag/CTF-Writeups/blob/main/GDG%20Algiers%20CTF%202K22/web/2.png">

We notice from the challenge description that it is a cookie challenge , so we inspect the cookie and we find the following
<img src="https://github.com/Malek-Zaag/CTF-Writeups/blob/main/GDG%20Algiers%20CTF%202K22/web/3.png">

We notice that it is a hexa value , we decode it we find {"user" : "guest"}, we change guest to admin , we encode as hexa again and we put the new value , we reload the page and boom

<img src="https://github.com/Malek-Zaag/CTF-Writeups/blob/main/GDG%20Algiers%20CTF%202K22/web/4.png">
The flag is CyberErudites{7H1$_WA$_T0O_wE4k_FOR_4_VAlID471on}
