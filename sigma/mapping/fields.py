field_mapping = {
    "AccessList": "Rule Name",
    "AccessMask": "Access Mask",
    "Accesses": "Accesses",
    "AppID": "Application",
    "AppId": "Application",
    "AppName": "Application",
    "AttributeLDAPDisplayName": ["Username", "Account Name", "Distinguished Name"],
    "AttributeValue": ["Attribute Old Value", "Attribute New Value"],
    "c-useragent": "User Agent",
    "cs-user-agent": "User Agent",
    "cs-username": "Username",
    "CallTrace": "Call Trace",
    "CallerProcessName": "Process Path",
    "cipher": "Ticket Encryption Type",
    "CommandLine": "Command",
    "cs-method": "Method",
    "DestinationHostname": "Destination Hostname",
    "ErrorCode": "Error Code",
    "ExceptionCode": "Error Code",
    "EventID": "Event ID",
    "eventSource": "devicetype",  # Log Source Type - LOGSOURCETYPENAME(devicetype)
    "FailureCode": "Error Code",
    "FileName": "Filename",
    "Filename": "Filename",
    "GrantedAccess": "Granted Access",
    "Hashes": "CONCAT('MD5=', 'MD5 Hash ', 'SHA1=', 'SHA1 Hash ', 'SHA256=', 'SHA256 "
              "Hash ', 'IMPHASH=', 'IMP HASH')",
    # "Hashes": ['MD5 Hash', 'SHA1 Hash', 'SHA256 Hash', 'File Hash'],
    "HostApplication": "Process Path",
    "HostName": "Hostname",
    "Image": ["Process Path", "Process Name"],
    "ImageName": "Process Name",
    "ImagePath": "Process Path",
    "Imphash": "IMP Hash",
    "IntegrityLevel": "Integrity Level",
    "InterfaceUuid": "Source Interface UUID",
    "LogonType": "Logon Type",
    "Message": "Message",
    "Name": "File Path",
    "ObjectName": "Object Name",
    "ObjectType": "Object Type",
    "OriginalFileName": "Filename",
    "ParentCommandLine": "Parent Command",
    "ParentImage": "Parent Process Path",
    "ParentProcessId": "Parent Process ID",
    "Path": "File Path",
    "path": "File Path",
    "Payload": "UTF8(payload)",
    "payload": "UTF8(payload)",
    "PipeName": "Pipe Name",
    "ProcessId": "Process ID",
    "ProcessName": "Process Name",
    "ProcessPath": "Process Path",
    # "Product": "Product",
    "SamAccountName": "SAM Account Name",
    "Service": "Service Name",
    "ServiceFileName": "Service Filename",
    "ServiceName": "Service Name",
    "ShareName": "Share Name",
    "Signed": "Signed",
    "Status": "Status",
    "StartAddress": "Start Address",
    "TargetFilename": "Filename",
    "TargetImage": "Target Process Path",
    "TargetObject": ["Process Name", "Target Process Name", "Object Name"],
    "TargetUserName": "Target Username",
    "TaskName": "Task Name",
    "TicketEncryptionType": "Ticket Encryption Type",
    "UserName": "Username",
    "Username": "Username",
    "md5": "MD5 Hash",
    "method": "Method",
    "NewTargetUserName": "Target Username",
    "sha1": "SHA1 Hash",
    "sha256": "SHA256 Hash",
    "SourceImage": "Source Process Path",
    "USER": "Username",
    "User": "Username",
    "userAgent": "User Agent",
    "user_agent": "User Agent",

    # Functions
    "eventName": "QIDNAME(qid)",
    "ImageLoaded": "CONCAT('file directory', '/', filename)",
}

host_field_mapping = {
    "DestinationIp": "destinationip",
    "DestPort": "destinationport",
    "DestinationPort": "destinationport",
    "destination.port": "destinationport",
    "dst_ip": "destinationip",
    "dst_port": "destinationport",
    "SourcePort": "sourceport",
    "src_ip": "sourceip",
}

unstructured_field_mapping = {
    "c-uri": "URL",
    "c-uri-extension": "URL",
    "c-uri-query": "URL",
    "cs-uri": "URL",
    "cs-uri-query": "URL",
    "cs-uri-stem": "URL",
    "properties.message": "Message",
    "ScriptBlockText": "Message",
    "uri": "URL",
}

unstructured_part_field_mapping = {
    "a0": "Command",
    "a1": "Command",
    "a2": "Command",
    "a3": "Command",
    "a4": "Command",
    "a5": "Command",
}

aql_field_mapping = {
    **field_mapping,
    **host_field_mapping,
    **unstructured_field_mapping,
    **unstructured_part_field_mapping,
}
