Download a serverless template:
	serverless create --template aws-python --path hello-world-python

Invoke serverless function locally:
	serverless invoke -f hello -l

Deploying a function and create stack:
	serverless deploy
	
Deploy only the function(in case you update a function body):
	serverless deploy function -f hello
	
Check logs of a function:
	serverless logs -f hello -t
	
Remove a deployed function and delete stack:
	serverless remove
	

