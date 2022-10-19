# Tweet scheduler

This is my tweet scheduler I made because I've noticed that most famous people or people that are active on twitter use tweet schedulers for their account. There are a few different websites that can provide this service but cost a subscription fee. So I thought it would be fun to create one myself.

I use as flask homepage to create the form that takes in the information for the tweet like the message, time and password I created for the app. The time used for the app uses a 24 hour clock style and is on the Mountain Standard Time zone. The date for when the tweet is sent use a YYYY-MM-DD format. I use a google sheet to store the scheduled tweet, time and if the tweet has been sent to the twitter page.

## Screenshots

Main Screen
![Main Screen](/screenshots/main.png?raw=true)
You can see in this screenshot that there are no tweets scheduled and they are 3 tweets that have already been sent. I can delete the already sent tweets or the tweets that are scheduled to be sent, by clicking the delete button.

---

Tweet Scheduled
![Tweet Scheduled](/screenshots/tweetscheduled.png?raw=true)
In this screenshot you can see that there is one tweet scheduled to be sent. In the background there is a worker script that will continuously run and check if the time has passed and if it has it will send the tweet.

---

Google Sheet
![Google Sheet](/screenshots/googlesheet.png?raw=true)
