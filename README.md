# Tracking-Efficiency-on-AWS-using-Jmeter

Frequently cloud service based systems need to support thousands or even millions of users (or subscribers) often simultaneously.
To support so many users the cloud services need to automatically scale. Scaling should be done both by scaling up to handle ever increasing demand, 
and then scaling back down to avoid being charged for unused and unneeded service.
This is implemented using Load balancers and Auto scaling groups on AWS that spawn instances based on incoming traffic. 
Traffic to the website is generated using Jmeter.
