# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import
# pylint: disable=line-too-long, too-many-lines

helps['apim'] = """
type: group
short-summary: Manage Azure API Management services.
"""

helps['apim api'] = """
type: group
short-summary: Manage Azure API Management API's.
"""

helps['apim backup'] = """
type: command
short-summary: Creates a backup of the API Management service to the given Azure Storage Account. This is long running operation and could take several minutes to complete.
examples:
  - name: Create a backup of the API Management service instance
    text: |-
        az apim backup --name MyApim -g MyResourceGroup --backup-name myBackup \
             --storage-account-name mystorageaccount --storage-account-container backups \
             --storage-account-key Ay2ZbdxLnD4OJPT29F6jLPkB6KynOzx85YCObhrw==
"""

helps['apim create'] = """
type: command
short-summary: Create an API Management service instance.
parameters:
  - name: --name -n
    type: string
    short-summary: unique name of the service instance to be created
    long-summary: |
        The name must be globally unique since it will be included as the gateway
        hostname like' https://my-api-servicename.azure-api.net'.  See examples.
examples:
  - name: Create a Developer tier API Management service.
    text: |-
        az apim create --name MyApim -g MyResourceGroup -l eastus --publisher-email email@mydomain.com --publisher-name Microsoft
  - name: Create a Consumption tier API Management service.
    text: |-
        az apim create --name MyApim -g MyResourceGroup -l eastus --sku-name Consumption --enable-client-certificate \\
            --publisher-email email@mydomain.com --publisher-name Microsoft
"""

helps['apim delete'] = """
type: command
short-summary: Deletes an API Management service.
examples:
  - name: Delete an API Management service.
    text: >
        az apim delete -n MyApim -g MyResourceGroup
"""

helps['apim list'] = """
type: command
short-summary: List API Management service instances.
"""

helps['apim show'] = """
type: command
short-summary: Show details of an API Management service instance.
"""

helps['apim update'] = """
type: command
short-summary: Update an API Management service instance.
"""

helps['apim api list'] = """
type: command
short-summary: List API Management API's.
"""

helps['apim api show'] = """
type: command
short-summary: Show details of an API Management API.
"""

helps['apim api delete'] = """
type: command
short-summary: Delete an API Management API.
"""

helps['apim api create'] = """
type: command
short-summary: Create an API Management API.
parameters:
  - name: --service-name
    type: string
    short-summary: name of the service instance
  - name: --api-id
    type: string
    short-summary: unique name of the api to be created
    long-summary: |
        API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
  - name: --path
    type: string
    short-summary: Path to the API
  - name: --display-name
    type: string
    short-summary: Display name of the API to be created
examples:
  - name: Create a basic API.
    text: |-
        az apim api create --service-name MyApim -g MyResourceGroup --api-id MyApi --path '/myapi' --display-name 'My API'
"""

helps['apim api update'] = """
type: command
short-summary: Update an API Management API.
parameters:
  - name: --service-name
    type: string
    short-summary: name of the service instance
  - name: --api-id
    type: string
    short-summary: unique name of the api to be created
    long-summary: |
        API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
examples:
  - name: Create a basic API.
    text: |-
        az apim api update --service-name MyApim -g MyResourceGroup --api-id MyApi --description foo
"""