# Cisco Intersight Universal API Calls
The Cisco Intersight Universal API Calls module provides a set of functions that simplify creation, retrieval, modification, and deletion of resources on Cisco Intersight. Any API type listed in the Cisco Intersight API Reference library can be accessed including those which do not yet have a specific module in the Intersight SDK for Python.

## Prerequisites:
1. Python 3 installed, which can be downloaded from https://www.python.org/downloads/.
2. The Cisco Intersight SDK for Python, which can be installed by running: "pip install git+https://github.com/CiscoUcs/intersight-python.git". More information on the Cisco Intersight SDK for Python can be found at https://github.com/CiscoUcs/intersight-python.
3. An API key from your Intersight account. To learn how to generate an API key for your Intersight account, more information can be found at https://intersight.com/help/features#rest_apis.
4. The path to any API types you are interested in working with. For example, if you are interested in creating an Adapter Configuration Policy on Intersight, you would need the path "adapter/ConfigPolicies". The path to available Cisco Intersight API types can be found in the API Reference section at https://intersight.com/apidocs/introduction/overview/.

## Getting Started:

1. Please ensure the above prerequisites have been met.
2. Download the intersight_universal_api_calls.py file for the Cisco Intersight Universal API Calls module from here on GitHub.
3. Edit the intersight_universal_api_calls.py file to set the key_id and key variables.
   - Open the intersight_universal_api_calls.py file in an IDLE or text editor of choice.
   - Find the comment **"MODULE REQUIREMENT #1"**.
   - Underneath, you will find the variable **key_id = ""**.
   - Fill in between the quotes of the key_id variable the ID of your API key. For example: **_key_id = "5c8988507564612d302ec143/5c82fc477564612d3088eb2f/5c8987b17564612d302eaaff"_**.
   - Find the comment **"MODULE REQUIREMENT #2"**.
   - Underneath, you will find the variable **key = ""**.
   - Fill in between the quotes of the key variable your system's file path to the SecretKey.txt file for your API key. For example: **_key = "C:\Keys\Key1\SecretKey.txt"_**.
4. The file is now ready for use via runni9ng directly or import. See the **"How to Use:"** section for the available functions and directions on use.

## How to Use:
#### Available Functions:
The Cisco Intersight Universal API Calls module contains six functions for creating, retrieving, modifying, and deleting resources. Here are the functions and sample command usage for each:

- **iu_get()** - Performs a universal or generic GET on objects under any available Intersight API type.
   - The required arguments are **api_path**.
   - Here are sample commands to retrieve all available Adapter Configuration policies:
   ```
   adapters = "adapter/ConfigPolicies"
   
   iu_get(adapters)
   ```
   
- **iu_get_moid()** - Performs a universal or generic GET on a specified object under any available Intersight API type.
   - The required arguments are **api_path** and **moid**.
   - Here are sample commands to retrieve a specific Adapter Configuration policy. The MOID below is an example:
   ```
   adapters = "adapter/ConfigPolicies"
   
   adapter1_moid = "5c8987b17564777d30212345"
   
   iu_get_moid(adapters,adapter1_moid)
   ```

- **iu_delete_moid()** - Performs a universal or generic DELETE on a specified object under any available Intersight API type.
   - The required arguments are **api_path** and **moid**.
   - Here are sample commands to delete a specific Adapter Configuration policy. The MOID below is an example:
   ```
   adapters = "adapter/ConfigPolicies"
   
   adapter1_moid = "5c8987b17564777d30212345"
   
   iu_delete_moid(adapters,adapter1_moid)
   ```

- **iu_post()** - Performs a universal or generic POST of an object under any available Intersight API type.
   - The required arguments are **api_path** and **body**.
   - Here are sample commands to create a new Adapter Configuration policy with 1 slot and LLDP and FIP protocol settings enabled:
   ```
   adapters = "adapter/ConfigPolicies"
   
   adapter2_body = {
   'Name': 'Adapter_Policy2', 
   'Settings': [
   {
   'ObjectType': 'adapter.AdapterConfig', 
   'EthSettings': {'ObjectType': 'adapter.EthSettings', 'LldpEnabled': True}, 
   'FcSettings': {'ObjectType': 'adapter.FcSettings', 'FipEnabled': True}, 
   'SlotId': '1'
   }
   ]
   }
   
   iu_post(adapters,adapter2_body)
   ```

- **iu_post_moid()** - Performs a universal or generic POST on a specified object under any available Intersight API type.
   - The required arguments are **api_path**, **moid** and **body**.
   - Here are sample commands to modify a specific Adapter Configuration policy. In this example, the LLDP and FIP protocol settings on slot 1 of the Adapter Configuration policy are being disabled. The MOID below is an example:
   ```
   adapters = "adapter/ConfigPolicies"
   
   adapter2_moid = "5c8987b17564777d30252537"
   
   adapter2_body = {
   'Settings': [
   {
   'EthSettings': {'ObjectType': 'adapter.EthSettings', 'LldpEnabled': False},
   'FcSettings': {'ObjectType': 'adapter.FcSettings', 'FipEnabled': False}, 
   'SlotId': '1'
   }
   ]
   }
   
   iu_post_moid(adapters,adapter2_body)
   ```

- **iu_patch_moid()** - Performs a universal or generic PATCH on a specified object under any available Intersight API type.
   - The required arguments are **api_path**, **moid** and **body**.
   - Here are sample commands to modify a specific Adapter Configuration policy. In this example, the Adapter Configuration policy name is being changed. The MOID below is an example:
   ```
   adapters = "adapter/ConfigPolicies"
   
   adapter2_moid = "5c8987b17564777d30252537"
   
   adapter2_body = {'Name': 'Adapter_Policy2_Updated'}
   
   iu_patch_moid(adapters,adapter2_body)
   ```

### Author:
Ugo Emekauwa

### Contact Information:
uemekauw@cisco.com or uemekauwa@gmail.com
