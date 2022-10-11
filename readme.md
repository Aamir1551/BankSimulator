Mini project.

You will need to have python version 3 to run this program. Simply type python3 main.py
This is a simple program where others can login/logout and deposit/withdraw a certain amount of cash.

Acts like a simple online bank account. Ideally, you wouldn't be storing username/passwords like this (although passwords are hashed), you would use something like AWS cognito or maybe use a database. 

If this piece of program were to have a frontend, I would prefrebly use vue.js + javascript + html/css. I wouldn't really use something like bootstrap or some other css framework since this is a fairy lightweight site. 

Finally, this is currently just done in loop, this is HORRIBLE, if given the time, I would ideally have a webpage (url and routing all done via ROUTE53), and maybe use a serverless architecture (lambads possibly...), or maybe since its pretty simple I would look into just using AWS ec2 instances that server as web servers + load balances if I had enough users.
