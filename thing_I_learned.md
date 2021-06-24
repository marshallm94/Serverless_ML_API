* Docker registries, repositories, images & tag hierarchy [source](https://play.google.com/books/reader?id=55YpCwAAQBAJ&printsec=frontcover&output=reader&hl=en&pg=GBS.PT44.w.10.0.12):
	* A Docker registry is a service that is used to store docker repositories (e.g. DockerHub, AWS ECR).
	* A Docker repository is a collection of related images (usually of the same name with different tags).
	* A tag is a unique alphanumeric identifier associated with a specific version.

	* This is why in `setup_aws_resources.sh`, the correct command is:

	```
	# $repo_url variable = 595614743545.dkr.ecr.us-east-1.amazonaws.com/ml-server
	$ docker tag ml-server $repo_url
	$ docker push $repo_url:latest
	```

	instead of:

	```
	$ docker tag ml-server $repo_url/ml-server 
	$ docker push $repo_url/ml-server:latest
	```

	* *595614743545.dkr.ecr.us-east-1.amazonaws.com*/**ml-server**
		* *italic* = registry
		* **bold** = repository
		* The variable `$repo_url` contains both the registry and the repository.