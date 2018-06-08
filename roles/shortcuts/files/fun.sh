des()
	{
	docker ps -aq | xargs docker stop 
	docker ps -aq | xargs docker rm
	} 

alias st='docker ps -a'

com()
	{
	git add .
	git commit -am "test"
	git push origin master
        }
