# Messages to log file and console
MESSAGES_LOG = {
    "authorization": {"message": "The authorization process for the bot number bot_id was not correct.!!! "
                                 "data_authorization"},

    "pre_authorization": {"message": "The authorization process for the bot number bot_id was not correct.!!! {"
                                     "'error': True, 'error_type': 'The parameters required for the request.}"},

    "post_authorization": {"message": "Post requests for the bot_id failed."},

    "third_party_script": {"message": "Incorrect work of a third-party script!"},

    "scenario_fail": {"message": "Warning Order order_id for the bot bot_id failed. Message - 'message', Type_error - "
                                 "'error_type'\n"},

    "socket_error": {"message": "Connection to socket server lost. Message - 'message', Type_error - "
                                "'error_type'\n"},

    "sys_api_error": {"message": "Connection system api server for the bot bot_id lost. Message - 'message', "
                                 "Type_error - 'error_type'\n"}
}
