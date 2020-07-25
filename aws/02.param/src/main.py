import datetime
import logging
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def run(event, context):
    current_time = datetime.datetime.now().time()
    function_name = context.function_name
    PARAM_PROVIDER = os.environ['PARAM_PROVIDER']
    PARAM_FUNCTION = os.environ['PARAM_FUNCTION']
    PARAM_FUNCTION_OVER_PROVIDER = os.environ['PARAM_FUNCTION_OVER_PROVIDER']
    PARAM_ENV = os.environ['PARAM_ENV']
    logger.info(
        ("function_name={function_name},"
            +" PARAM_PROVIDER={PARAM_PROVIDER},"
            +" PARAM_FUNCTION={PARAM_FUNCTION},"
            +" PARAM_FUNCTION_OVER_PROVIDER={PARAM_FUNCTION_OVER_PROVIDER},"
            +" PARAM_ENV={PARAM_ENV},"
            +" current_time={current_time}").format(
            function_name=function_name,
            PARAM_PROVIDER=PARAM_PROVIDER,
            PARAM_FUNCTION=PARAM_FUNCTION,
            PARAM_FUNCTION_OVER_PROVIDER=PARAM_FUNCTION_OVER_PROVIDER,
            PARAM_ENV=PARAM_ENV,
            current_time=current_time,
        )
    )
