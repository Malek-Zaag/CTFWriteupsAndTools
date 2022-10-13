# cookauth

<img src="">
We open the link and we get the following page 
<img src="">

We notice from the challenge description that it is a cookie challenge , so we inspect the cookie and we find the following
<img src="">

We notice that it is a hexa value , we decode it we find {"user" : "guest"}, we change guest to admin , we encode as hexa again and we put the new value , we reload the page and boom

<img src="">
The flag is CyberErudites{7H1$_WA$_T0O_wE4k_FOR_4_VAlID471on}
