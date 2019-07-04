"""
Cisco Intersight Universal API Calls Module, v1.1
Author: Ugo Emekauwa
Contact: uemekauw@cisco.com, uemekauwa@gmail.com
Summary: The Cisco Intersight Universal API Calls module provides
          a set of functions that simplify creation, retrieval,
          modification, and deletion of resources on Cisco Intersight.
"""

# Import needed Python modules
import sys
import json
import requests
import os
import intersight
from intersight.intersight_api_client import IntersightApiClient


# MODULE REQUIREMENT 1
"""
For the following variable below named key_id, please fill in between
the quotes your Intersight API Key ID.

Here is an example: key_id = "5c89885075646127773ec143/5c82fc477577712d3088eb2f/5c8987b17577712d302eaaff"
"""
key_id = ""

# MODULE REQUIREMENT 2
"""
For the following variable below named key, please fill in between
the quotes your system's file path to your Intersight API key "SecretKey.txt" file.

Here is an example: key = "C:\Keys\Key1\SecretKey.txt"
"""
key = ""


# Define Intersight SDK IntersightApiClient variables
# Tested on Cisco Intersight API Reference v1.0.9-853
base_url = "https://intersight.com/api/v1"
api_instance = IntersightApiClient(host=base_url,private_key=key,api_key_id=key_id)

# Establish Intersight Universal Functions

def iu_get(api_path):
  """This is a function to perform a universal or generic GET on objects under available Intersight API types,
  including those not yet defined in the Intersight SDK for Python. An argument for the API type path is required.

  Args:
    api_path: The path to the targeted Intersight API type. For example, to specify the Intersight API type for
      adapter configuration policies, enter "adapter/ConfigPolicies". More API types can be found in the Intersight
      API reference library at https://intersight.com/apidocs/introduction/overview/.

  Returns:
    A dictionary containing all objects of the specified API type. If the API type is inaccessible, an
    implicit value of None will be returned.
  """
  full_resource_path = "/" + api_path
  try:
    api_instance.call_api(full_resource_path,"GET")
    response = api_instance.last_response.data
    results = json.loads(response)
    print("The API resource path '" + api_path + "' has been accessed successfully.\n")
    return results
  except:
    print("Unable to access the API resource path '" + api_path + "'.\n")


def iu_get_moid(api_path,moid):
  """This is a function to perform a universal or generic GET on a specified object under available
  Intersight API types, including those not yet defined in the Intersight SDK for Python. An argument for the
  API type path and MOID (managed object identifier) is required.
  
  Args:
    api_path: The path to the targeted Intersight API type. For example, to specify the Intersight API type for
      adapter configuration policies, enter "adapter/ConfigPolicies". More API types can be found in the Intersight
      API reference library at https://intersight.com/apidocs/introduction/overview/.
    moid: The managed object ID of the targeted API object.

  Returns:
    A dictionary containing all parameters of the specified API object. If the API object is inaccessible, an
    implicit value of None will be returned.
  """
  full_resource_path = "/" + api_path + "/" + moid
  try:
    api_instance.call_api(full_resource_path,"GET")
    response = api_instance.last_response.data
    results = json.loads(response)
    print("The object located at the resource path '" + full_resource_path + "' has been accessed succesfully.\n")
    return results
  except:
    print("Unable to access the object located at the resource path '" + full_resource_path + "'.\n")


def iu_delete_moid(api_path,moid):
  """This is a function to perform a universal or generic DELETE on a specified object under available
  Intersight API types, including those not yet defined in the Intersight SDK for Python. An argument for the
  API type path and MOID (managed object identifier) is required.
    
  Args:
    api_path: The path to the targeted Intersight API type. For example, to specify the Intersight API type for
      adapter configuration policies, enter "adapter/ConfigPolicies". More API types can be found in the Intersight
      API reference library at https://intersight.com/apidocs/introduction/overview/.
    moid: The managed object ID of the targeted API object.

  Returns:
    A statement indicating whether the DELETE method was successful or failed.
  
  Raises:
    Exception: An exception occured while performing the API call. The exact error will be
    specified.
  """
  full_resource_path = "/" + api_path + "/" + moid
  try:
    api_instance.call_api(full_resource_path,"DELETE")
    print("The deletion of the object located at the resource path '" + full_resource_path + "' has been completed.\n")
    return "The DELETE method was successful."
  except Exception as exception_message:
    print("Unable to access the object located at the resource path '" + full_resource_path + "'.\n")
    print(exception_message)
    return "The DELETE method failed."


def iu_post(api_path,body):
  """This is a function to perform a universal or generic POST of an object under available Intersight
  API types, including those not yet defined in the Intersight SDK for Python. An argument for the
  API type path and body configuration data is required.
  
  Args:
    api_path: The path to the targeted Intersight API type. For example, to specify the Intersight API type for
      adapter configuration policies, enter "adapter/ConfigPolicies". More API types can be found in the Intersight
      API reference library at https://intersight.com/apidocs/introduction/overview/.
    body: The content to be created under the targeted API type. This should be provided in a dictionary format.
  
  Returns:
    A statement indicating whether the POST method was successful or failed.
    
  Raises:
    Exception: An exception occured while performing the API call. The exact error will be
    specified.
  """
  full_resource_path = "/" + api_path
  try:
    api_instance.call_api(full_resource_path,"POST",body=body)
    print("The creation of the object under the resource path '" + full_resource_path + "' has been completed.\n")
    return "The POST method was successful."
  except Exception as exception_message:
    print("Unable to create the object under the resource path '" + full_resource_path + "'.\n")
    print(exception_message)
    return "The POST method failed."


def iu_post_moid(api_path,moid,body):
  """This is a function to perform a universal or generic POST of a specified object under available Intersight
  API types, including those not yet defined in the Intersight SDK for Python. An argument for the
  API type path, MOID (managed object identifier), and body configuration data is required.
      
  Args:
    api_path: The path to the targeted Intersight API type. For example, to specify the Intersight API type for
      adapter configuration policies, enter "adapter/ConfigPolicies". More API types can be found in the Intersight
      API reference library at https://intersight.com/apidocs/introduction/overview/.
    moid: The managed object ID of the targeted API object.
    body: The content to be modified on the targeted API object. This should be provided in a dictionary format.
  
  Returns:
    A statement indicating whether the POST method was successful or failed.
    
  Raises:
    Exception: An exception occured while performing the API call. The exact error will be
    specified.
  """
  full_resource_path = "/" + api_path + "/" + moid
  try:
    api_instance.call_api(full_resource_path,"POST",body=body)
    print("The update of the object located at the resource path '" + full_resource_path + "' has been completed.\n")
    return "The POST method was successful."
  except Exception as exception_message:
    print("Unable to access the object located at the resource path '" + full_resource_path + "'.\n")
    print(exception_message)
    return "The POST method failed."


def iu_patch_moid(api_path,moid,body):
  """This is a function to perform a universal or generic PATCH of a specified object under available Intersight
  API types, including those not yet defined in the Intersight SDK for Python. An argument for the
  API type path, MOID (managed object identifier), and body configuration data is required.
      
  Args:
    api_path: The path to the targeted Intersight API type. For example, to specify the Intersight API type for
      adapter configuration policies, enter "adapter/ConfigPolicies". More API types can be found in the Intersight
      API reference library at https://intersight.com/apidocs/introduction/overview/.
    moid: The managed object ID of the targeted API object.
    body: The content to be modified on the targeted API object. This should be provided in a dictionary format.
  
  Returns:
    A statement indicating whether the PATCH method was successful or failed.
    
  Raises:
    Exception: An exception occured while performing the API call. The exact error will be
    specified.
  """
  full_resource_path = "/" + api_path + "/" + moid
  try:
    api_instance.call_api(full_resource_path,"PATCH",body=body)
    print("The update of the object located at the resource path '" + full_resource_path + "' has been completed.\n")
    return "The PATCH method was successful."
  except Exception as exception_message:
    print("Unable to access the object located at the resource path '" + full_resource_path + "'.\n")
    print(exception_message)
    return "The PATCH method failed."


# Verify API key variables have been set
key_id_setting = key_id.strip()
if key_id_setting is None or len(key_id_setting) is 0 or "/" not in key_id_setting:
  print("\nThe key_id variable for the intersight_universal_api_calls module has not been set correctly!")
  print("Please edit the intersight_universal_api_calls.py file and set the key_id variable \nwith the ID of your API key in order for the module to work properly.")
key_setting = key.strip()
if key_setting is None or len(key_setting) is 0 or not os.path.isfile(key_setting):
  print("\nThe key variable for the intersight_universal_api_calls module has not been set correctly!")
  print("Please edit the intersight_universal_api_calls.py file and set the key variable \nwith your system's path to your API key SecretKey.txt file in order for the module to work properly.")
