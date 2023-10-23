# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.support import MicrosoftSupport

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-support
# USAGE
    python update_contact_details_of_support_ticket.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = MicrosoftSupport(
        credential=DefaultAzureCredential(),
        subscription_id="SUBSCRIPTION_ID",
    )

    response = client.support_tickets_no_subscription.update(
        support_ticket_name="testticket",
        update_support_ticket={
            "contactDetails": {
                "additionalEmailAddresses": ["tname@contoso.com", "teamtest@contoso.com"],
                "country": "USA",
                "firstName": "first name",
                "lastName": "last name",
                "phoneNumber": "123-456-7890",
                "preferredContactMethod": "email",
                "preferredSupportLanguage": "en-US",
                "preferredTimeZone": "Pacific Standard Time",
                "primaryEmailAddress": "test.name@contoso.com",
            }
        },
    )
    print(response)


# x-ms-original-file: specification/support/resource-manager/Microsoft.Support/preview/2022-09-01-preview/examples/UpdateContactDetailsOfSupportTicket.json
if __name__ == "__main__":
    main()
