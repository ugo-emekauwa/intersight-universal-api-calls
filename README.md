# Cisco Intersight Universal API Calls
The Cisco Intersight Universal API Calls module provides a set of functions that simplify creation, modification, and deletion of resources.

## Prerequisites:
1. Python 3 installed, which can be downloaded from https://www.python.org/downloads/.
2. The Cisco Intersight SDK for Python, which can be installed by running: "pip install git+https://github.com/CiscoUcs/intersight-python.git". More information on the Cisco Intersight SDK for Python can be found at https://github.com/CiscoUcs/intersight-python.
3. An API key from your Intersight account. To learn how to generate an API key for your Intersight account, more information can be found at https://intersight.com/help/features#rest_apis.

## Getting Started:

1. Please ensure the above prerequistes have been met.
2. Download the intersight_universal_api_calls.py file for the Cisco Intersight Universal API Calls module from here on GitHub.
3. Edit the intersight_universal_api_calls.py file to set the key_id and key variables.
   - Open the intersight_universal_api_calls.py file and find the comment **"MODULE REQUIREMENT #1"**.
   - Underneath, you will find the variable **key_id = None**.
   - Remove the value of **None**, and replace it with the ID of your API key within quotes. For example: **_key_id = "5c8988507564612d302ec143/5c82fc477564612d3088eb2f/5c8987b17564612d302eaaff"_**.
   - Find the comment **"MODULE REQUIREMENT #2"**.
   - Underneath, you will find the variable **key = None**.
   - Remove the value of **None**, and replace it with your system's file path to the SecretKey.txt file for your API key. For example: **_key = "C:\Keys\Key1\SecretKey.txt"_**.
4. The file is now ready for use via runni9ng directly or import. See the **"How to Use"** section for the available functions and directions on use.
  

### Author:
Ugo Emekauwa

### Contact Information:
uemekauw@cisco.com or uemekauwa@gmail.com
