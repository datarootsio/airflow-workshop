# a. Create a DAG with two tasks:
#    1. A task that calls the weather API from https://open-meteo.com/ to fetch the weather in your home town. Store the result in XCom.
#    2. A task that reads the weather from XCom and formats the result in a small weather report (print it)
# b. Create a sensor that waits for good weather (> 20 degrees celsius). Create a DAG to test it.