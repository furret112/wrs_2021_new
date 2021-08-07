# For using program of nodeMCU

In nodeMCU_python/src/esp_to_python
1. programming "get_MAC" to get recieve_board's MAC address
2. programming "WRS_send" in send_board(remember to change recieve_board's MAC address)
3. programming "WRS_recieve" in recieve_board
4. connect your recieve_board to PC 
5. check your recieve_board's serial port by typing "ls /dev/tty* " in the terminal
6. give your serial port permission by typing "sudo chmod 777 /dev/{your_port} " in the terminal

# For using nodeMCU to connect PC by USB

Drag "nodeMCU_python" to your {your_workspace}/src 

In your workspace
1. $source devel/setup.bash
2. $roslaunch nodeMCU_python run_esp.launch port:=/dev/ttyUSB0

PS, "port" is default to /dev/ttyUSB0 
