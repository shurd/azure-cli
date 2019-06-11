# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import
# pylint: disable=line-too-long, too-many-lines

helps['cosmosdb'] = """
type: group
short-summary: Manage Azure Cosmos DB database accounts.
"""

helps['cosmosdb check-name-exists'] = """
type: command
short-summary: Checks if an Azure Cosmos DB account name exists.
examples:
  - name: Checks if an Azure Cosmos DB account name exists. (autogenerated)
    text: az cosmosdb check-name-exists --name MyCosmosDBDatabaseAccount
    crafted: true
"""

helps['cosmosdb collection'] = """
type: group
short-summary: Manage Azure Cosmos DB collections.
"""

helps['cosmosdb create'] = """
type: command
short-summary: Creates a new Azure Cosmos DB database account.
parameters:
  - name: --locations
    short-summary: Add a location to the Cosmos DB database account
    long-summary: |
        Usage:          --locations [KEY=VALUE ...]
        Required Keys:  regionName, failoverPriority
        Optional Key:   isZoneRedundant
        Default:        single region account in the location of the specified resource group.
        Failover priority values are 0 for write regions and greater than 0 for read regions. A failover priority value must be unique and less than the total number of regions.
        Multiple locations can be specified by using more than one `--locations` argument.
examples:
  - name: Creates a new Azure Cosmos DB database account. (autogenerated)
    text: az cosmosdb create --name MyCosmosDBDatabaseAccount --resource-group MyResourceGroup --subscription MySubscription
    crafted: true
  - name: Creates a new Azure Cosmos DB database account with two regions. UK South is zone redundant.
    text: az cosmosdb create -n myaccount -g mygroup --locations regionName=eastus failoverPriority=0 isZoneRedundant=False --locations regionName=uksouth failoverPriority=1 isZoneRedundant=True --enable-multiple-write-locations
"""

helps['cosmosdb database'] = """
type: group
short-summary: Manage Azure Cosmos DB databases.
"""

helps['cosmosdb delete'] = """
type: command
short-summary: Deletes an Azure Cosmos DB database account.
examples:
  - name: Deletes an Azure Cosmos DB database account. (autogenerated)
    text: az cosmosdb delete --name MyCosmosDBDatabaseAccount --resource-group MyResourceGroup
    crafted: true
"""

helps['cosmosdb failover-priority-change'] = """
type: command
short-summary: Changes the failover priority for the Azure Cosmos DB database account.
"""

helps['cosmosdb list'] = """
type: command
short-summary: List Azure Cosmos DB database accounts.
"""

helps['cosmosdb list-connection-strings'] = """
type: command
short-summary: List the connection strings for a Azure Cosmos DB database account.
examples:
  - name: List the connection strings for a Azure Cosmos DB database account. (autogenerated)
    text: az cosmosdb list-connection-strings --name MyCosmosDBDatabaseAccount --resource-group MyResourceGroup
    crafted: true
"""

helps['cosmosdb list-keys'] = """
type: command
short-summary: List the access keys for a Azure Cosmos DB database account.
examples:
  - name: List the access keys for a Azure Cosmos DB database account. (autogenerated)
    text: az cosmosdb list-keys --name MyCosmosDBDatabaseAccount --resource-group MyResourceGroup --subscription MySubscription
    crafted: true
"""

helps['cosmosdb list-read-only-keys'] = """
type: command
short-summary: List the read-only access keys for a Azure Cosmos DB database account.
examples:
  - name: List the read-only access keys for a Azure Cosmos DB database account. (autogenerated)
    text: az cosmosdb list-read-only-keys --name MyCosmosDBDatabaseAccount --resource-group MyResourceGroup
    crafted: true
"""

helps['cosmosdb network-rule'] = """
type: group
short-summary: Manage Azure Comsos DB network rules.
"""

helps['cosmosdb regenerate-key'] = """
type: command
short-summary: Regenerate an access key for a Azure Cosmos DB database account.
examples:
  - name: Regenerate an access key for a Azure Cosmos DB database account. (autogenerated)
    text: az cosmosdb regenerate-key --key-kind primary --name MyCosmosDBDatabaseAccount --resource-group MyResourceGroup
    crafted: true
"""

helps['cosmosdb show'] = """
type: command
short-summary: Get the details of an Azure Cosmos DB database account.
examples:
  - name: Get the details of an Azure Cosmos DB database account. (autogenerated)
    text: az cosmosdb show --name MyCosmosDBDatabaseAccount --resource-group MyResourceGroup
    crafted: true
"""

helps['cosmosdb update'] = """
type: command
short-summary: Update an Azure Cosmos DB database account.
parameters:
  - name: --locations
    short-summary: Add a location to the Cosmos DB database account
    long-summary: |
        Usage:          --locations [KEY=VALUE ...]
        Required Keys:  regionName, failoverPriority
        Optional Key:   isZoneRedundant
        Default:        single region account in the location of the specified resource group.
        Failover priority values are 0 for write regions and greater than 0 for read regions. A failover priority value must be unique and less than the total number of regions.
        Multiple locations can be specified by using more than one `--locations` argument.
examples:
  - name: Update an Azure Cosmos DB database account. (autogenerated)
    text: az cosmosdb update --capabilities EnableGremlin --name MyCosmosDBDatabaseAccount --resource-group MyResourceGroup
    crafted: true
  - name: Creates a new Azure Cosmos DB database account with two regions. UK South is zone redundant.
    text: az cosmosdb update -n myaccount -g mygroup --locations regionName=eastus failoverPriority=0 isZoneRedundant=False --locations regionName=uksouth failoverPriority=1 isZoneRedundant=True --enable-multiple-write-locations
"""
