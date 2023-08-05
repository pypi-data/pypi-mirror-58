function GetOciTopLevelCommand_dts() {
    return 'dts'
}

function GetOciSubcommands_dts() {
    $ociSubcommands = @{
        'dts' = 'appliance job nfs-dataset physical-appliance'
        'dts appliance' = 'cancel delete get-passphrase list never-receive request request-entitlement show show-entitlement update-shipping-address'
        'dts job' = 'change-compartment close create delete detach-devices-details list show update verify-upload-user-credentials'
        'dts job detach-devices-details' = 'change-compartment'
        'dts nfs-dataset' = 'activate create deactivate delete get-seal-manifest list reopen seal seal-status set-export show'
        'dts physical-appliance' = 'configure-encryption finalize initialize-authentication list show unlock unregister'
    }
    return $ociSubcommands
}

function GetOciCommandsToLongParams_dts() {
    $ociCommandsToLongParams = @{
        'dts appliance cancel' = 'appliance-label from-json help job-id'
        'dts appliance delete' = 'appliance-label force from-json help job-id'
        'dts appliance get-passphrase' = 'appliance-label from-json help job-id'
        'dts appliance list' = 'all from-json help job-id'
        'dts appliance never-receive' = 'appliance-label from-json help job-id'
        'dts appliance request' = 'address1 address2 address3 address4 addressee care-of city-or-locality country email from-json help job-id phone-number state-province-region zip-postal-code'
        'dts appliance request-entitlement' = 'compartment-id defined-tags display-name email freeform-tags from-json help max-wait-seconds name wait-for-state wait-interval-seconds'
        'dts appliance show' = 'appliance-label from-json help job-id'
        'dts appliance show-entitlement' = 'compartment-id from-json help'
        'dts appliance update-shipping-address' = 'address1 address2 address3 address4 addressee appliance-label care-of city-or-locality country email force from-json help job-id phone-number state-province-region zip-postal-code'
        'dts job change-compartment' = 'compartment-id from-json help if-match job-id'
        'dts job close' = 'from-json help job-id'
        'dts job create' = 'bucket compartment-id defined-tags device-type display-name freeform-tags from-json help max-wait-seconds wait-for-state wait-interval-seconds'
        'dts job delete' = 'force from-json help job-id'
        'dts job detach-devices-details change-compartment' = 'compartment-id from-json help if-match transfer-job-id'
        'dts job list' = 'all compartment-id display-name from-json help lifecycle-state'
        'dts job show' = 'from-json help job-id'
        'dts job update' = 'defined-tags display-name force freeform-tags from-json help job-id'
        'dts job verify-upload-user-credentials' = 'bucket from-json help'
        'dts nfs-dataset activate' = 'appliance-profile from-json help ip name rw subnet-mask-length world'
        'dts nfs-dataset create' = 'appliance-profile from-json help ip name rw subnet-mask-length world'
        'dts nfs-dataset deactivate' = 'appliance-profile from-json help name'
        'dts nfs-dataset delete' = 'appliance-profile from-json help name'
        'dts nfs-dataset get-seal-manifest' = 'appliance-profile from-json help name output-file'
        'dts nfs-dataset list' = 'appliance-profile from-json help'
        'dts nfs-dataset reopen' = 'appliance-profile from-json help name'
        'dts nfs-dataset seal' = 'appliance-profile from-json help name wait'
        'dts nfs-dataset seal-status' = 'appliance-profile from-json help name'
        'dts nfs-dataset set-export' = 'appliance-profile from-json help ip name rw subnet-mask-length world'
        'dts nfs-dataset show' = 'appliance-profile from-json help name'
        'dts physical-appliance configure-encryption' = 'appliance-label appliance-profile from-json help job-id'
        'dts physical-appliance finalize' = 'appliance-label appliance-profile from-json help job-id skip-upload-user-check'
        'dts physical-appliance initialize-authentication' = 'access-token appliance-cert-fingerprint appliance-ip appliance-label appliance-port appliance-profile from-json help job-id profile'
        'dts physical-appliance list' = 'from-json help'
        'dts physical-appliance show' = 'appliance-profile from-json help'
        'dts physical-appliance unlock' = 'appliance-label appliance-profile from-json help job-id'
        'dts physical-appliance unregister' = 'appliance-profile from-json help'
    }
    return $ociCommandsToLongParams
}

function GetOciCommandsToShortParams_dts() {
    $ociCommandsToShortParams = @{
        'dts appliance cancel' = '? h'
        'dts appliance delete' = '? h'
        'dts appliance get-passphrase' = '? h'
        'dts appliance list' = '? h'
        'dts appliance never-receive' = '? h'
        'dts appliance request' = '? h'
        'dts appliance request-entitlement' = '? c h'
        'dts appliance show' = '? h'
        'dts appliance show-entitlement' = '? c h'
        'dts appliance update-shipping-address' = '? h'
        'dts job change-compartment' = '? c h'
        'dts job close' = '? h'
        'dts job create' = '? c h'
        'dts job delete' = '? h'
        'dts job detach-devices-details change-compartment' = '? c h'
        'dts job list' = '? c h'
        'dts job show' = '? h'
        'dts job update' = '? h'
        'dts job verify-upload-user-credentials' = '? h'
        'dts nfs-dataset activate' = '? h'
        'dts nfs-dataset create' = '? h'
        'dts nfs-dataset deactivate' = '? h'
        'dts nfs-dataset delete' = '? h'
        'dts nfs-dataset get-seal-manifest' = '? h'
        'dts nfs-dataset list' = '? h'
        'dts nfs-dataset reopen' = '? h'
        'dts nfs-dataset seal' = '? h'
        'dts nfs-dataset seal-status' = '? h'
        'dts nfs-dataset set-export' = '? h'
        'dts nfs-dataset show' = '? h'
        'dts physical-appliance configure-encryption' = '? h'
        'dts physical-appliance finalize' = '? h'
        'dts physical-appliance initialize-authentication' = '? h'
        'dts physical-appliance list' = '? h'
        'dts physical-appliance show' = '? h'
        'dts physical-appliance unlock' = '? h'
        'dts physical-appliance unregister' = '? h'
    }
    return $ociCommandsToShortParams
}