counter=0
while [ $counter -le 500 ]
do
	python3 twitter_api.py $counter
	counter=$((counter + 1))
	sleep 900
done
