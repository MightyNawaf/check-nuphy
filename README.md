<h1> Checking the availability of Nuphy Keyboard </h1>

This is the credintails for the sender email, you can start off by changing this to your gmail credentials:
```python
server.login("sender@gmail.com", "password")
```

After that change the reciver email:
```python
msg['From'] = "sender@gmail.com" // has to be the same email used in server.login()
msg['To'] = "to@gmail.com"
```

After that you're good to go! <br>
*Note: You can use Crontab in macOS/Linux to automate this process <br>
*Note: When using gmail smtp, you have to allow "less secure apps" from gmail settings

<h1>Usage on other websites</h1>

You can use this script in other webister, just change the URL here: <br>
```python
  r = requests.get('https://nuphy.com/collections/shop/products/nutype-f1?variant=32851509149805')
```

Then try to search for the keywords tht you want to look for in the page by printing the content of the page by using getText() method: <br>
```python
soup.getText()
```

After that just change the if statments to your own cases and that's it :)
